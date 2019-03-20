'''

Given an array of numbers arr, add 1 to every second element, specifically those whose index is odd (arr[1], [3], [5], etc). Afterward, console.log each array value and return arr.

- define function
- create empty list
- for loop through given list
- add 1 to each odd index value in the list
- append new value to empty list
- print each index value
- return list

'''

def incrementSecond(listy):

  new_listy = []

  for i in range(len(listy)):
    if i % 2 != 0:
      listy[i] += 1
    else:
      listy[i]
    new_listy.append(listy[i])
    print listy[i]

  print new_listy

incrementSecond([2, 4, 6, 8, 9, 7, 5, 3])