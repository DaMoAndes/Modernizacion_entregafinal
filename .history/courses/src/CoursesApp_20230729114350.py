from flask import Flask, jsonify, Response
from .modelos import db
from flask_restful import Api
from flask_jwt_extended import JWTManager
from .vistas.CoursesLogic import Courses, Course, GetNumCoursesByTimeRange, SoftDelete, RestoreDeletedCourse, \
    GetNumCoursesByTimeRange, HealthCheck

app = Flask(__name__)
app.config.from_object("src.config.Config")


#@app.before_first_request

#def create_tables():
# db.create_all()


db.init_app(app)


@app.route("/courses/ping")
def hello_world():
    return "pong", 200


api = Api(app)
api.add_resource(Courses, '/Courses')
api.add_resource(Course, '/Course/<courseId>')
api.add_resource(SoftDelete, '/Softdelete/<courseId>')
api.add_resource(RestoreDeletedCourse, '/Restore/<courseId>')
api.add_resource(GetNumCoursesByTimeRange, '/CoursesByTimeRange')
api.add_resource(HealthCheck, '/ping')

jwt = JWTManager(app)
