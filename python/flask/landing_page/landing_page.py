from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'I am a secret key!'


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/ninjas')
def displayNinjas():
  return render_template('ninjas.html')

@app.route('/dojos/new', methods = ['POST', 'GET'])
def process():
  if request.method == 'POST':
    session['name'] = request.form['firstName']
    return render_template('dojos.html', name = session['name'])
  else:
    return render_template('dojos.html')

app.run(debug = True)