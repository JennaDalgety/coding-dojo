class Vertebrate(object):
  def __init__(self):
    self.has_backbone = True
    
class Mammal(Vertebrate):
  def __init__(self):
    super(Mammal, self).__init__()
    print 'here in mammal'
    self.number_of_legs = 4
    self.hp = 5
    self.regulates_internal_body_temp = True
    self.has_fur = True
  def breathe(self):
    print 'respiring'

class Cat(Mammal):  # object is just saying it can do these things and have methods
  def __init__(self, name): # added , name to create a variable name that goes along with self.name
    super(Cat, self).__init__()
    self.name = name
    self.hp = 20  # self is like this in javascript/jquery
    self.well_being = 100
    self.hunger = 0
    
  def meow(self):
    print 'miao'
  def sleep(self):
    if self.hp < 20:
      self.hp += 5
    print 'zzzzz', self.hp
  def walk(self):
    self.hp -= 3
  def chase_bird(self):
    self.hp -= 12
    print 'chased a bird, hp are', self.hp





squirrel = Cat('confused')
print squirrel.hp, squirrel.number_of_legs


meowth = Cat("Garfield")  # pass in name down here when we instantiate the cat
print meowth.name, meowth.hp, meowth.well_being

cat2 = Cat("Heathcliff")
cat2.number_of_legs = 3 
print cat2.name, cat2.hp, cat2.well_being

meowth.meow()
cat2.sleep()
cat2.chase_bird()
cat2.sleep()
cat2.sleep()
print cat2