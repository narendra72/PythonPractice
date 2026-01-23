# Calling the Parent Constructor

class Parent:

  def __init__(self):
    print("Hello this is my car")

class child(Parent):

  def __init__(self):
    super().__init__()    # if we want to access the parent class constructor than need to use super keyword
    print("hii bro")

c1 = child()

# no need to call method bcz constructor call automatically when an object of that class is created 
# Python automatically passes 'self'