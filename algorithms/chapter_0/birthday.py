#If 2 given numbers represent your birth month and day in either order, log "How did you know?", else log "Just another day....",

#Example: given yourBirthday(4,19) or yourBirthday(19,4)


# def birthday(num1, num2):

#   full_birthday = [4, 19]

#   for i in full_birthday:
#     if (i[0], i[1]) == (num1, num2) or (i[1], i[0]) == (num2, num1):
#       print('How did you know?')
#     else:
#       print('Just another day....')

# birthday(19, 4)


def birthday(guess1, guess2):

  month = 'February'
  day = 1

  if ((guess1, guess2) == (month, day)) or ((guess1, guess2) == (day, month)):
    print('How did you know?')
  else:
    print('Just another day...')

birthday(1, 'February')