# NumPy Operations 
import numpy as np


arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])


arr1+arr2


arr1-arr2


arr2/arr1


arr2%arr1


arr1**arr2


# scaler operation
arr1+1


arr2*2


arr1>2


# Mathematical Functions
np.sqrt(arr2)


np.log(arr1)


np.sum(arr1)


arr3 = np.array([7,2,8])


np.sort(arr3)


# shape operation   --> dimensions
np.shape(arr3)


arr4 = np.array([[1,2,3],[4,5,6]])
arr4


np.shape(arr4)


# reshaping operations  --> changing shape without changing data
arr5 = np.array([1,2,3,4,5,6,7,8])
arr5


arr5.reshape(2,4)


arr5.reshape(4,-1)  # Auto calculate dimension


import numpy as np


arr6 = np.array([[1,2,3,4],[5,6,7,8]])
arr6


arr6.ravel()


arr6


arr6.T


# stacking
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])


np.hstack((arr1,arr2))


arr3 = np.vstack((arr1,arr2))
arr3


# spliting 
arr1


np.hsplit(arr1,3)


np.vsplit(arr3,2)


arr3.flatten()




