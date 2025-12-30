mylist = [1,2,3,4,5,6]
square = list(filter(lambda x : x>4, mylist))
print(square)

numbers = [10, 15, 20, 25, 30]
even_nums = list(filter(lambda x: x % 2 == 0, numbers))
print(even_nums)
