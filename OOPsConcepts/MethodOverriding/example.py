class Employee:
  def __init__(self,name,salary):
    self.name = name
    self.salary = salary

  def calculatedsalary(self):   # two inst variable pass not arg
    print("salary",self.salary)
    return self.salary

class Developer(Employee):
  def __init__(self,name,salary,bonus):
    super().__init__(name,salary)
    self.bonus = bonus

  def calculatedsalary(self):
    base = super().calculatedsalary()
    print("Salary with bonus")
    return base + self.bonus

d1 = Developer("Naren",1000000,10000)
print(d1.calculatedsalary())
    
