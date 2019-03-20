def accurate_grade(grade):

  if 89 < grade < 100:
    if grade in range(90, 93):
      print('Score: {}.  Grade: A-'.format(grade))
    else:
      print('Score: {}.  Grade: A'.format(grade))
  if 79 < grade < 90:
    if grade in range(80, 83):
      print('Score: {}.  Grade: B-'.format(grade))
    if grade in range(88, 90):
      print('Score: {}.  Grade: B+'.format(grade))
    else:
      print('Score: {}.  Grade: B'.format(grade))
  if 69 < grade < 80:
    if grade in range(70, 73):
      print('Score: {}.  Grade: C-'.format(grade))
    if grade in range(78, 80):
      print('Score: {}.  Grade: C+'.format(grade))
    else:
      print('Score: {}.  Grade: C'.format(grade))
  if 59 < grade < 70:
    if grade in range(60, 63):
      print('Score: {}.  Grade: D-'.format(grade))
    if grade in range(68, 70):
      print('Score: {}.  Grade: D+'.format(grade))
    else:
      print('Score: {}.  Grade: D'.format(grade))
  if grade < 60:
    print('Score: {}.  Grade: F'.format(grade))

accurate_grade(87)