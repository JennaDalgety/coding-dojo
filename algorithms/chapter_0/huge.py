def huge():

  sum = 0

  for i in range(-300, 300):
    if i % 2 != 0:
      sum = sum + i

  print sum

huge()