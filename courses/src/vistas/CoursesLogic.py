import json
from urllib.parse import urlparse, parse_qs
from flask_restful import Resource
from ..modelos import  db, CourseModel, CourseModelSchema
from flask import request, Response
import datetime

courseModel_schema = CourseModelSchema()

class Courses(Resource):
    def post(self):
        if  request.is_json:
            parse_json = request.get_json()
            if(parse_json.get('id', None)):
                curso = CourseModel.query.filter((CourseModel.id==f"{parse_json.get('id', None)}")).all()
                if len(curso) > 0:
                    return {"msg": "El recurso ya existe"}, 401
            nuevo_course = CourseModel(
                    id = parse_json.get('id', None),
                    name = parse_json.get('name', None),
                    timeZone = parse_json.get('timeZone', None),
                    institute = parse_json.get('institute', None),
                    createdAt = datetime.datetime.now(),
                    deletedAt ='null'
                    )
            
            db.session.add(nuevo_course)
            db.session.commit()
            return {
                "id":f"{nuevo_course.id}",
                "name":f"{nuevo_course.name}",
                "timeZone":f"{nuevo_course.timeZone}",
                "institute": f"{nuevo_course.institute}",
                "createdAt": f"{nuevo_course.createdAt}"
                }, 201
        else:
            return {
                "msg": "No se pudo crear el curso"
                }, 400
    
    def get(self):
        if  request.is_json:
            id_list = request.get_json()
            courses_list = []
            for id in id_list:
                curso = CourseModel.query.filter((CourseModel.id==int(id))).first()
                if curso != None:
                    courses_list.append(curso)
            if courses_list == []:
                return {"msg": "No existen los cursos"}, 401
            return json.dumps(courses_list)
        else:
            return {
                "msg": "No se pudo hacer la búsqueda"
                }, 400
    
class GetNumCoursesByTimeRange(Resource):
    pass

class RestoreDeletedCourse(Resource):
    def put(self, courseId):
        course = CourseModel.query.get(int(courseId))
        if not course:
            return {
                "msg": "No se encuentra el curso."
                }, 400
        else:
            course.deletedAt = None
            return "Course was restored"

class SoftDelete(Resource):
    def put(self, courseId):
        course = CourseModel.query.get(int(courseId))
        if not course:
            return {
                "msg": "No se encuentra el curso."
                }, 400
        else:
            course.deletedAt = datetime.datetime.now()
            return str(course.deletedAt)

class Course(Resource):
    def get(self, courseId):
        course = CourseModel.query.get(courseId)
        if not course:
            return {
                "msg": "No se encuentra el curso."
                }, 400
        print(datetime.datetime.now())             
        return courseModel_schema.dump(course), 200 
        
    def delete(self, courseId):
        course = CourseModel.query.get(courseId)
        if not course:
            return {
                "msg": "No se encuentra el curso."
                }, 404
        else:
            db.session.delete(course)
            db.session.commit()
            return {
                "msg": "Curso Eliminado correctamente."
            }, 200
    
    def put(self):
        if request.is_json:
            parse_json = request.get_json()
            print(parse_json)