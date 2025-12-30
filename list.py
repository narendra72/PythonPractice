# create a list 
# a = [1,2,"a","B","Hello",True]
# print(a)
# print(type(a))
# print(a[4])
# nested = [[1, 2], [3, 4]]
# print(nested[1])


# looping in list 
items = [ "apple","banna","cherry","mango"]
for i in items:
  if i =="banna":
    print(i)


# list Comprehension
nums = [x**2 for x in range(5)]
print(nums)


# list method 

l = [10,50,1,4,40,2,54]

# for add number in list at the end of list
l.append(100)
print(l)

#  for sorting in acending order
l.sort()
print(l)

#  for sorting in decending order
l.sort(reverse = True)
print(l)

#  for add new list to old list

m = [100,200,300]

l.extend(m)
print("After externding the list\n",l)


