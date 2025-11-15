class student:
  # Parameterized constructor 
  def __init__(self,n,a):
    self.name = n
    self.age = a

  def info(self):
    print(f"Student Name is {self.name} and  age is {self.age}")


s1 = student("Rohan",20)
s1.info()
