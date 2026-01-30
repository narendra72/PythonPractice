# Noraml function 

def squares(n):
  result = []

  for i in range(n):
    result.append(i*i)
  return result
  
print(squares(4))

# generator 

def square(m):
  for i in range(m):
    yield i*i

gen = square(4)
print(next(gen))
print(next(gen))
print(next(gen))


