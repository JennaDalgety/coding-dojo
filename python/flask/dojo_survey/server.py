from flask import Flask, render_template, request, redirect
app = Flask(__name__)
app.secret_key = 'I am a secret key!'

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/results', methods=['POST'])
def create_user():
   print "Got Post Info"
   
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

   return render_template("results.html", user_info = user_info)



app.run(debug=True)