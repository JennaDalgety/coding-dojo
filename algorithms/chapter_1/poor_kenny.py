import random

def what_happens_today():

  chance = random.randint(1, 100)

  if chance <= 10:
    print('Kenny got melted by a volcano!')
  elif 11 <= chance <= 25:
    print('Kenny got drowned by a tsunami!')
  elif 26 <= chance <= 45:
    print('Kenny got buried by an earthquake!')
  elif 46 <= chance <= 70:
    print('Kenny got buried by a blizzard!')
  elif 71 <= chance <= 100:
    print('Kenny got smashed by a meteor strike!')
  
what_happens_today()