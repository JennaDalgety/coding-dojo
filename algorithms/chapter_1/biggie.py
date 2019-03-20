def biggie(listy):

  for n, i in enumerate(listy):
    if i > 0:
      listy[n] = 'big'
  print listy

biggie([-1, 3, 5, -5])