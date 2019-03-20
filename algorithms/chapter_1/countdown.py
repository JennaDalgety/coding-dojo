def doThis(num):

  blanky = [num]

  while num > 0:
    num -= 1
    blanky.append(num)

  print blanky
  print len(blanky)

doThis(10)