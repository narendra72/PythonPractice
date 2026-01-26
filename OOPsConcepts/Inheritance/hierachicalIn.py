class Parent:

  def showA(self):
    print("Parent class")

class child1(Parent):

  def showB(self):
    print("Child1 class")

class child2(Parent):

  def showC(self):
    print("child2 class")

c1 = child1()
c2 = child2()

c1.showB()
c1.showA()

c2.showC()
c2.showA()