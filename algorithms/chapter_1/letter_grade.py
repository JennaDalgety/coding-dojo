def letter_grade(grade):

  if 89 < grade < 100:
    print('Score: {}.  Grade: A'.format(grade))
  if 79 < grade < 90:
    print('Score: {}.  Grade: B'.format(grade))
  if 69 < grade < 80:
    print('Score: {}.  Grade: C'.format(grade))
  if 59 < grade < 70:
    print('Score: {}.  Grade: D'.format(grade))
  if grade < 60:
    print('Score: {}.  Grade: F'.format(grade))

letter_grade(80)