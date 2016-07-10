# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 14:37:09 2016

@author: waytoalpit
"""

import numpy as np

numpy_A= np.array([25.6, 84.3, 12.7, 62.8])
numpy_B= np.array([5.21, 34.3, 98.2, 46.4])

print(numpy_A)
print(numpy_B)

# multiplication of arrays
print(numpy_A * numpy_B)
# addition of arrays
print(numpy_A + numpy_B)


#some more basic examples
data= np.arange(10)
print (data)


#reshape into 2-D matrix
matrix= (data.reshape(5,2))
print (matrix)

#data type
print(type(matrix))
print(matrix.dtype)

#size
print(matrix.size)

#dimention
print (matrix.ndim)

#shape
print (matrix.shape)

print(matrix * matrix)
print(matrix + 2)