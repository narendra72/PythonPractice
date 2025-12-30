class student:

  schoolName = "ABC"  # class variable 
  def __init__(self,name,rollno):
    self.name = name   # instance variable
    self.rollno = rollno  # instance variable

  def show(self):
    print(f"Name of the student is {self.name} and roll number is {self.rollno} and study at {student.schoolName} ")

s1 = student("Narendra",11)
s1.show()
s2 = student("rohan", 12)
s2.show()

    
    