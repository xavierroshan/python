# Count the number of possible triangles
arr = [4, 6, 3, 7]
arr1 = []
n =len(arr)
for i in range(0,n):
    for j in range(i+1, n):
        for k in range(j+1,n):
            if arr[i]+arr[j] > arr[k] and arr[j]+arr[k] > arr[i] and arr[i]+arr[k] > arr[j]:
                arr1.append([arr[i], arr[j], arr[k]])

print(arr1)
