from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators, PasswordField, IntegerField
from wtforms.fields import EmailField, DateField
# from wtforms import validators
# from wtforms.fields.html5 import EmailField
import re
def check_phone_number(form, field):
    if not re.match(r'^[89][0-9]{7}$', str(field.data)):
        raise validators.ValidationError('Invalid phone number,it must start with either 8 or 9 and be 8 digit long')

class CreateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    password = StringField(label='Password', validators=[
        validators.Length(min=6, max=10),
        validators.EqualTo('confirm_password', message='Passwords must match')
    ])
    confirm_password = PasswordField('Confirm Password', [validators.Length(min=6, max=10), validators.DataRequired()])
    address1 = StringField('Address Line 1', [validators.length(max=100), validators.DataRequired()])
    address2 = StringField('Address Line 2(optional)', [validators.length(max=100)])
    membership = SelectField('Role', choices=[('E', 'Employee'), ('M', 'Manager'), ('A', 'Admin')], default='F')
    phone_number = IntegerField('Phone Number', [validators.InputRequired(), check_phone_number])
    status = SelectField('Status', choices=[('A','Active'),('N','Non-Active')],default='A')


class CreateCustomerForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    phone_number = IntegerField('Phone Number', [validators.InputRequired(), check_phone_number])
    date_joined = DateField('Date Joined', format='%Y-%m-%d')
    password = StringField(label='Password', validators=[
        validators.Length(min=6, max=10),
        validators.EqualTo('confirm_password', message='Passwords must match')
    ])
    confirm_password = PasswordField('Confirm Password', [validators.Length(min=6, max=10), validators.DataRequired()])
    address1 = StringField('Mailing Address', [validators.length(max=100), validators.DataRequired()])
    address2 = SelectField('Buyer or Seller', choices=[('B', 'Buyer'), ('S', 'Seller')], default='F')
    status = SelectField('Status', choices=[('A','Active'),('N','Non-Active')],default='A')

class LoginForm(Form):
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    password = StringField(label='Password', validators=[
        validators.Length(min=6, max=10),
        validators.EqualTo('confirm_password', message='Passwords must match')
    ])
    

