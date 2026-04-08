from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField
from wtforms.validators import DataRequired,Length,Regexp

class AdmissionForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    age = StringField("Age", validators=[
    DataRequired(),
    Regexp('^[0-9]+$', message="Enter numbers only")
])
    student_class = StringField("Class", validators=[DataRequired()])
    stream = SelectField(
    "Stream",
    choices=[
        ("Science", "Science"),
        ("Commerce", "Commerce"),
        ("KG", "KG"),
        ("LKG", "LKG"),
        ("Primary", "Primary"),
        ("Junior", "Junior")
    ],
    validators=[DataRequired()]
)
    city = StringField("City", validators=[DataRequired()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])