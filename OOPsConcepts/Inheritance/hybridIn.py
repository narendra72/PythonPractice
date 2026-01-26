class A:
  
  def showA(self):
      print("A")

class B(A):          # single inheritance
  
  def showB(self):
      print("B")

class C(A):         # multilevel inheritance 
  
  def showC(self):
      print("C")

class D(B, C):     # multiple inheritance 
  
  def showD(self):
      print("D")

obj = D()
obj.showA()
obj.showB()
obj.showC()
obj.showD()
