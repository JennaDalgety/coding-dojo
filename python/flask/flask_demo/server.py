from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'I am a secret Key!'

@app.route('/')


def index():
  if session.get('name'):
    name = session['name']
  else:
    name = ''
  return render_template('index.html', name = name)

@app.route('/process', methods = ['POST'])
def process():
  
  session['name'] = request.form['first_name']

  return redirect('/')

app.run(debug = True)