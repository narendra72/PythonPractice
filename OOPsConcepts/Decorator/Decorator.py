
def decfunction(fx):
  def wrapper(*args,**kwargs):
    print("Good moring")
    fx(*args,**kwargs)
    print("Thanks for using this function")
  return wrapper

@decfunction
def hello():
  print("Hello World")

hello()

@decfunction
def add(a,b):
  print(a+b)

add(2,4)