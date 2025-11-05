#  Normal function

def add(a,b):
  return a+b

print(add(2,4))

#  Lambda Function 

add = lambda a , b: a + b 

print(add(2,4))

avg = lambda a,b,c: a+b+c/3
print(avg(2,4,6))


lambda a: a*a
print(5)