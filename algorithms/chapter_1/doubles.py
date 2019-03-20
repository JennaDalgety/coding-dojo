'''

Given array, create a function to return a new array where each value in the original has been doubled. Calling double([1,2,3]) should return [2,4,6] without changing original.

- define function
- create a blank list
- for loop through given list
- multiply each value in the list by 2
- append each value to the blank list
- print new/blank list

'''

def doubles(listy):

  new_listy = []

  for i in listy:
    i *= 2
    new_listy.append(i)

  print new_listy

doubles([1, 2, 3])