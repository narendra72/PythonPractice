class A:

  def show(self):
    print("Parent class")

class B(A):

  def show(self):
    print("Derived1 class")

class C(A):

  def show(self):
    print("Derived2 class")

class D(B,C):

  def show(self):
    print("Derived3 class")

obj = D()
obj.show()
print(D.__mro__)    #Method Resolution Order (MRO)
