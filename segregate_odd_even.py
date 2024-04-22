# segregate even and odd 
# Method 1
list = [0,4,5,0,10,0,1,2,3,100,0,7,9,200,300,219]
list1=[]
list2=[]
for x in list:
    if x % 2 == 0:
        list1.append(x)
    else:
        list2.append(x)
print(list1+list2)
# Method 2 - without consuming memoryview
arr = [0,4,5,0,10,0,1,2,3,100,0,7,9,200,300,219]
left, right = 0, len(arr)-1

while left < right:
    while arr[left]%2 == 0:
        left += 1 
    while arr[right]%2 != 0:
        right -= 1 
    if left < right:
     arr[left], arr[right] = arr[right], arr[left]
print(arr)        