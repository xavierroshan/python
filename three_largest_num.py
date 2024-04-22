# find three largest elements in the array 
import sys 
arr = [10, 4, 3, 50, 23, 90]
arr_size = len(arr)
first = second = third = -sys.maxsize

for i in range(0,arr_size):
    if arr[i] > first:
        third = second
        second = first
        first = arr[i]
    elif arr[i] > second:
        third = second
        second = arr[i]
    elif arr[i] > third:
        third = arr[i]
print(first, second, third)
        