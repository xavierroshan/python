# Print All Distinct Elements of a given integer array
# Method1
arr = [0,4,5,0,10,0,1,2,3,100,0,7,9,200,300,219,300,219,0,4,5]
arr1 = []
for x in arr:
    if x not in arr1:
        arr1.append(x)
print(arr1)   

# Method2


