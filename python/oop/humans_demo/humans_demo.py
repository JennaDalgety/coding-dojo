class Human(object):
  def __init__(self, clan=None):
    print 'New Human!!!!'

    self.clan = clan
    self.health = 100
    self.strength = 3
    self.intelligence = 3
    self.stealth = 3

  def taunt(self):
    print 'You want a piece of me?'



michael = Human('CodingDojo')
jimmy = Human('CodingNinjas')

michael.taunt()

print michael
print jimmy