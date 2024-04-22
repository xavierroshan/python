
#method 6
lst = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
lst2 = []
lst3 = []
for x in lst:
    if x not in lst2:
        lst2.append(x)
    elif x not in lst3:
        lst3.append(x)
        
print(lst3)
