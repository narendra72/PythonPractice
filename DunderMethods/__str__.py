class student:

  def __init__(self,name):
    self.name = name

  def __str__(self):   # if we use only str it give differnt o/p
    return f"Student Name is {self.name}"

s1 = student("Naren")
# print(s1.__str__())
print(s1)

# Without __str__  if we try to print an object in Python shows a message that containing the memory address

    