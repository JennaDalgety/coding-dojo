class Bike(object):

  def __init__(self, price, max_speed):
    self.price = price
    self.max_speed = max_speed
    self.miles = 0

  def display_info(self):
    print self.price
    print self.max_speed
    print self.miles

  def ride(self):
    print ("Riding")
    self.miles += 10
    return self

  def reverse(self):
    if self.miles < 0:
      print ("You can't go negative miles")
    else:
      print ("Reversing")
      self.miles -= 5
    return self

    


bike1 = Bike(200, "25 mph")
bike2 = Bike(300, "30 mph")
bike3 = Bike(400, "40 mph")

bike1.ride().ride().ride().reverse().display_info()
bike2.ride().ride().reverse().reverse().display_info()
bike3.reverse().reverse().reverse()
