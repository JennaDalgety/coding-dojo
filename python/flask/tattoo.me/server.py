from flask import Flask, render_template, redirect, flash, request
import re
from db import readUser
app = Flask(__name__)
app.secret_key = 'iurgn398yty89ouynw9ubiytniri?&#%^*(reurneeruer'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
  email = request.form['email']
  password = request.form['password']

  errors = []

  if len(email) < 1:
    errors.append('Please enter an email')
  if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9_.]+$)", email):
    errors.append('Must be a valid email')

  if errors:
    return render_template('index.html')

@app.route('/register', methods=['GET'])
def register():

  return render_template('registration.html')


@app.route('/create_user', methods=['POST'])
def create_user():

  error = False
  firstName = request.form['first_name']
  lastName = request.form['last_name']
  email = request.form['email']
  password = request.form['password']
  confirmPassword = request.form['confirm_password']

  user_info = {
    'email': email,
    'first_name': firstName,
    'last_name': lastName,
    'password': password,
    'confirm_password': confirmPassword
  }
  
  if len(email) < 1:
    flash('Must enter an email')
    error = True
  elif not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9_.]+$)", email):
    flash('Must enter a valid email')
    error = True

  if len(firstName) < 1:
    flash('Must enter a first name')
    error = True
  elif re.search(r"[0-9]", firstName):
    flash('First name cannot contain numbers')
    error = True
  
  if len(lastName) < 1:
    flash('Must enter a last name')
    error = True
  elif re.search(r"[0-9]", lastName):
    flash('Last name cannot contain numbers')
    error = True

  if len(password) == 0:
    flash('Must enter a password')
    error = True
  elif len(password) < 8:
    flash('Password must have at least 8 characters')
    error = True

  if confirmPassword != password:
    flash('Must retype password')
    error = True

  if error == False:
    return redirect('/')

  return redirect('/register') 

  # if method.request == 'GET':





app.run(debug=True)