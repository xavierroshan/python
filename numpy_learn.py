"""
# Union function in numpy
import numpy as np
arr1 = np.array([10, 20, 30, 40]) 
print("array1 ", arr1) 
arr2 = np.array([20, 40, 60, 80]) 
print("array2 ", arr2) 
print(np.union1d(arr1,arr2))"""
"""
# Finding unique row in array
import numpy as np
arr2D = np.array([[11, 11, 12, 11],
                 [13, 11, 12, 11],
                 [16, 11, 12, 11],
                [11, 11, 12, 11]])
arr = np.unique(arr2D)
print(arr)
print('******')
arr = np.unique(arr2D, axis=0)
print(arr)
print('******')
arr = np.unique(arr2D, axis=1)
print(arr)
print('******')"""

"""
# Find index of the unique elements
import numpy as np
arr2D = np.array([[11, 11, 12, 11],
                     [13, 11, 12, 11],
                     [16, 11, 12, 11],
                     [11, 11, 12, 11]])
print(np.unique(arr2D, return_index = True))
print(np.unique(arr2D, return_inverse = True))
"""
"""
# Trim leading an trailing zeros
import numpy as np 
arr = np.array([0,0,0,0,0,2,5,6,8,0,0,0,0])
arr1 = np.trim_zeros(arr)
print(arr1)
arr1 = np.trim_zeros(arr, 'f')
print(arr1)
arr1 = np.trim_zeros(arr, 'b')
print(arr1)"""

"""# Rounding of a number
import numpy as np
arr = [[1.1,2.2,2.3],
       [3.1,5.1,6.7]]
print(arr)
print(np.round(arr))"""

"""# String operations
import numpy as np
arr = [['Roshan', 'Xavier', 'Chirayil'],
       ['Deepa', 'Joseph', 'Kanadamangalathan']]

print(np.char.lower(arr))
print(np.char.upper(arr))


str1 = "My name is Roshan"
arr = np.char.split(str1)
print(arr)
arr = np.char.split(str1, sep=' ')
print(arr)"""


"""# only showing certain index
import numpy as np
a = np.arange(10, 1, -2) 
b = a[np.array([2,4])]
print(b)

import numpy as np
a = np.arange(0,8)
print(a)
b = a[2:8:2]
print(b)"""

"""# advanced index
arr = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])
row_index = np.array([0,1,2])
column_index = np.array([0,1,2])
arr1 = arr[row_index,column_index]
print(arr1)

arr = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])

print(arr[arr>3])"""

"""arr = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])

print(arr[arr%3==0]*10)"""

"""
import numpy as np
arr = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])

a = np.compress((True, False, True),arr, axis=0)

print(a)"""


"""import numpy as np 
  
# Creating a 3X4 2-D Numpy array 
arr = np.array([[101, 20, 3, 10],  
                [40, 5, 66, 7],  
                [70, 88, 9, 141]]) 

print(arr[0:2,0:1])"""

"""# Broadcasting
import numpy as np 
arr = np.array([101, 20, 3, 10])
arr1 = np.array([10])
print(arr+arr1)
arr = np.array([[101, 20, 3, 10],  
                [40, 5, 66, 7],  
                [70, 88, 9, 141]])

arr1 = np.array([10])
print(arr+arr1)
arr1 = np.array([10,20,30,40])
print(arr+arr1)
print('*********************')

import numpy as np
 
a = np.array([5, 7, 3, 1])
b = np.array([90, 50, 0,2])
print(a*b)"""

"""# variance, SD, mean etc
import numpy as np
arr = np.array([1, 2, 1, 1])
print(np.std(arr))
print(np.var(arr))
print(np.mean(arr))
print(np.median(arr))"""

"""#arithematic operations
import numpy as np
a = np.array([1, 2, 1, 1])
b = np.array([90, 50, 0,2])

print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))"""

"""import numpy as np
a = np.array([1, 2, 1, 1], dtype=float)
b = np.array([2, 3, 5,2])
print(np.divide(a,b))
print(np.reciprocal(a))"""


"""import numpy as np
b = np.array([2, 3, 5,2])
mean = np.mean(b)
c = b-mean
print(np.mean(abs(c)))"""

# trace determinant, etc
import numpy as np
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])

print(np.linalg.matrix_rank(A))
print(np.trace(A))
print(np.linalg.det(A))
print(np.linalg.matrix_power(A,3))

































































