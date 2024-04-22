#Iterable and iterator
# list is iterable cause it can for looped
list = [1,2,3,4,5,6,7,8]
for x in list:
    print(x)
#Iterator is something on which next can be applied
Iterator = iter(list)
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
