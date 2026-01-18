class Student:
    college_name = "SKIT"  # Class Variable

    def __init__(self, name):
        self.name = name

    @classmethod       
    def change_college(cls, new_name):
        cls.college_name = new_name

    def show_info(self):
        print(f"Student: {self.name} , College: {self.college_name}")


s1 = Student("Rahul")
s2 = Student("Narendra")

Student.change_college("MNIT")

s1.show_info()  # Output College: MNIT
s2.show_info()  # Output  College: MNIT
print(s1.college_name)

# class variable is change from SKIT to MNIT 
