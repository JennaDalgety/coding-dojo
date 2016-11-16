from flask import Flask, render_template, redirect, request
from mysqlconnection import MySQLConnector
from methods import add_notes, display_notes

app = Flask(__name__)
mysql = MySQLConnector(app, 'notes')



@app.route('/')
def index():

  query = 'SELECT description FROM posts'
  posts = mysql.query_db(query)

  return render_template('index.html', posts=posts)



# @app.route('/posts/create/index_json', methods=['POST'])
# def index_json():

#   print 'we are on the index_json posts create route!'

#   index_json(mysql, jsonify)



@app.route('/posts/create', methods=['POST'])
def create():

  print 'we are on the creating posts route!'

  add_notes(request.form, mysql)
  posts = display_notes(mysql)
  
  return render_template('index.html', posts=posts)



app.run(debug=True)