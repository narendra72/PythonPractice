def add():
  x = 10  # local variable 
  print(x)

add()
# print(x)  # local variable can not be use outside the function


y = 20
def sum():
  print(y) # global var can be use inside the function and everywhere

sum()
print(y)