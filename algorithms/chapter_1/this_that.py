def jinx(num1, num2):

  blanky = []

  for i in range(num1):
    blanky.append(num2)
  print blanky
  if num1 == num2:
    print "Jinx!"

jinx(5, 2)