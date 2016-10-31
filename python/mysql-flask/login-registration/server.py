from flask import Flask, render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt
from validations import registration_validation, register_user, login_user
from mysqlconnection import MySQLConnector

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'login-registration')
app.secret_key = "thisisthesecretkey12345"

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():

    errors = registration_validation(request.form, flash, mysql)

    if errors:
        return redirect('/')
    else:
        register_user(mysql, request.form, flash, bcrypt)
        return redirect('/')


@app.route('/login', methods=['POST'])
def login():

  if login_user(request.form, mysql, flash, bcrypt, session, redirect):
    flash('user logged in')

    return redirect('/')

  else:
    flash('incorrect user/password combo')
    return redirect('/')






app.run(debug=True)
