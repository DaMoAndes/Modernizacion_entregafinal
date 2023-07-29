from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


db = SQLAlchemy()


class CourseModel(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(50))
    timeZone = db.Column(db.String(50))
    institute = db.Column(db.String(50))
    createdAt = db.Column(db.DateTime)
    deletedAt = db.Column(db.DateTime)


class CourseModelSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CourseModel
        include_relationships = True
        load_instance = True

