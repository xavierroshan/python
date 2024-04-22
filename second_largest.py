# find three largest elements in the array 
import sys 
arr = [10, 4, 3, 50, 23, 90,200]
arr_size = len(arr)
first = second = -sys.maxsize

for i in range(0,arr_size):
    if arr[i] > first:
        second = first
        first = arr[i]
    elif arr[i] > second:
        second = arr[i]

print(second)
        