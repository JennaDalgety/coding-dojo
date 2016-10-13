 # Finish the assignment and upload your code below
 # Create a simple web application that holds a counter that increments every time the page is visited. Complete this using session.
 # For ninjas: add a +2 button underneath the counter that increments the counter by 2 and reloads the page.
 # For hackers: add a reset button that will reset the counter to 1


from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'iaugfbaerkjcnbwi479uronfqriugfnbwuliwe'


@app.route('/', methods=['POST', 'GET'])

def index():
  
  print type(session)

  if 'counter' not in session:
    session['counter'] = 0

  if request.method == 'POST':
    
    if 'Ninjas' in request.form:
      session['counter'] += 2

    elif 'Hackers' in request.form:
      session['counter'] = 1

  else:
    session['counter'] += 1
    

  return render_template("index.html", counter=session['counter'])


app.run(debug=True)