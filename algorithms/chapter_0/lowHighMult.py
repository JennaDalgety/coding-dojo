def lowHighMult(lowNum, highNum, mult):

  for num in range(highNum, lowNum, -1):
    if num % mult == 0:
      print num

lowHighMult(2, 9, 3)