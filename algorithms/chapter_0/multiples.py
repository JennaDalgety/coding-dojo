#Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6.

def multiples():

  for i in range(3, -301, -1):
    if i % 3 == 0:
      if i == -3 or i == -6:
        continue
      else:
        print i

multiples()