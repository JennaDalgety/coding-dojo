from animal import Animal

class Dog(Animal):
  def __init__(self, name):
    super(Dog, self).__init__(name)
    self.health = 150

  def pet(self):
    self.health = self.health + 5

    return self


class Dragon(Animal):
  def __init__(self, name):
    super(Dragon, self).__init__(name)
    self.health = 170
  
  def display_health(self):
    print 'this is a dragon! ' + self.name + ': ' + str(self.health)

  def fly(self):
    self.health = self.health - 10

    return self



dog = Dog('Bartholemew')
dragon = Dragon('Smaug')

dog.walk().walk().walk().run().run().pet().display_health()
dragon.walk().walk().walk().run().run().fly().fly().display_health()