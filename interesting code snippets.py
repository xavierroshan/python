#interesting code snippets

#1
print([x**2 for x in range(10)])


#2
import random
random_number = random.randint(1,200)
print(random_number)

#3
num = 6
result = 'even' if num % 2 == 0 else 'odd'
print(result)


#4 enumerate
fruit_list = ['apple', 'orange', 'pear', 'pineapple', 'grapes']
for index, fruit in enumerate(fruit_list):
    print(f"{index}:{fruit}")
    
    
#5
my_dict = {'a': 1, 'b': 2, 'c': 3}
print( 'z' in my_dict)
print( 'a' in my_dict)
print(my_dict.get('a', 'default'))
print(my_dict.get('z', 'default'))
print(my_dict['a'])

#6
list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = [1,2,3,4,5]
for x,y in zip(list1, list2):
    print(x,y)

#7
SUM(x) for x in range(5)


