# print("Recusion")

# # code for factorial of number
# def factorial(n):
#   if n==0 or n==1:
#     return 1
#   else:
#     return n * factorial (n - 1)

# print(factorial(3))
# print(factorial(4))

# fibonacci series 

def series(n):
  if n==0 or n==1:
    return n
  else:
    return series(n-1) + series(n-2)

def series_f(n):
  for i in range(n):
      print(series(i), end=" ")


series_f(6)