#  Example 1 
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # true bcz data inside the vaiable is same 
print(a is b)  # false bcz list is mutable so it get different loction address

# Example 2 
x = (1,2,3)
y = (1,2,3)

print(x == y)  # true bcz it check data inside the variables 
print(x is y)  # true bcz tuples are immutable  

# Example 3
p = [1, 2, 3]
q = [1, 2, 4]

print(p == q)   
print(p is q) 
