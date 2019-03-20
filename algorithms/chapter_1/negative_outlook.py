def negs(listy):

  newListy = []

  for i in listy:
    if i > 0:
      i = i * -1
    newListy.append(i)

  return newListy


negs([1, -3, 5])