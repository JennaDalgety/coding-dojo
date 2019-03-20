def replace(listy):

  newListy = []

  for i in listy[1:]:
    newListy.append(len(i))

  print newListy


replace(['hello', 'goodbye', 'start', 'stop'])