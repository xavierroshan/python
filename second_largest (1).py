# find second largest elements in the array 
import sys 
arr = [10, 4,4, 3,3, 50, 23, 90,200]
print(arr)
arr = set(arr)
print(arr)
print(sorted(list(arr),reverse = True)[1])

        