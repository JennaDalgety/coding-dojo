from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'iaugfbaerkjcnbwi479uronfqriugfnbwuliwe'

playerRoster = {}

@app.route('/', methods=['POST', 'GET'])

def index():
  
  
    

  return render_template("index.html")

@app.route('/players', methods=['POST', 'GET'])

def players():

  session['Name'] = request.form['name']
  session['Jersey Number'] = request.form['jersey number']
  session['Team'] = request.form['team']
  
  playerRoster[session['Jersey Number']] = {
    session['Name'],
    session['Jersey Number'],
    session['Team']
  }

  # session['Jersey Number'] [session['Name'], session['Team']]
  print playerRoster
  return redirect('/')

app.run(debug=True)