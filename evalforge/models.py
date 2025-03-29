from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Client(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    student_id = db.Column(db.String(50), unique=True, nullable=True)
    last_fie_date = db.Column(db.Date, nullable=False)
    last_iep_date = db.Column(db.Date, nullable=False)
    due_fie_date = db.Column(db.Date, nullable=False)  # 3 years after last_fie_date
    documents = db.relationship('StudentDocument', back_populates='client', lazy=True)


class StudentDocument(db.Model):
    __tablename__ = 'student_document'
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    filename = db.Column(db.String(100), nullable=False)
    file_type = db.Column(db.String(20), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(255))

    client = db.relationship('Client', back_populates='documents')
