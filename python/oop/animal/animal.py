class Animal(object):
  def __init__(self, name):
    self.health = 100
    self.name = name

  def walk(self):
    self.health = self.health - 1
    return self

  def run(self):
    self.health = self.health - 5
    return self

  def display_health(self):

    print self.name + ': ' + str(self.health)

animal = Animal('Bobby')

animal.walk().walk().walk().run().run().display_health()
