'''

Given array of numbers, create function to replace last value with number of positive values.

Example: countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.


- define function
- create a count variable
- for loop through given list
- if the given value is positive, the count goes up by one
- else nothing
- once done looping, change the last value of the given list ([-1]) to the count

'''

def positives(listy):

  count = 0

  for i in listy:
    if i > 0:
      count += 1

  listy[-1] = count

  print listy

positives([-1, 1, 1, 1])