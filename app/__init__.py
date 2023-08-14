from flask import Flask

app = Flask(__name__)


def create_app(enviroment:dict):

    app.config.from_object(enviroment)
    return app