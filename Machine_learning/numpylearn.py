"""
0 D array

import numpy as np
# arr= numpy.array(1)
# print(arr)  # Output: [1]
# print(arr.ndim) #nth dimension Output: [0]
"""
# import numpy as np
#1D array in numpy
# import numpy as np
# arr= np.array([1,2,3,4])
# print(arr)  # Output: [1 2 3 4]
# print(arr.ndim) #nth dimension 

"""
This are called 2D matrices.
They are used to represent data in a table format.
"""
# arraye= np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arraye)
# print(arraye.ndim)

# import numpy as np

# arr3=np.zeros((2,3))  #zeros are uses for making a matrix.We have send the value in tuple. It can easily make an matrix.
# print(arr3)

# arr4=np.ones((3,3))
# print(arr4)

# arr5=np.identity(5) #using identity the value are arrange in a matrix as per given input row=column and in diagonal all values would be 1
# print(arr5)


# arr6=np.arange(10) # arange() is similar of range() in python loop. 
# arr6=np.arange(1,11) # arange() is similar of range() in python loop. 
# arr6=np.arange(11,0,-1) # arange() is similar of range() in python loop. 
# print(arr6)

import numpy as np
ars1=np.array([1,2,3,4,5])
# print(ars1.shape)
ars2=np.array([[1,2,3,4],[6,7,8,9]])
print(ars2.shape)
print(ars2.ndim)

#for calculate how the structure are made for this: 2 matrix 2 row 6 column 
ars3=np.array([[[1,2,3,4,5,6],[7,8,9,10,11,12]],[[13,14,15,16,17,18],[19,20,21,22,23,24]]])
print(ars3.shape)
print(ars3.ndim)

#for counting number of item
print('for counting number of item')
print(ars1.size)
print(ars2.size)
print(ars3.size)

#Finding data type
print('Finding Data Type')
print(ars2.dtype)

#changing data type
print('changing data type')
print(ars3.astype('float'))