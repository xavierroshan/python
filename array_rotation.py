arr= [1,2,3,4,5,6,7]
arr_size=len(arr)
d=2
for k in range(0,d):
    temp = arr[0]
    for i in range(0,arr_size-1):
        arr[i]=arr[i+1] 
    arr[arr_size-1]=temp
print(arr)