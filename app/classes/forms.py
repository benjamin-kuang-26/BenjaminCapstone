# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, Email, DataRequired, NumberRange
from wtforms.fields.html5 import URLField, DateField, IntegerRangeField, EmailField
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField, RadioField
from wtforms_components import TimeField

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    image = FileField("Image") 
    submit = SubmitField('Post')
    role = SelectField('Role',choices=[("Teacher","Teacher"),("Student","Student")])



class ConsentForm(FlaskForm):
    adult_fname = StringField('First Name',validators=[DataRequired()])
    adult_lname = StringField('Last Name',validators=[DataRequired()])
    adult_email = EmailField('Email',validators=[Email()])
    consent = RadioField('Do you want your parents or teachers to see your sleep data/graph', choices=[(True,"True"),(False,"False")])
    submit = SubmitField('Submit')

class SleepForm(FlaskForm):
    rating = SelectField("How would you rate your sleep: 5 is great, 1 is poor", choices=[(None,'---'),(1,1),(2,2),(3,3),(4,4),(5,5)], validators=[DataRequired()])
    starttime = TimeField("Start Time")   
    endtime = TimeField("End Time")   
    feel = SelectField("How did you feel when you woke up: 5 is great, 1 is poor", choices=[(None,'---'),(1,1),(2,2),(3,3),(4,4),(5,5)], validators=[DataRequired()])
    sleep_date = DateField("What date did you go to sleep")
    wake_date = DateField("What date did you wake up")
    minstosleep = IntegerField("How many minutes did it take you to fall asleep?", validators=[NumberRange(min=0,max=180, message="Enter a number between 0 and 180.")])
    submit = SubmitField("Submit")

class BlogForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    content = TextAreaField('Blog', validators=[DataRequired()])
    tag = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Post!')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')

class ClinicForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    streetAddress = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zipcode = StringField('Zipcode',validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class LimitForm(FlaskForm):
    question1 = SelectField('What is the fundamental concept about limits?', choices=[(None,'---'),(1,"Graphs"),(2,"Algebra"),(3,"Logarithms"),(4,"Infinity"),(5,"Trigonometry")], validators=[DataRequired()])
    question2 = SelectField('How many number are between 0.1 and 0.2?', choices=[(None,'---'),(1,"There are none"),(2,"1"),(3,"10"),(4,"Infinity"),(5,"How is that possible?")], validators=[DataRequired()])
    question3 = SelectField('How did we model the concept of limits?', choices=[(None,'---'),(1,"Money"),(2,"Pizza"),(3,"Screen Time"),(4,"Running Distance"),(5,"Hair length")], validators=[DataRequired()])
    question4 = SelectField('What is 1 over infinity supposed to be?', choices=[(None,'---'),(1,"Too many things!"),(2,"Nothing"),(3,"Close to 0"),(4,"My mental capacity"),(5,"My bank account")], validators=[DataRequired()])
    question5 = SelectField('IS INFINITY A NUMBER? IF SO WHAT NUMBER?', choices=[(None,'---'),(1,"A million"),(2,"1 Googol"),(3,"It is NOT a number"),(4,"0")], validators=[DataRequired()])
    submit = SubmitField('Submit Quiz')

class DerivativeForm(FlaskForm):
    question1 = SelectField('What is a derivative used to calculate?', choices=[(None,'---'),(1,"Area"),(2,"Slope"),(3,"Money"),(4,"Shapes"),(5,"How much food you have left")], validators=[DataRequired()])
    question2 = SelectField('What did our example use to demonstrate basic slope?', choices=[(None,'---'),(1,"Happiness"),(2,"Apples"),(3,"Time"),(4,"Screen time"),(5,"Coffee")], validators=[DataRequired()])
    question3 = SelectField('What is the smallest interval of a graph that is best to estimate slope?', choices=[(None,'---'),(1,"1/2"),(2,"1/4"),(3,"1/8"),(4,"1/220"),(5,"1/infinity")], validators=[DataRequired()])
    question4 = SelectField('Do you remember the slope formula?', choices=[(None,'---'),(1,"(y2-y1)/(x2-x1)"),(2,"y=mx+b"),(3,"y-y1=m(x-x1)"),(4,"Ax+By=C"),(5,"I have no idea...")], validators=[DataRequired()])
    question5 = SelectField('What is the difference between a derivative and slope?', choices=[(None,'---'),(1,"Average change"),(2,"Final - initial"),(3,"Instantaneous change"),(4,"One is harder to calculate")], validators=[DataRequired()])
    submit = SubmitField('Submit Quiz')

class IntegralForm(FlaskForm):
    question1 = SelectField('What is an integral used to calculate?', choices=[(None,'---'),(1,"Slope"),(2,"Area"),(3,"Money"),(4,"Shapes"),], validators=[DataRequired()])
    question2 = SelectField('How did we calculate area according to our example?', choices=[(None,'---'),(1,"Equations"),(2,"Coins"),(3,"Money"),(4,"Shapes"),], validators=[DataRequired()])
    question3 = SelectField('How many rows and columns give us the best estimate for an area?', choices=[(None,'---'),(1,"5"),(2,"15"),(3,"100"),(4,"Infinite"),], validators=[DataRequired()])
    question4 = SelectField('What shape did we use to demonstarte this idea of estimating area?', choices=[(None,'---'),(1,"Circle"),(2,"Triangle"),(3,"Curve"),(4,""),], validators=[DataRequired()])
    question5 = SelectField('What does this idea of calculating area help us calculate more of?', choices=[(None,'---'),(1,"One's screen time"),(2,"A growth cycle"),(3,"Monopoly boards"),(4,"Complex areas"),], validators=[DataRequired()])
    submit = SubmitField('Submit Quiz')