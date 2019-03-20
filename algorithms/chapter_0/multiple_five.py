def mult5():

  count = 0

  for i in range(512, 4097):
    if i % 5 == 0:
      print i
      count += 1
  print count

mult5()