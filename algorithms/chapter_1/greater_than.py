def greaterThan(arr):

  count = 0

  for i in arr:
    if i > arr[1]:
      print i
      count += 1
  print count

greaterThan([1, 3, 5, 7, 9, 13])