#course-catalogue/app.py

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://course:password@course-db:5432/courses')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import models after db initialized
from models import Course

with app.app_context():
    db.create_all()

@app.route("/health")
def health():
    return {"status": "ok", "service": "course-catalogue"}

@app.route("/courses", methods=["GET"])
def list_courses():
    courses = Course.query.all()
    return jsonify([c.as_dict() for c in courses])

@app.route("/courses", methods=["POST"])
def add_course():
    data = request.get_json()
    course = Course(
        code=data["code"],
        title=data["title"],
        description=data.get("description", ""),
        credits=data.get("credits", 15),
        instructor=data.get("instructor", "Unknown")
    )
    db.session.add(course)
    db.session.commit()
    return jsonify(course.as_dict()), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
