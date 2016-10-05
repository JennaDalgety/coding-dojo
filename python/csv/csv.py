import csv

with open('us-500.csv', 'rb') as new_variable:
  reader = csv.reader(new_variable)
  for row in reader:
    print row