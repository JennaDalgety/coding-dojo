# def draw_stars():
  
#   arr = [4, 6, 1, 3, 5, 7, 25]

#   for i in range(len(arr)):
    
#     arr[i] = '*' * arr[i]

#     print arr[i]


# draw_stars()



# def draw_stars():

#   arr = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

#   for i in range(len(arr)):

#     if isinstance(arr[i], basestring):

#       arr[i] = len(arr[i])

#     arr[i] = '*' * arr[i]

#     print arr[i]


# draw_stars()



def draw_stars():

  arr = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

  for i in range(len(arr)):

    if isinstance(arr[i], basestring):
      
      firstLetter = arr[i][0][0]

      arr[i] = len(arr[i])

      x = firstLetter * arr[i]

      arr[i] = x.lower()

    else: 
      
      arr[i] = '*' * arr[i]

    print arr[i]


draw_stars()