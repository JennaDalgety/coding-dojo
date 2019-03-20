class Product(object):
  
  def __init__(self, price, name, weight, brand, cost):
    self.price = price
    self.name = name
    self.weight = weight
    self.brand = brand
    self.cost = cost

    self.status = "for sale"

  
  def sell(self):
    self.status = "sold"
    return self


  def add_tax(self):

    sales_tax = .11

    tax = self.price * sales_tax  #don't change the state of the object
    return self.price + tax


  def returny(self, reason):

    if reason == "defective":
      self.price = 0
      self.status = "defective"
    if reason == "in box" or reason  == "like new":
      self.status = "for sale"
    if reason == "opened":
      self.status = "used"
      discount = self.price  * .20
      self.price -= discount
    return self


  def display_info(self):
    print "Name:", self.name
    print "Price:", self.price
    print "Weight:", self.weight
    print "Cost:", self.cost
    print "Status:", self.status

  

product1 = Product(2.20, "Bananas", "1 lb.", "Chiquita", 1.50)
product1.returny("defective").display_info()
