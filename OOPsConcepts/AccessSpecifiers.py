class car:
  def __init__(self):
    self.color = "White"
    self._brand = "bmd"
    self.__price = "100000"


c = car()
print(c.color)
print(c._brand)
# print(c.__price) give error 
print(c._car__price)