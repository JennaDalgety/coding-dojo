import re

#validates all registration form fields
def registration_validation(form, flash, mysql):

    error = False
    first_name = form['first_name']
    last_name = form['last_name']
    email = form['email']
    password= form['password']
    confirm_password = form['confirm_password']


    users = check_for_existing_user(email, flash, mysql)

    if len(first_name) < 2:
        flash("first name cannot be shorter than 2 letters", "name_error")
        error = True
    if len(last_name) < 2:
        flash("last name cannot be shorter than 2 letters", "name_error")
        error = True
    if not re.match( r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        flash("please enter a valid email address", "email_error")
        error = True
    if len(password) < 8:
        flash("password must be at least 8 characters long", "password_error")
        error = True
    if not password == confirm_password:
        flash("passwords must match", "password_error")
    if users:
        flash("this user already exists. please use another email")
        error = True

    return error

#inserts new user into database through registration form
def register_user(mysql, form, flash,bcrypt):

    pw_hash = bcrypt.generate_password_hash(form['password'])

    query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES(:first_name, :last_name, :email, :password, NOW(), NOW())'

    data = {
        'first_name'    : form['first_name'],
        'last_name'     : form['last_name'],
        'email'         : form['email'],
        'password'      : pw_hash
    }

    mysql.query_db(query, data)
    flash("new user created", "status_message")



#checks to see if user is already in database
def check_for_existing_user(email, flash, mysql):

    query = "SELECT * from users WHERE users.email = :email"

    data = {
        'email': email
    }

    existing_user = mysql.query_db(query, data)
    return existing_user



#checks email and password against database and logs them in if all is correct
def login_user(form, mysql, flash, bcrypt, session, redirect):

    email = form['email']
    password = form['password']

    user_exists = check_for_existing_user(email, flash, mysql)

    if user_exists:
        if bcrypt.check_password_hash(user_exists[0]['password'], password):
            session['logged_in_user'] = user_exists[0]['id']
            return redirect('/')




