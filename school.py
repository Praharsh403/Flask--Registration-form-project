from flask import Flask,render_template,request
import os

web=Flask(__name__)
picfolder = os.path.join('static')
web.config['UPLOAD_FOLDER']= picfolder

@web.route('/')

def homepage():
    pic = os.path.join(web.config['UPLOAD_FOLDER'],'school.jpg')
    return render_template("home.html",user_image=pic)

@web.route('/form')

def form():
    return render_template("register.html")

@web.route('/confirmation',methods=['POST','GET'])

def register():
    if request.method=='POST':
        n=request.form.get('name')
        a=request.form.get('age')
        student_class=request.form.get('student_class')
        s=request.form.get('stream')
        c=request.form.get('city')
        ph=request.form.get('phone_number')
        return render_template('success.html',name=n,age=a,student_class=student_class,stream=s,city=c,phone_number=ph)

if __name__=='__main__':
    web.run(debug=True)
