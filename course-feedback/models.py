# course-feedback/models.py
# This file is part of Flask structure which is based on Model-View-Controller (MVC)
# Specifically, this file defines the database schema of the course-feedback microservice and how this maps to Python objects.

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, nullable=False)
    course_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.String(255))

