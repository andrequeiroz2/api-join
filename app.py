from flask import Flask
from flask_restful import Api
from join.api.join_route import init_join_api

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "todo-api/api-join:latest"

    api = Api(app)
    init_join_api(api)


    return app