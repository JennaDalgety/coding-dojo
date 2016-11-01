from flask import Flask, flash, redirect, render_template, request
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)

app.secret_key = "9827gfbyn398y7fbn438yubn8u4ynimq3jcekmew!2qy7812y3h8eu"

mysql = MySQLConnector(app, 'friends')

@app.route('/')
def index():

  return render_template('index.html')



@app.route('/friends', methods=['POST'])
def create():

  first_name = request.form['first_name']
  last_name = request.form['last_name']
  email = request.form['email']

  errors = False

  if len(first_name) < 2:
    flash('please enter a valid first name')
    error = True
  if len(last_name) < 2:
    flash('please enter a valid last name')
    error = True
  if not re.match( r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
    flash('please enter a valid email address')
    error = True

  if not errors:
    query = 'INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())'

    data = {
      'first_name': first_name,
      'last_name': last_name,
      'email': email
    }

    friends = mysql.query_db(query, data)
    return friends

    return render_template('index.html', friends=friends)

  else:
    return redirect('/')



@app.route('/friends/<id>/edit')
def edit(id):

  render_template('edit.html')



@app.route('/friends/<id>', methods=['POST'])
def update(id):

  query = 'SELECT * FROM users where users.id = :id'

  data = {
    'first_name': first_name,
    'last_name': last_name,
    'email': email
  }

  friends = mysql.query_db(query, data)
  return friends

    




# @app.route('friends/<id>/delete', methods=['POST'])
# def destroy(id):





app.run(debug=True)