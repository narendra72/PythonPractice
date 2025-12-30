class student:
  # Non-Parameterized constructor
  def __init__(self):
    self.name = "Rohan"
    self.age = 20

  def info(self):
    print(f"Student Name is {self.name} and  age is {self.age}")


s1 = student()
s1.info()
