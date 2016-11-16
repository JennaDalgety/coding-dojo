from flask import Flask, render_template, jsonify, request
from mysqlconnection import MySQLConnector
from models import Posts

app = Flask(__name__)
mysql = MySQLConnector(app, 'real_notes')
post = Posts(mysql, jsonify)


@app.route('/')
def index():

  return render_template('index.html')



@app.route('/posts/create', methods=['POST'])
def create():

  
  # this function should take the submitted form info and submits it to the database
  # 1. type text into form
  #    see form on template
  # 2. submit text from form to /posts/create route
  #    see line 16 on template
  # 3. extract data from form
  content = request.form['post_content']
  print content 
  # 4. run query to insert that data into database
  #    see line 15 of models
  post.add_post_to_db(content)
  # 5. run query to select the post that was just created
  #    see line 8 of models
  post.
  # 6. return the post that was just created
  return render_template('index.html')



app.run(debug=True)