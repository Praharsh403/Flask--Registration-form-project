# Flask--Registration-form-project
Flask- Registration form project
In this project, I created a basic school admission form where users can enter their details like name, age, class, stream, city, and phone number. After submitting the form, the entered data is displayed on a confirmation page.

Project Structure:

school.py → Main Flask application file
templates → Contains HTML files (home, form, success page)
static → Contains images (used on homepage)

What I Learned:
While working on this project, I learned how to:
1)Create forms thst are user-friendly.
2)how does Flask,render_template,and request works in python and the requirments needed for them to successfully work.
3) how to apply images to forms
4) how does the 'Get' and "Post' methods operate
5)Form handling and validation along with database integration.
6) where to looks for styling or improving the background of website through various styling.(eg: getbootstap.com)

RUN the Project:
1) To run the project, just hit run and click on the url generated to visit the website.

Learning:
This project helped me understand the basics of web development using Flask and how backend and frontend are connected.And how applications so simple as Flask are user rich and provide friendly experience not only for coder but as well the user like pininterest as stated in the lecture as well.

Post Feedback:
For the Flask project, I built a simple school admission form. Initially, I was using basic form handling, but based on feedback, I improved the project by implementing Flask-WTF forms with validation. I created a separate forms.py file and added validators to ensure correct user input.

I also integrated SQLAlchemy to store form data in a database instead of just displaying it. I created a Student model and used it to save user details like name, age, class, stream, city, and phone number.

I faced an issue where the form was not submitting, which I later understood was due to validation errors. I fixed it by simplifying validators and displaying error messages on the form. I also updated the success page to correctly display all submitted data.

Additionally, I made small improvements like adding a dropdown for stream selection and including an image on the success page.

Overall, this task helped me understand form handling, validation, and database integration in a practical way.
