from flask import Flask, render_template, request, redirect, session
from random import randrange
app = Flask(__name__)
app.secret_key = 'q8374tgbftuyvg4wih8biyt8tkh'


@app.route('/', methods=['POST', 'GET'])

@app.route('/guess', methods=['POST', 'GET'])

def index():

  if 'answer' not in session:
    
    session['answer'] = randrange(1, 101)

  session['result'] = None

  session['correct'] = True

  if request.method == 'POST':
    guess = int(request.form['guess'])
    if guess != session['answer']:
      session['correct'] = False
      if guess > session['answer']:
        session['result'] = 'Too high!'
      elif guess < session['answer']:
        session['result'] = 'Too low!'
    else:
      session['result'] = 0

  return render_template('index.html')

@app.route('/reset', methods=['POST'])

def reset():

 session['answer'] = randrange(1, 101)

 return redirect('/') 

app.run(debug=True)