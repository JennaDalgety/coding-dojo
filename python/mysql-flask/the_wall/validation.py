import re


def get_user_by_email(email, mysql):

  query = 'SELECT * FROM users WHERE users.email = :email'
  data = {
    'email': email
  }
  users = mysql.query_db(query, data)

  return users


def create_new_user(flash, form, mysql, bcrypt):

  pw_hash = bcrypt.generate_password_hash(form['password'])

  query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())'

  data = {
      'first_name': form['first_name'],
      'last_name': form['last_name'],
      'email': form['email'],
      'password': pw_hash
    }

  mysql.query_db(query, data)

  flash('New user has been created')

  return

def check_password_hash(bcrypt):
  
  password = 'password'
  pw_hash = bcrypt.generate_password_hash(password)
  test_password_1 = 'thisiswrong'
  bcrypt.check_password_hash(pw_hash, test_password_1)
  test_password_2 = 'password'
  bcrypt.check_password_hash(pw_hash, test_password_2)


def register_check(flash, form, mysql):

  errors = False

  first_name = form['first_name']
  last_name = form['last_name']
  email = form['email']
  password = form['password']
  verify_password = form['verify_password']

  users = get_user_by_email(email, mysql)

  if users:
    flash('Invalid email, please use another one')
    errors = True
  if not first_name or (len(first_name) < 2):
    flash('You must enter a first name')
    errors = True
  if not last_name or (len(last_name) < 2):
    flash('You must enter a last name')
    errors = True
  if not email:
    flash('You must enter an email address')
    errors = True
  if not password:
    flash('You must enter a password')
    errors = True
  if not verify_password:
    flash('You must verify your password')
    errors = True
  if not re.match(r'(^[a-zA-z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', email):
    flash('Please enter a valid email address')
    errors = True
  if not verify_password == password:
    flash('Please enter your password exactly as above')
    errors = True
  if len(password) < 8:
    flash('Your password must be 8 characters or more')
    errors = True

  return errors



def login_query(flash, form, bcrypt, mysql):

  query = 'SELECT * FROM users WHERE users.email = :email'
    
  data = {
    'email': form['login_email'],
  }

  users = mysql.query_db(query, data)

  login_password = form['login_password']

  if not users:
    flash('Your password/email is not recognized')

  return users



