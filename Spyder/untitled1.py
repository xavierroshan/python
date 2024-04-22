# Python program to find Cumulative sum of a list
lst = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
n = len(lst)
for i in range(n-1,-1,-1):
    sum = 0
    for j in range(i+1):
        sum = sum+lst[j]        
    lst[i]=sum
print(lst)
    