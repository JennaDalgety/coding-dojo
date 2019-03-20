import random

def what_really_happens_today():

  chance = random.randint(1, 100)
  kenny = 'alive'
  
  if chance <= 10:
    print('Kenny got melted by a volcano!')
    kenny = 'dead'
  chance = random.randint(1, 100)
  if 11 <= chance <= 25:
    print('Kenny got drowned by a tsunami!')
    kenny = 'dead'
  chance = random.randint(1, 100)
  if 26 <= chance <= 45:
    print('Kenny got buried by an earthquake!')
    kenny = "dead"
  chance = random.randint(1, 100)
  if 46 <= chance <= 70:
    print('Kenny got buried by a blizzard!')
    kenny = "dead"
  chance = random.randint(1, 100)
  if 71 <= chance <= 100:
    print('Kenny got smashed by a meteor strike!')
    kenny = "dead"

  if kenny != "dead":
    print('Kenny survived!!!')
  

what_really_happens_today()