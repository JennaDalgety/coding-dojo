'''

Dragon Class
When the Dragon's displayHealth() function is called, it should say 'this is a dragon!' before it displays the default information. You can achieve this by calling the parent's displayHealth() function.

Now try creating a new Animal and confirm that it can not call the pet() and fly() methods, and it's displayHealth() is not saying 'this is a dragon!'. Also confirm that your Dog class can not fly().

'''



class Animal(object):

  def __init__(self, name):
    self.name = name
    self.health = 100

  def walk(self):
    self.health -= 1
    return self

  def run(self):
    self.health -= 5
    return self

  def display_health(self):
    print("{}: {}".format(self.name, self.health))


animal1 = Animal("Butter")

animal1.walk().walk().walk().run().run()
animal1.display_health()
