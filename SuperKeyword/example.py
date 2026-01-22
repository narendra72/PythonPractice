class Parent:
  def show(self):
    print("This is Parent class")

class child(Parent):
  def show1(self):
    print("This child class")


s1 = child()
print(s1.show1())

  