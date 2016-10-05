def scoresGrades():

  scores = []

  print "Enter 10 test scores:"

  score1 = input("")
  scores.append(score1)
  score2 = input("")
  scores.append(score2)
  score3 = input("")
  scores.append(score3)
  score4 = input("")
  scores.append(score4)
  score5 = input("")
  scores.append(score5)
  score6 = input("")
  scores.append(score6)
  score7 = input("")
  scores.append(score7)
  score8 = input("")
  scores.append(score8)
  score9 = input("")
  scores.append(score9)
  score10 = input("")
  scores.append(score10)

  print "Scores and Grades"

  for i in range(len(scores)):

    if scores[i] >= 90 and scores[i] <= 100:
      print('Score: {0}; Your grade is A'.format(scores[i]))
    elif scores[i] >= 80 and scores[i] <= 89:
      print('Score: {0}; Your grade is B'.format(scores[i]))
    elif scores[i] >= 70 and scores[i] <= 79:
      print('Score: {0}; Your grade is C'.format(scores[i]))
    elif scores[i] >= 60 and scores[i] <= 69:
      print('Score: {0}; Your grade is D'.format(scores[i]))
    else:
      print('Score: {0}; Your grade is F'.format(scores[i]))

  print "End of the program.  Bye!"


scoresGrades()