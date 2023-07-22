from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


db = SQLAlchemy()


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    timeZone = db.Column(db.String(50))
    institute = db.Column(db.String(50))
    createdAt = db.Column(db.DateTime)
    #deletedAt = db.Column(db.DateTime)


class CourseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Course
        include_relationships = True
        load_instance = True

