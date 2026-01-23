class Parent:

  def show(self):
    print("This is Parent class")


class child(Parent):

  def show(self):
    super().show()
    print("This child class")


s1 = child()
s1.show()

