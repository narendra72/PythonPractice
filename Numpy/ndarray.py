# creating n-d arrays
import numpy as np 


# np.array   --> convert list into array
# 1 d array
arr1 = np.array([1,2,3,4])   
arr1


type(arr1)


# 2 d array 
arr2 = np.array([[1,2,3,4],[5,6,7,8]])
arr2


# n d array just to initallise pass tuples 
# np.zeros(())
arr3 = np.zeros((2,2))
arr3


# np.ones(())
arr4 = np.ones((4,4))
arr4


# np.identity()   --> to create identity matrix 
arr5 = np.identity(4)
arr5


arr6 = np.arange(10)
arr6


arr7 = np.arange(10,20,2)
arr7


arr8 = np.linspace(10,20,5)  # give 5 equidistant point between 10 and 20
arr8


# to copy the privices array
arr9 = arr1.copy()
arr9


arr10 = np.full((2,3),7)
arr10


arr11 = np.random.rand(3)
arr11


arr12 = np.random.rand(2,3)
arr12


arr13 = np.random.randint(1, 10, size=(5,2))
arr13




