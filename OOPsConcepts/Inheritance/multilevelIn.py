class A:

  def showA(self):
    print("GrandParent class")

class B(A):

  def showB(self):
    print("Parent class")

class C(B):

  def showC(self):
    print("Child class")

c1 = C()
c1.showA()
c1.showB()
c1.showC()