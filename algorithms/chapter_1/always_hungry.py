def hungry(listy):

  count = 0

  for i in listy:
    print i
    if i == 'food':
      print 'yummy'
      count += 1
  if count == 0:
    print "I'm hungry"


hungry(['cat', 'food', 1, 2, 'dog'])