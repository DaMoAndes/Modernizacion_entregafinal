from flask import Flask, jsonify, Response
from .modelos import db
from flask_restful import Api
from flask_jwt_extended import JWTManager
from .vistas import ListCourse

app = Flask(__name__)
app.config.from_object("src.config.Config")
@app.before_first_request

def create_tables():
    db.create_all()
db.init_app(app)


@app.route("/courses/ping")
def hello_world():
    return "pong", 200

api = Api(app)
api.add_resource(ListCourse, '/courses')

jwt = JWTManager(app)