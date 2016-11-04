from flask import Flask, render_template, session, flash, request
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = "97ghbnev78wytbvnvnurwvrovywonvibelnrlidjnlx"
bcrypt = Bcrypt(app)

mysql = MySQLConnector(app, 'world')


@app.route('/')
def index():

    results =  mysql.query_db('SELECT name, continent FROM countries')
    return render_template('index.html', results=results)

@app.route('/countries')
def index():
  # results = mysql.query_db('SELECT countries.id, countries.name, region, cities.population, gnp, cities.name AS country_capital FROM countries JOIN cities ON countries.capital = cities.id ORDER BY countries.population DESC LIMIT 10')
  return render_template('index.html')



@app.route('/countries', methods=['POST'])
def create():
  create_data = {
  'name': request.form['name'],
  'region': request.form['region'],
  'population': request.form['population'],
  'capital': request.form['capital'],
  'gnp': request.form['gnp']
  }

  create_query = 'INSERT INTO countries (name, region, gnp, capital, population) VALUES (:name, :region, :gnp, :capital, :population)'
  row = mysql.query_db(create_query, create_data)
  
  return render_template('render_partial')



@app.route('/countries/new')
def new():
  return render_template('edit.html', results=False)



@app.route('/render_partial')
def partial():
  results = mysql.query_db('SELECT countries.id, countries.name, region, cities.population, gnp, cities.name AS country_capital FROM countries JOIN cities ON countries.capital = cities.id ORDER BY countries.population DESC LIMIT :first,10')
  
  return render_template('partials/partial.html', results=results)



@app.route('/countries/<id>')
def show(id):
  results = mysql.query_db('SELECT countries.id, countries.name, region, cities.population, gnp, cities.name AS country_capital FROM countries JOIN cities ON countries.capital = cities.id WHERE countries.id = {}'.format(id))
  
  language_query = 'SELECT * FROM languages WHERE country_id = :country_id'
  
  language_data = {
    'country_id': id
  }

  languages = mysql.query_db(language_query, language_data)

  return render_template('show.html', results=results[0], languages=languages)



@app.route('/countries/<id>', methods=['POST'])
def update(id):

  insert_data = {
    'name': request.form['name'],
    'gnp': request.form['gnp'],
    'region': request.form['region'],
    'population': request.form['population']
  }



app.run(debug=True)