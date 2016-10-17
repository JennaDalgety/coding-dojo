from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = 'I am a secret key!'

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/results', methods=['POST'])
def create_user():
  print "Got Post Info"
  
  error = False 
  name = request.form['Your Name']
  location = request.form['Dojo Location']
  language = request.form['Favorite Language']
  comment = request.form['Comment']
  
  user_info = {
    'Your Name': name,
    'Dojo Location': location, 
    'Language': language, 
    'Comment': comment
  }

  if len(name) < 1:
    flash('Name cannot be that small!')
    error = True

  if len(comment) > 120:
    flash('Comment cannot be greater than 120 characters!')
    error = True
  
  if error == False:
    return render_template("results.html", user_info = user_info)

  return redirect('/') 


app.run(debug=True)