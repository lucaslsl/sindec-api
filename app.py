import os
from flask import Flask,request,jsonify
from flask_mongoengine import MongoEngine
from flask_restful import Resource, Api
from models import StateDataEntry

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = MongoEngine(app)


class StatesEntries(Resource):
    def get(self):
        filter_UF = request.args.get('UF', None)
        filter_Ano = request.args.get('Ano', None)
        filter_Mes = request.args.get('Mes', None)

        pg_page = request.args.get('page', 1)
        pg_page = int(pg_page)
        pg_per_page = request.args.get('per_page', 27)
        pg_per_page = int(pg_per_page)

        if pg_per_page>27:
            pg_per_page = 27

        queryset = StateDataEntry.objects().order_by('-Ano','-Mes')

        if filter_UF is not None:
            queryset = queryset.filter(UF=filter_UF)
        if filter_Ano is not None:
            queryset = queryset.filter(Ano=int(filter_Ano))

        if filter_Mes is not None:
            queryset = queryset.filter(Mes=int(filter_Mes))

        queryset = queryset.paginate(page=pg_page, per_page=pg_per_page)

        return jsonify(queryset.items)

api = Api(app)
api.add_resource(StatesEntries, '/api/v1/reclamacoes', endpoint="reclamacoes")

if __name__ == "__main__":
    app.run(port=5001)