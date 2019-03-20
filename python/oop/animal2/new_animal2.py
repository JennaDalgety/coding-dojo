from animal2 import Animal


class Dog(Animal):

  def __init__(self, name):
    super(Dog, self).__init__(name)
    self.health = 150

  def pet(self):
    self.health += 5
    return self


class Dragon(Animal):

  def __init__(self, name):
    super(Dragon, self).__init__(name)
    self.health = 170

  def fly(self):
    self.health -= 10
    return self

  def display_health(self):
    print("this is a dragon!")
    print("{}: {}".format(self.name, self.health))





dog1 = Dog("Fido")
dragon1 = Dragon("Beelzebub")

dog1.walk().walk().walk().run().run().pet()
dog1.display_health()

dragon1.walk().walk().walk().run().run().fly().fly()
dragon1.display_health()