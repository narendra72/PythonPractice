class student:

  def __init__(self,name):
    self.name = name

  def __repr__(self):     # repr method defination depends on developer how he write  
    return f"Student Name is = '{self.name}'"

s1 = student("Naren")

print(s1)



