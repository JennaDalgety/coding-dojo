from humans import Human
class Wizard(Human):
  def __init__(self):
    super(Wizard, self).__init__()
    self.intelligence = 10
  def heal(self):
    self.health += 10
class Ninja(Human):
  def __init__(self):
    super(Ninja, self).__init__()
    self.stealth = 10
  def steal(self):
    self.stealth += 5
class Samurai(Human):
  def __init__(self):
    super(Samurai, self).__init__()
    self.strength = 10
  def sacrifice(self):
    self.health -= 5
# create new instance of Wizard, Ninja, and Samurai
harry = Wizard()
rain = Ninja()
tom = Samurai()
# all instances still have human properties because its
# class inherits from the Human class
print harry.health
print rain.health
print tom.health
# yet they are subclasses which mean they can extend the current functionality of Human class
# instances of the Wizard class can perform the heal method
harry.heal()
print harry.health
# instances of the Ninja class can perform the steal method
rain.steal()
print rain.stealth
# instances of the Samurai class can perform the sacrifice method
tom.sacrifice()
print tom.health
print tom.stealth