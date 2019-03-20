print "  x   1   2   3   4   5   6   7   8   9  10  11  12",
print
for x_axis in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
  for y_axis in [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
    print format(x_axis * y_axis, '3d'),
  print