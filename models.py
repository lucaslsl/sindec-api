from mongoengine import *
import datetime
from flask_mongoengine import MongoEngine

db=MongoEngine()


class AgeGroupEntry(db.EmbeddedDocument):
    FaixaEtariaConsumidor = StringField()
    Quantidade = IntField(required=True)

class CostumersData(db.EmbeddedDocument):
    SexoConsumidor = StringField()
    Total = IntField(required=True)
    Entradas = ListField(EmbeddedDocumentField(AgeGroupEntry))

class StateDataEntry(db.Document):
    UF = StringField(required=True)
    Ano = IntField(required=True)
    Mes = IntField(required=True)
    Total = IntField(required=True)
    Dados = ListField(EmbeddedDocumentField(CostumersData))
