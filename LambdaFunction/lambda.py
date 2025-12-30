#  Normal function

def add(a,b):
  return a+b

print(add(2,4))

#  Lambda Function 

add = lambda a , b: a + b 

print(add(2,4))

avg = lambda a,b,c: a+b+c/3
print(avg(2,4,6))


# No need to define function name 
lambda a: a*a
print(5)

add = lambda x, y: x + y
print(add(3, 5))   # Output: 8
