# when parent and child class has the same variable name but in child class we want only parent class variable 

class parent:
  x = 20

  def __init__(self):
    print("parent class")

class child(parent):
  x = 30

  def __init__(self):
     super().__init__()
     print(super().x)
     print(self.x)
     print("child class")

c1 = child()
  
  

   


  