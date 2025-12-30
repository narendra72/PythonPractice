class Human:
  firstname = "Narendra"
  lastname = "Choudhary"
  age = 21

  def info(self):
    print(f"{self.firstname} {self.lastname} age is {self.age}")


person1 = Human()
person1.firstname = "Rohan"
person1.info()


person2 = Human()
person2.firstname = "Prakash"
person2.age = 15
person2.info()

