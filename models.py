from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import os

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class JobStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    is_current = db.Column(db.Boolean, default=False)
    order = db.Column(db.Integer, default=0)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False) # e.g., AI, Web, Tools
    proficiency = db.Column(db.Integer, default=80) # 0-100

class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String(100), nullable=False)
    institution = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(50), nullable=False)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    headline = db.Column(db.String(100))
    about_text = db.Column(db.Text)
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    technologies = db.Column(db.String(200))
    link = db.Column(db.String(200))
    image_url = db.Column(db.String(200))

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
        
        # Initial data if empty
        if not Skill.query.first():
            skills = [
                Skill(name="Python", category="", proficiency=95),
                Skill(name="C/C++", category="", proficiency=85),
                Skill(name="WordPress (CMS)", category="", proficiency=90),
                Skill(name="MySQL", category="Database", proficiency=80),
                Skill(name="NumPy/Pandas", category="Tools", proficiency=85),
                Skill(name="Google Analytics", category="Tools", proficiency=80),
                Skill(name="CVAT", category="Tools", proficiency=75),
            ]
            for s in skills: db.session.add(s)
            
            jobs = [
                JobStatus(company="Bol7 Technologies Pvt. Ltd.", role="Python Developer", duration="2023 - Present", description="Currently working as a Python Developer, contributing to backend development, automation workflows, AI Chatbots, and scalable software solutions.", is_current=True),
                JobStatus(company="Prowiz Infotech LLP", role="AI Engineer", duration="Past", description="Worked as an AI Engineer, contributing to the development and optimization of machine learning models, automation workflows, AI Chatbots, and AI-driven business solutions.", is_current=False)
            ]
            for j in jobs: db.session.add(j)
            
            projects = [
                Project(title="Railway Reservation System", description="Developed a Python and SQL-based system for managing train bookings, passenger records, and secure ticket reservations.", technologies="Python, SQL"),
                Project(title="Face Recognition Attendance System", description="Developed a Python-based system for attendance using face recognition and database integration.", technologies="Python, Django"),
                Project(title="Portfolio Website", description="Designed and developed a responsive personal portfolio website using WordPress.", technologies="WordPress, CMS")
            ]
            for p in projects: db.session.add(p)
            db.session.commit()

        if not Profile.query.first():
            profile = Profile(
                name="Aashish Sharma",
                headline="Python Developer & AI Engineer",
                about_text="I am a passionate Python Developer and AI Engineer at Bol7 Technologies, specializing in backend systems, automation workflows, and AI chatbots.",
                email="aashish783078@gmail.com",
                phone="+91 7830785069"
            )
            db.session.add(profile)
            db.session.commit()
        
        if not Education.query.first():
            edu1 = Education(degree="Postgraduation in MCA", institution="Graphic Era Hill University (GEHU)", duration="2023 - 2025")
            edu2 = Education(degree="Graduation in BCA", institution="Sri Dev Suman University (SDIMT)", duration="2020 - 2023")
            db.session.add(edu1)
            db.session.add(edu2)
            db.session.commit()
