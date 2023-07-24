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
        courses = CourseModel.query.all()
        if( not courses):
            return {"msg": "No existen cursos"}, 401
        return [(course.id) for course in courses], 200
    
class GetNumCoursesByTimeRange(Resource):
    pass

class RestoreDeletedCourse(Resource):
    pass

class SoftDelete(Resource):
    pass

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