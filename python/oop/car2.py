class Car(object):

  def __init__(self, price, speed, fuel, mileage):
    self.price = price
    self.speed = speed
    self.fuel = fuel
    self.mileage = mileage

    if self.price > 10000:
      self.tax = 0.12
    else:
      self.tax = 0.15

    self.display_all()

  def display_all(self):
    print "Price:", self.price
    print "Speed:", self.speed
    print "Fuel:", self.fuel
    print "Mileage:", self.mileage
    print "Tax:", self.tax
    print "-" * 30

    

car1 = Car(15000, "35 mph", "Full", "15 mpg")
car2 = Car(20000, "50 mph", "Not Full", "17 mpg")
car3 = Car(10000, "40 mph", "Kind of Full", "16 mpg")
car4 = Car(50000, "60 mph", "Empty", "10 mpg")
car5 = Car(100000, "80 mph", "Full", "13 mpg")
car6 = Car(5000, "30 mph", "Kind of Full", "20 mpg")

# car6.display_all()