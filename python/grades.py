'''

Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:

Score: 60 - 69; Grade - D Score: 70 - 79; Grade - C Score: 80 - 89; Grade - B Score: 90 - 100; Grade - A

'''

import random

def grades():

  print('Scores and Grades')

  for i in range(1, 11):
    random_num = random.randint(60, 100)
    if 60 <= random_num <= 69:
      print('Score: {}; Your grade is D'.format(random_num))
    if 70 <= random_num <= 79:
      print('Score: {}; Your grade is C'.format(random_num))
    if 80 <= random_num <= 89:
      print('Score: {}; Your grade is B'.format(random_num))
    if 90 <= random_num <= 100:
      print('Score: {}; Your grade is A'.format(random_num))

  print('End of the program.  Bye!')

grades()