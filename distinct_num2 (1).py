# distinct element
arr = [1,4,2,7,9,4,1,10,20,30,30,20,1,0,0,1,1]
arr_size = len(arr)
for i in range(0,arr_size):
    d=0
    for j in range(0,i):
        if arr[i]==arr[j]:
            d=1
            break
    if d==0:
        print(arr[i])