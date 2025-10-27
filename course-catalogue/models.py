# course-catalogue/models.py
# This file is part of Flask structure which is based on Model-View-Controller (MVC) Architecture
# Specifically, this file defines the database schema of the course-catalogue microservice and how this maps to Python objects.

from app import db

class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    credits = db.Column(db.Integer, nullable=False)
    instructor = db.Column(db.String(100), nullable=True)

    def as_dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "title": self.title,
            "description": self.description,
            "credits": self.credits,
            "instructor": self.instructor,
        }
