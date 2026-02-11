# indexing 
import numpy as np
arr = np.arange(5,50)
arr


print(arr[2])


arr1 = np.array([[1,2,3],[4,5,6]])
arr1


print(arr1[1,1])


arr2 = np.array([[[1, 2],[3, 4]],[[5, 6],[7, 8]]])
arr2


print(arr2[1,1,1])


# Slicing
arr


arr[1:7]


arr[10:]


print(arr1[:, 0:1])


# iteration 
arr


for i in arr:
    print(i)


arr1


for row in arr1:
    print(row)


for i in np.nditer(arr1):
    print(i)


 # Indexing with Boolean Arrays
import numpy as np


arr = np.random.randint(low = 10 ,high = 100, size= 20).reshape(4,5)
arr


arr[0]


arr[arr>50]


arr[(arr>50) & (arr<60)]




