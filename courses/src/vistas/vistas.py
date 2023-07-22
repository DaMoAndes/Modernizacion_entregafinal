from flask_restful import Resource
from ..modelos import  db, Course, CourseSchema
from flask import request, Response
import datetime


course_schema = CourseSchema()
class ListCourse(Resource):
    def get(self):
        courseId = 1
        course = Course.query.get(courseId)
        if not course:  
            return Response(status=204) 
        print(datetime.datetime.now())             
        return course_schema.dump(course), 200
    def post(self):
        if  request.is_json:
            parse_json = request.get_json()
            print(not request.is_json)

            nuevo_course = Course(
                    id = parse_json.get('id', None),
                    name = parse_json.get('name', None),
                    timeZone = parse_json.get('timeZone', None),
                    institute = parse_json.get('institute', None),
                    createdAt = datetime.datetime.now(),
                    #createdAt = datetime.datetime.now() - datetime.timedelta(days=35)
                    )
            
            db.session.add(nuevo_course)
            db.session.commit()
            return {
                    "id": "nuevo_usuario",
                    "createdAt": ""
                }, 200
        else:
            print("Else")
            return Response(status=400)
        
