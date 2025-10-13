print("Custom Error")
x = int(input("Enter Number"))

if(x>5 or x<0):
  raise ValueError("Enter number between 0 to 4")