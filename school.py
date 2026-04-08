from flask_sqlalchemy import SQLAlchemy
from forms import AdmissionForm
from flask import Flask,render_template
import os


web=Flask(__name__)
picfolder = os.path.join('static')
web.config['UPLOAD_FOLDER']= picfolder
web.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
web.config['SECRET_KEY'] = 'mysecretkey'

db = SQLAlchemy(web)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    student_class = db.Column(db.String(50))
    stream = db.Column(db.String(50))
    city = db.Column(db.String(50))
    phone_number = db.Column(db.String(15))

with web.app_context():
    db.create_all()

@web.route('/')

def homepage():
    pic = os.path.join(web.config['UPLOAD_FOLDER'],'school.jpg')
    return render_template("home.html",user_image=pic)

@web.route('/form', methods=['GET', 'POST'])
def form():
    form = AdmissionForm()

    if form.validate_on_submit():
        print("Valid Form")

        student = Student(
            name=form.name.data,
            age=form.age.data,
            student_class=form.student_class.data,
            stream=form.stream.data,
            city=form.city.data,
            phone_number=form.phone_number.data
        )

        db.session.add(student)
        db.session.commit()

        return render_template(
            'success.html',
            name=form.name.data,
            age=form.age.data,
            student_class=form.student_class.data,
            stream=form.stream.data,
            city=form.city.data,
            phone_number=form.phone_number.data,
            image='student-at-school-playground-free-vector.jpg'
        )

    return render_template("register.html", form=form)

if __name__=='__main__':
    web.run(debug=True)
