'''

- define function
- set up even count
- set up odd count
- for loop through list
- if there are three even numbers in a row, print message
- if there are three odd numbers in a row, print message

'''

def odd_even(listy):

  odd_count = 0
  even_count = 0

  for i in listy:
    print i
    if i % 2 != 0:
      odd_count += 1
      even_count = 0
      if odd_count == 3:
        print "That's odd!"
    elif i % 2 == 0:
      even_count += 1
      odd_count = 0
      if even_count == 3:
        print 'Even more so!'

odd_even([1, 2, 3, 4, 5, 5, 5, 6, 4, 4, 4, 7, 3, 4, 9, 9, 9, 2, 2, 2])