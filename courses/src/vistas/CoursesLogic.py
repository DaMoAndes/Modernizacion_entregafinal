import json
from urllib.parse import urlparse, parse_qs
from flask_restful import Resource
from modelos import  db, CourseModel, CourseModelSchema
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
                    deletedAt = None
                    )
            
            db.session.add(nuevo_course)
            db.session.commit()
            return {
                "id":f"{nuevo_course.id}",
                "name":f"{nuevo_course.name}",
                "timeZone":f"{nuevo_course.timeZone}",
                "institute": f"{nuevo_course.institute}",
                "createdAt": f"{nuevo_course.createdAt}",
                "deletedAt": "null"
                }, 200
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
            return [courseModel_schema.dump(c) for c in courses_list], 200
        else:
            return {
                "msg": "No se pudo hacer la búsqueda"
                }, 400
    
class GetNumCoursesByTimeRange(Resource):
    def get(self):
        if  request.is_json:
            parse_json = request.get_json()
            if (parse_json.get('startTime') is None) or (parse_json.get('endTime') is None):
                return {"msg": "Parámetros inválidos"}, 401
            else:
                startTime = datetime.datetime.strptime(parse_json.get('startTime'), "%Y-%m-%dT%H:%M:%S.%fZ")
                endTime = datetime.datetime.strptime(parse_json.get('endTime'), "%Y-%m-%dT%H:%M:%S.%fZ")
                courses = CourseModel.query.filter((CourseModel.createdAt>=startTime and CourseModel.createdAt<endTime)).all()
                return json.dumps(courses), 200
        else:
            return {
                "msg": "No se pudo hacer la consulta"
                }, 400

class RestoreDeletedCourse(Resource):
    def put(self, courseId):
        course = CourseModel.query.get(int(courseId))
        if not course:
            return {
                "msg": "No se encuentra el curso."
                }, 400
        else:
            course.deletedAt = None
            db.session.commit()
            return "Course was restored", 200

class SoftDelete(Resource):
    def put(self, courseId):
        course = CourseModel.query.get(int(courseId))
        if not course:
            return {
                "msg": "No se encuentra el curso."
                }, 400
        else:
            course.deletedAt = datetime.datetime.now()
            db.session.commit()
            return str(course.deletedAt), 200

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
    
    def put(self, courseId):
        if  request.is_json:
            parse_json = request.get_json()
            if (parse_json.get('id') is None):
                return {"msg": "No se proporcionó id"}, 401
            if ((parse_json.get('name') is None) 
            and (parse_json.get('timeZone') is None) 
            and (parse_json.get('institute') is None)):
                return {"msg": "Parámetros inválidos"}, 401
            course = CourseModel.query.get(courseId)
            if (parse_json.get('name') != None):
                course.name = parse_json.get('name')
            if (parse_json.get('timeZone') != None):
                course.timeZone = parse_json.get('timeZone')
            if (parse_json.get('institute') != None):
                course.institute = parse_json.get('institute')
            db.session.commit()
            return courseModel_schema.dump(course), 200 
        else:
            return {
                "msg": "No se pudo modificar el curso"
                }, 400
        
class HealthCheck(Resource):
    def get(self):
        return "Pong", 200