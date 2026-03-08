from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, JobStatus, Skill, Project, Education, Profile, init_db
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    profile = Profile.query.first()
    edu_list = Education.query.all()
    jobs = JobStatus.query.all()
    skills = Skill.query.all()
    projects = Project.query.all()
    return render_template('index.html', profile=profile, edu_list=edu_list, jobs=jobs, skills=skills, projects=projects)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('admin'))
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/admin')
@login_required
def admin():
    profile = Profile.query.first()
    edu_list = Education.query.all()
    jobs = JobStatus.query.all()
    skills = Skill.query.all()
    projects = Project.query.all()
    return render_template('admin.html', profile=profile, edu_list=edu_list, jobs=jobs, skills=skills, projects=projects)

@app.route('/admin/job/add', methods=['POST'])
@login_required
def add_job():
    company = request.form.get('company')
    role = request.form.get('role')
    duration = request.form.get('duration')
    description = request.form.get('description')
    is_current = 'is_current' in request.form
    
    new_job = JobStatus(company=company, role=role, duration=duration, description=description, is_current=is_current)
    db.session.add(new_job)
    db.session.commit()
    return redirect(url_for('admin'))

@app.route('/admin/skill/add', methods=['POST'])
@login_required
def add_skill():
    name = request.form.get('name')
    category = request.form.get('category')
    proficiency = request.form.get('proficiency')
    
    new_skill = Skill(name=name, category=category, proficiency=proficiency)
    db.session.add(new_skill)
    db.session.commit()
    return redirect(url_for('admin'))

@app.route('/admin/change-password', methods=['POST'])
@login_required
def change_password():
    new_password = request.form.get('new_password')
    if new_password:
        current_user.password = generate_password_hash(new_password)
        db.session.commit()
        flash('Password updated successfully!')
    return redirect(url_for('admin'))

@app.route('/admin/job/edit/<int:id>', methods=['POST'])
@login_required
def edit_job(id):
    job = JobStatus.query.get(id)
    if job:
        job.company = request.form.get('company')
        job.role = request.form.get('role')
        job.duration = request.form.get('duration')
        job.description = request.form.get('description')
        db.session.commit()
        flash('Job updated successfully!')
    return redirect(url_for('admin'))

@app.route('/admin/profile/edit', methods=['POST'])
@login_required
def edit_profile():
    profile = Profile.query.first()
    if profile:
        profile.name = request.form.get('name')
        profile.headline = request.form.get('headline')
        profile.about_text = request.form.get('about_text')
        profile.email = request.form.get('email')
        profile.phone = request.form.get('phone')
        db.session.commit()
    return redirect(url_for('admin'))

@app.route('/admin/education/add', methods=['POST'])
@login_required
def add_education():
    edu = Education(
        degree=request.form.get('degree'),
        institution=request.form.get('institution'),
        duration=request.form.get('duration')
    )
    db.session.add(edu)
    db.session.commit()
    return redirect(url_for('admin'))

@app.route('/admin/education/edit/<int:id>', methods=['POST'])
@login_required
def edit_education(id):
    edu = Education.query.get(id)
    if edu:
        edu.degree = request.form.get('degree')
        edu.institution = request.form.get('institution')
        edu.duration = request.form.get('duration')
        db.session.commit()
    return redirect(url_for('admin'))

@app.route('/admin/education/delete/<int:id>')
@login_required
def delete_education(id):
    edu = Education.query.get(id)
    if edu:
        db.session.delete(edu)
        db.session.commit()
    return redirect(url_for('admin'))

@app.route('/admin/project/add', methods=['POST'])
@login_required
def add_project():
    new_project = Project(
        title=request.form.get('title'),
        description=request.form.get('description'),
        technologies=request.form.get('technologies')
    )
    db.session.add(new_project)
    db.session.commit()
    return redirect(url_for('admin'))

@app.route('/admin/project/edit/<int:id>', methods=['POST'])
@login_required
def edit_project(id):
    project = Project.query.get(id)
    if project:
        project.title = request.form.get('title')
        project.description = request.form.get('description')
        project.technologies = request.form.get('technologies')
        db.session.commit()
    return redirect(url_for('admin'))

@app.route('/admin/project/delete/<int:id>')
@login_required
def delete_project(id):
    project = Project.query.get(id)
    if project:
        db.session.delete(project)
        db.session.commit()
    return redirect(url_for('admin'))

@app.route('/admin/skill/edit/<int:id>', methods=['POST'])
@login_required
def edit_skill(id):
    skill = Skill.query.get(id)
    if skill:
        skill.name = request.form.get('name')
        skill.category = request.form.get('category')
        db.session.commit()
        flash('Skill updated successfully!')
    return redirect(url_for('admin'))

@app.route('/admin/job/delete/<int:id>')
@login_required
def delete_job(id):
    job = JobStatus.query.get(id)
    if job:
        db.session.delete(job)
        db.session.commit()
    return redirect(url_for('admin'))

@app.route('/admin/skill/delete/<int:id>')
@login_required
def delete_skill(id):
    skill = Skill.query.get(id)
    if skill:
        db.session.delete(skill)
        db.session.commit()
    return redirect(url_for('admin'))

if __name__ == '__main__':
    # Create an admin user if not exists
    with app.app_context():
        if not User.query.filter_by(username='Aashish').first():
            admin_user = User(username='Aashish', password=generate_password_hash('78@Aashish'))
            db.session.add(admin_user)
            db.session.commit()
    app.run(debug=True)
