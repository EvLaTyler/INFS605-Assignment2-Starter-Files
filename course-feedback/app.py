# course-feedback/app.py
from flask import Flask, jsonify, request
from models import db, Feedback
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://feedback:password@feedback-db:5434/feedback'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create global db instance
db.init_app(app)

@app.route('/feedback', methods=['GET'])
def get_feedback():
    feedback = Feedback.query.all()
    return jsonify([{
        'id': f.id,
        'student_id': f.student_id,
        'course_id': f.course_id,
        'rating': f.rating,
        'comments': f.comments
    } for f in feedback])

@app.route('/feedback', methods=['POST'])
def add_feedback():
    data = request.get_json()
    new_feedback = Feedback(
        student_id=data['student_id'],
        course_id=data['course_id'],
        rating=data['rating'],
        comments=data.get('comments')
    )
    db.session.add(new_feedback)
    db.session.commit()
    return jsonify({'message': 'Feedback added successfully!'}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5003, debug=True)
