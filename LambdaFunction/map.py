def square(x):
  return x * x 

print(square(2))

mylist = [1,2,3,4,5,6]

newlist = []
for item in mylist:
  newlist.append(square(item))

print(newlist)



#  by using map function 
newlist = list(map(square,mylist))
print(newlist)