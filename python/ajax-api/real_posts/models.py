class Posts(object):
  def __init__(self, mysql, json):
    self.db = mysql
    self.json = json
    
  def get_all_posts(self):

    query = 'SELECT description from POSTS ORDER BY created_at DESC LIMIT 20'
    posts = self.db.query_db(query)

    return posts

  def add_post_to_db(self, abc):

    query = 'INSERT INTO posts (description, created_at, updated_at) VALUES (:description, :created_at, :updated:at)'
    
    data = {
      'description': abc['description']
    }

    insert_posts = self.db.query_db(query)