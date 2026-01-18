class math:

  @staticmethod
  def add(a,b):   # not required self 
    return a+b

t1 = math()
print(math.add(2,4))  # class name se call no instance required
print(t1.add(4,5))    # call though object

# Static Method Cannot Access Instance or Class Variables

'''class hello:
  x = 10

  @staticmethod
  def show():
    print(self.x)

h1 = hello()
print(h1.show()) '''
