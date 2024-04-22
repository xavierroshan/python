arr= [10, 5, 6, 3, 2, 20, 100, 80]
arr = sorted(arr)
arr_size=len(arr)
print(arr)
for i in range(0,arr_size,2):
    arr[i], arr[i+1] = arr[i+1], arr[i]
print(arr)