def highLow(listy):

  min = listy[0]
  max = listy[0]
  
  for i in listy:
    if i < min:
      min = i
    if i > max:
      max = i

  print min
  return max

highLow([1,3,5,7,9])