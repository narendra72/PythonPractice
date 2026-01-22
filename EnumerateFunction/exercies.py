# enumerate() allows us to loop through an iterable while keeping track of the index and the value simultaneously.

# through Normal function 

Car = ["BMW","rolls_royce","bugatti","maclaren"]

for i in range(len(Car)):
  print(i,Car[i])


# same task with enumerate function

for index , Car in enumerate(Car):
  print(index,Car)