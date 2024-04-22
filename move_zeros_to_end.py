# move all zeros to the end of the array 
# Method 1
list = [0,4,5,0,10,0,1,2,3,100,0]
list1 = []
count=0
for x in list:
    if x == 0:
        count+=1
    else:
        list1.append(x)
if count >0:
    for i in range(count):
        list1.append(0)
print(list1)

# Method 2
arr = [0,4,5,0,10,0,1,2,3,100,0]
arr1 = []
count=0
arr_size = len(arr)
for i in range (arr_size):
    if arr[i]!=0:
        arr[count]=arr[i]
        count+=1 
        
while count < arr_size:
    arr[count]=0
    count+=1 
print(arr)


        
    