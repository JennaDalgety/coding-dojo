from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "thisisthesupersecretkey"



@app.route('/')
def index():

    return render_template('index.html')

@app.route('/ninjas')
def ninjas():

    return render_template('ninjas.html')


@app.route('/ninjas/<color>')
def ninjacolor(color):
  ninjas = {
    'red': 'raphael',
    'orange': 'michaelangelo',
    'blue': 'leonardo',
    'purple': 'donatello'
  }

  if color == 'red' or color == 'blue' or color == 'orange' or color == 'purple':
    return render_template('ninjas.html', color = ninjas[color])
  else:
    return render_template('ninjas.html', color = 'april')




app.run(debug=True)
