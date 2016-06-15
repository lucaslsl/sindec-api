import os
from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = MongoEngine(app)

@app.route("/")
def hello():
    return "Complaints API"

if __name__ == "__main__":
    app.run()