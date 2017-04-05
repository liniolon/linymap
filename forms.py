from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length 

class SignupForm(Form):
	first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
	last_name = StringField('Last name', validators=[DataRequired("Please enter your last name.")])
	email  = StringField('Email address', validators=[DataRequired("Please enter your email."), Email('Enter a correct email address')])
	password = PasswordField('Password', validators=[DataRequired("Please enter your password."), Length(min=6, message="Password must be 6 or more")])
	submit = SubmitField('Sign up')

class LoginForm(Form):

	email = StringField('Email', validators=[DataRequired("Email field must not empty"), Email("Enter a correct email address")])
	password  = PasswordField('Password', validators=[DataRequired("Enter your password"), Length(min=6, message="Should be more 6 charachter")])

	submit = SubmitField("Sign in")	


class AddressForm(Form):
	address = StringField('Address', validators=[DataRequired("Enter an address")])
	submit = SubmitField('Explore')