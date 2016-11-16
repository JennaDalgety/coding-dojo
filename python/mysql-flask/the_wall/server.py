from flask import Flask, render_template, redirect, request, session, flash
from validation import register_check, create_new_user, login_query, get_user_by_email
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
app = Flask(__name__)

app.secret_key = "o87564eysdfjgkuyf85r6tuykuilhgftrueyxsdhfgjhyg"

mysql = MySQLConnector(app, 'the_wall')
bcrypt = Bcrypt(app)


@app.route('/')
def index():

  if 'logged_in_user' in session:
    return redirect('/wall')

  else:
    return render_template('index.html')



@app.route('/register', methods=['POST'])
def register():

  errors = register_check(flash, request.form, mysql)

  if errors:
    return redirect('/')

  else:
    create_new_user(flash, request.form, mysql, bcrypt)

    return redirect('/')



@app.route('/login', methods=['POST'])
def login():

  users = get_user_by_email(request.form['login_email'], mysql)

  if users:
    if bcrypt.check_password_hash(users[0]['password'], request.form['login_password']):
      session['logged_in_user'] = users[0]['id']
      return redirect('/wall')
    else:
      flash('Incorrect Username/Password Combo')
      return redirect('/')

  else:
      flash('Incorrect Username/Password Combo')
      return redirect('/')



@app.route('/wall')
def wall():

  if not 'logged_in_user' in session:
    return redirect('/')
  
  else:
    # post query
    query = 'SELECT users.first_name, users.last_name, posts.content, posts.created_at, posts.id FROM posts JOIN users ON users.id = posts.user_id ORDER BY posts.created_at DESC LIMIT 20'
    posts = mysql.query_db(query)
    

    for post in posts:
      # comment query
      query = 'SELECT users.first_name, users.last_name, comments.content, comments.created_at, comments.id FROM comments JOIN users ON users.id = comments.user_id WHERE comments.post_id = :id'
      
      data = {
        'id': post['id']
      }

      post['comments'] = mysql.query_db(query, data)

    return render_template('wall.html', posts=posts)



@app.route('/post', methods=['POST'])
def post():

  if 'logged_in_user' in session:
    post = request.form['post']

    query = 'INSERT INTO posts (content, user_id, created_at, updated_at) VALUES (:content, :user_id, NOW(), NOW())'

    message = {
      'content': request.form['post'],
      'user_id': session['logged_in_user']
    }

    mysql.query_db(query, message)


  return redirect('/wall')



@app.route('/comment', methods=['POST'])
def comment():

  if 'logged_in_user' in session:
    comment = request.form['comment']

    query = 'INSERT INTO comments (content, user_id, post_id, created_at, updated_at) VALUES (:content, :user_id, :post_id, NOW(), NOW())'

    comment = {
      'content': request.form['comment'],
      'user_id': session['logged_in_user'],
      'post_id': request.form['post_id']
    }

    print comment

    comments = mysql.query_db(query, comment)

  return redirect('/wall')



@app.route('/logout')
def logout():

  if 'logged_in_user' in session:
    session.pop('logged_in_user')

  return redirect('/')



app.run(debug=True)