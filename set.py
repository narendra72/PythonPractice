# print("set theory")

# set = {1,25,6,7,8}
# print(set)
# # it remove duplicate valus from the set
# set1 = {1,2,3,4,5,5,1,2}
# print(set1)


# give wrong output
# s = {1,2,[3,4]}
# print(s)

# tuples are allowed in set
# s ={1,2,(3,4)}
# print(s)

# add method
s = {1,2,3,4}
s.add(5)
s.update([6, 7])
print(s)

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))            # {1, 2, 3, 4, 5}
print(a.intersection(b))     # {3}
print(a.difference(b))       # {1, 2}
print(a.symmetric_difference(b))  # {1, 2, 4, 5}
