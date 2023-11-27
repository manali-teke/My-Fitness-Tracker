from datetime import date
from re import sub
from flask import app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.fields.core import DateField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from apps import App,Mongo
import re


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[
            DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        mongo = Mongo().mongoClient
         
        temp = mongo.user.find_one({'email': email.data}, {'email', 'pwd'})
        if temp:
            raise ValidationError('Email already exists!')
    def validate_password(self, password):
        password_value = password.data

        if len(password_value) < 8 or not re.search(r'[A-Z]', password_value) or not re.search(r'[a-z]', password_value) or not re.search(r'\d', password_value) or not re.search(r'[!@#$%^&*]', password_value):
            password.data = None
            raise ValidationError('Password must be least 8 characters long and must contain at least 1 uppercase, lowercase, digit and special character.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class ChangePasswordForm(FlaskForm):
    oldpassword = PasswordField('Old Password', validators=[DataRequired()])
    newpassword = PasswordField('New Password', validators=[DataRequired()])
    confirmpassword = StringField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Change_Password')


class CalorieForm(FlaskForm):
    app = App()      
    mongo = Mongo().mongoClient
    cursor = mongo.food.find()
    get_docs = []
    for record in cursor:
        get_docs.append(record)

    result = []
    temp = ""
    for i in get_docs:
        temp = i['Food'] + ' (' + i['Calories'] + ')'
        result.append((temp, temp))

    food = SelectField(
        'Select Food', choices=result)

    burnout = StringField('Burn Out', validators=[DataRequired()])
    submit = SubmitField('Save')


class UserProfileForm(FlaskForm):
    weight = StringField(
        'Weight', validators=[
            DataRequired(), Length(
                min=2, max=20)])
    height = StringField(
        'Height', validators=[
            DataRequired(), Length(
                min=2, max=20)])
    goal = StringField(
        'Goal', validators=[
            DataRequired(), Length(
                min=2, max=20)])
    target_weight = StringField(
        'Target Weight', validators=[
            DataRequired(), Length(
                min=2, max=20)])
    submit = SubmitField('Save Profile')


class HistoryForm(FlaskForm):
    app = App()
    date = DateField()
    submit = SubmitField('Fetch')


class EnrollForm(FlaskForm):
    app = App()
    submit = SubmitField('Enroll')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[
            DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset')

class DietPlanForm(FlaskForm):
    day = IntegerField('Day',
                           validators=[DataRequired()])
    app = App()      
    mongo = Mongo().mongoClient
    cursor = mongo.food.find()
    get_docs = []
    for record in cursor:
        get_docs.append(record)

    food_result = []
    temp = ""
    for i in get_docs:
        temp = i['Food'] + ' (' + i['Calories'] + ')'
        food_result.append((temp, temp))
    food = SelectField(
        'Select Food', choices=food_result)
    
    

    mealtypes = ["Breakfast", "Lunch", "Snacks", "Dinner", "Bedtime"]
    mealtype = SelectField(
        'Select Meal Type', choices=mealtypes)
    submit = SubmitField('Save Diet Plan')

class AdminForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    roles = [ "Dietician", "Trainer" ]
    role = SelectField(
        'Role', choices=roles)
    submit = SubmitField('Save')

class DieticianForm(FlaskForm):
    submit = SubmitField('Save')

class TrainerForm(FlaskForm):
    submit = SubmitField('Save')