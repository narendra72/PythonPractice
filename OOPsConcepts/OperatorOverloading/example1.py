class mat:
  def __init__(self,a,b):
    self.a = a
    self.b = b

  def __add__(self,x):
    return mat(self.a + x.a , self.b + x.b)

m1 = mat(2,6)
m2 = mat(4,8)

m3 = m1 + m2
print(m3.a, m3.b)