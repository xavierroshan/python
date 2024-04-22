import numpy as np

arr2D = np.array([[11, 11, 12, 11],
                     [13, 11, 12, 11],
                     [16, 11, 12, 11],
                     [11, 11, 12, 11]])
uniquerows = np.unique(arr2D)
print(uniquerows)