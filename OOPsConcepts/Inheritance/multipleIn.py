class A:

  def showA(self):
    print("Parent1 class")

class B:

  def showB(self):
    print("Parent2 class")

class C (A,B):

  def showC(self):
    print("Child class")

c1 = C()
c1.showA()
c1.showB()
c1.showC()