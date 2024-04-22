# Find subarrays with given sum
arr = [2,3,4,1,2,3,4]
arr_size = len(arr)
subarray_sum = 0
k = 7

for i in range(0,arr_size):
    subarray_sum +=arr[i]
    for j in range(i+1,arr_size):
        subarray_sum+=arr[j]
        if subarray_sum == 7:
            print(arr[i:j+1])
            break
    subarray_sum =0
    