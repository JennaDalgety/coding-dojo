def threeNums(arr):

  if arr[0] > len(arr):
    print 'Too big!'
  elif arr[0] < len(arr):
    print 'Too small!'
  else:
    print 'Just right!'

threeNums([9, 5, 7, 9])