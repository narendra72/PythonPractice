try:
  a = 5
  b = 0
  print(a/b)
except ZeroDivisionError:
 print("Something went wrong")



# try:
#       x = int(input("Enter a number: "))
#       print(10 / x)
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# except ValueError:
#     print("Please enter a valid number!")


x = -5
if x < 0:
    raise ValueError("Only positive numbers are allowed!")
