from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    summary = db.Column(db.Text)
    education = db.Column(db.Text)
    experience = db.Column(db.Text)
    skills = db.Column(db.Text)

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/resume')
def resume():
    return redirect('/resume/templates')

@app.route('/resume/templates')
def resume_templates_view():
    return render_template('resume_templates.html')
 
@app.route('/generate_resume')
def generate_resume():
    return render_template('resume_templates.html')  # this file should exist

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Process form (optional for now)
        return redirect('generate_resume') # Or anywhere you want
    return render_template('register.html')

@app.route('/resume/form', methods=['GET', 'POST'])
def resume_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        summary = request.form.get('summary')
        education = request.form.get('education')
        experience = request.form.get('experience')
        skills = request.form.get('skills')

        resume = Resume(
            name=name,
            email=email,
            phone=phone,
            summary=summary,
            education=education,
            experience=experience,
            skills=skills
        )
        db.session.add(resume)
        db.session.commit()

        return render_template('view_resume.html', resume=resume)

    return render_template('resume_form.html')



@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
