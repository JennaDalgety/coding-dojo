def swap(listy):


  for idx, val in enumerate(listy):
    if idx % 3 == 0:
      listy[idx], listy[-(idx + 1)] = listy[-(idx + 1)], listy[idx]
  print listy


swap([1, 2, 3, 4, 5, 6])