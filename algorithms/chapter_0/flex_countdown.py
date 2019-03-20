def paramFlex(param1, param2, param3, param4):

  while param2 < param3:
    param2 += 1
    if param2 == param4:
      continue
    if param2 % 3 == 0:
      print param2


paramFlex(3, 5, 17, 9)