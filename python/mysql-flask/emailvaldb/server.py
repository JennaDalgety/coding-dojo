from flask import Flask, render_template, request, flash, redirect, session
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "thisisthesupersecretkey"

mysql = MySQLConnector(app, "emaildb")


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/process', methods=['POST'])
def validations():
    error = False
    email = request.form['email']
    session['email'] = email

    if not re.match( r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', email):
        flash('please enter a valid email address')
        error = True

    query = 'SELECT * FROM users WHERE users.email = :email'
    data = {
        'email': email
    }
    users = mysql.query_db(query, data)

    if users:
        flash('this email already exists')
        error = True 

    if not error:
        query = 'INSERT INTO users (email, created_at, updated_at) VALUES (:email, NOW(), NOW())'
        # query is a variable, can name it anything

        insert_emails = {
            'email': request.form['email']
        }
        mysql.query_db(query, insert_emails)
        return redirect('/success')
    else:
        return redirect('/')



@app.route('/success')
def success():


    email_display_query = 'SELECT * FROM users'
    emails = mysql.query_db(email_display_query)


    return render_template('success.html', emails = emails)


@app.route('/edit/<id>', methods=['POST', 'GET'])
def edit(id):

    if request.method == 'GET':
        query = 'SELECT * FROM users WHERE users.id = :id'
        data = {
            'id': id
        }
        email = mysql.query_db(query, data)[0]
        return render_template('email_update.html', email = email)
    else:
        query = 'UPDATE users SET users.email = :updated_email WHERE users.id = :id'
        data = {
            'id': id,
            'updated_email': request.form['email'] # key from text box on the input
        }
        mysql.query_db(query, data)
        session['email'] = request.form['email']
        return redirect('/success')

app.run(debug=True)