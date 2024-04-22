# Leaders in an arry
arr = [16, 17, 4, 3, 5, 2]
arr1 = []
n =len(arr)

for i in range(0,n):
    flag = True
    for j in range(i+1,n):
        if arr[i] > arr[j]:
            pass
        else:
            flag = False
            break
    if flag == True:
        arr1.append(arr[i])
        
print(arr1)        
        

