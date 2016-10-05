def oddEven():

  for num in range(1,2001):
    if num % 2 == 0:
      print("Number is {0}.  This is an even number.".format(num))
    if num % 2 != 0:
      print("Number is {0}.  This is an odd number.".format(num))

oddEven()  