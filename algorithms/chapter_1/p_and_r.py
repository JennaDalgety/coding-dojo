'''

Build a function that takes array of numbers. The function should print second-to-last value in the array, and return first odd value in the array.

- define function
- pick out the second to last value, [-2]
- print that value
- pick out the first odd value, [1]
- return this value

'''

def printReturn(listy):

  print listy[-2]
  return listy[1]

printReturn([2, 3, 4, 5, 6])