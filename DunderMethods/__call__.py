class Car:
  
  def __init__(self):
    print("Hello")

  def __call__(self,name):
    self.name = name
    print(f"this is my {self.name} car")

c1 = Car()
c1("bugatti chiron")       #  object called like a function

