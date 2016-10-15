from flask import Flask, session, render_template, redirect
import random, datetime
app = Flask(__name__)
app.secret_key = "eioruvn54w8uoi4nrtuirwunru.fjitrnmg"

@app.route('/', methods=['GET', 'POST'])

def index():

  if 'gold' not in session:
    session['gold'] = 0
    session['activities'] = []

  return render_template('index.html')

@app.route('/process_money/<building>', methods=['POST'])

def earn(building):  

  if building == 'farm':
    earned = random.randint(10, 20)
    message = 'Earned '+str(earned)+' gold from the farm! {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

  if building == 'cave':
    earned = random.randint(5, 10)
    message = 'Earned '+str(earned)+' gold from the cave! {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

  if building == 'house':
    earned = random.randint(2, 5)
    message = 'Earned '+str(earned)+' gold from the house! {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

  if building == 'casino':
    earned = random.randint(-50, 50)
    message = 'Entered a casino and won '+str(earned)+' gold! {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    if earned < 0:
      message = 'Entered a casino and lost '+str(earned)+' gold.  Ouch. {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    elif earned == 0:
      message = 'Entered a casino and broke even. {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

  session['gold'] += earned
  session['activities'].insert(0, message)


  return redirect('/')


app.run(debug=True)