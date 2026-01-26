class Animal:

  def show(self):
    print("This is an parent class")

class dog(Animal):

  def show1(self):
    print("This is am child class")

c1 = dog()
c1.show()
c1.show1()
