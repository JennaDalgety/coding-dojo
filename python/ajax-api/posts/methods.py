def add_notes(form, mysql):

  query = 'INSERT INTO posts (description, created_at, updated_at) VALUES (:description, NOW(), NOW())'

  data = {
    'description': form['description']
  }

  mysql.query_db(query, data)



def display_notes(mysql):

  print 'We are displaying notes!'

  query = 'SELECT description FROM posts ORDER BY created_at DESC LIMIT 10'

  posts = mysql.query_db(query)
  return posts



# def index_json(mysql):

#   print 'we are indexing json!'

#   query = 'SELECT description FROM posts ORDER BY created_at DESC LIMIT 10'

#   posts = mysql.query_db(query)
#   return jsonify(posts)