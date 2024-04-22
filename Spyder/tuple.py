#Find the size of a Tuple in Python

import sys
Tuple1 = ("A", 1, "B", 2, "C", 3)
print(Tuple1.__sizeof__())
print(sys.getsizeof(Tuple1))



#Python program to create a list of tuples from given list having number and its cube in each tuple
#Input: list = [1, 2, 3]
#Output: [(1, 1), (2, 8), (3, 27)]

#Input: list = [9, 5, 6]
#Output: [(9, 729), (5, 125), (6, 216)]


#method 1
lst = [1, 2, 3]
lst1 = [(x,x**3) for x in lst]
print(lst1)

#method 2
lst = [1, 2, 3]
lst1 = list(map(lambda x : (x,x**3), lst))
print(lst1)

#method 3
lst = [1, 2, 3]
lst1 = []
for x in lst:
    tup=(x,x**3)
    lst1.append(tup)
print(lst1)


#Python – Adding Tuple to List and vice – versa
#The original list is : [5, 6, 7]
#tuple: (9,10)
#The container after addition : [5, 6, 7, 9, 10]

#method 1
lst =  [5, 6, 7]
tup = (9,10)
lst = lst+list(tup)
print(lst)

#method 2

lst =  [5, 6, 7]
tup = (9,10)
for i in tup:
    lst.append(i)
print(tuple(lst))

#method 3
lst =  [5, 6, 7]
tup = (9,10)
lst.extend(list(tup))
print(lst)


#method 3
lst =  [5, 6, 7]
tup = (9,10)
index=3
lst.insert(index, tup)
print(lst)

#Python program to sort a list of tuples by second Item
#Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
#Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]


#method 1
input_lst = [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
output_lst = sorted(input_lst, key = lambda x:x[1])
print(output_lst)

#method 2
input_lst = [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
input_lst.sort(key=lambda x: x[1])
print(input_lst)


#method 3
from operator import itemgetter
input_lst = [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
output_lst = sorted(input_lst, key=itemgetter(1))
print(output_lst)

#method 4
input_lst = [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
l = len(input_lst)
for i in range(l):
    for j in range(l-i-1):
        if input_lst[j][1]>input_lst[j+1][1]:
            input_lst[j], input_lst[j+1]= input_lst[j+1], input_lst[j]
print( input_lst)


#Python – Flatten tuple of List to tuple
#Input : test_tuple = ([5], [6], [3], [8]) 
#Output : (5, 6, 3, 8) 

#Input : test_tuple = ([5, 7, 8]) 
#Output : (5, 7, 8)

#method1 
test_tuple = ([5], [6], [3], [8]) 
test_tuple = ([5], [6], [3], [8,9]) 
test_tuple1 = tuple()


for i in test_tuple:
    if type(i)==list:
        for j in i:
            test_tuple1 = test_tuple1 + (j,)      
print(test_tuple1)

#method 2
res = []
for i in test_tuple:
    res.extend(i)
print(tuple(res))
    


#method 3
test_tuple = ([5, 6], [6, 7, 8, 9], [3])
res = tuple(sum(test_tuple, []))
print(res)

#method 4
from itertools import chain
test_tuple = ([5, 6], [6, 7, 8, 9], [3])
res = tuple(chain.from_iterable(test_tuple))
print(res)
res = tuple(chain(*test_tuple))
print(res)

#method 5
test_tuple = ([5, 6], [6, 7, 8, 9], [3])
res = []
[res.extend(x) for x in test_tuple]
print(tuple(res))


#method 6
test_tuple = ([5, 6], [6, 7, 8, 9], [3])
res = []
y = list(map(lambda x:res.extend(x),test_tuple))
print(tuple(res))
################ Recursion method #############





#Python – Convert Nested Tuple to Custom Key Dictionary
#The original tuple : ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))
#The converted dictionary : [{'key': 4, 'value': 'Gfg', 'id': 10}, {'key': 3, 'value': 'is', 'id': 8}, {'key': 6, 'value': 'Best', 'id': 10}]


#method 1
tuple1 = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))
dict1 = {}
res = []



for i in range(len(tuple1)):
    for j in tuple1: 
        dict1['key']=tuple1[i][0]
        dict1['value']=tuple1[i][1]
        dict1['id']=tuple1[i][2]
    res.append(dict1)
    dict1 = {}
        
print(res)
print('\n')


#method 2
tuple1 = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))
dict1 = {}
res = []



for i in range(len(tuple1)):
    dict1 = {}
    for j in tuple1: 
        dict1['key']=tuple1[i][0]
        dict1['value']=tuple1[i][1]
        dict1['id']=tuple1[i][2]
    res.append(dict1)
        
print(res)
print('\n')

#method 3
tuple1 = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))
dict1 = {}
res = []
for i in range(len(tuple1)):
    for j in tuple1: 
        dict1.update({'key':tuple1[i][0]})
        dict1.update({'value':tuple1[i][1]})
        dict1.update({'id':tuple1[i][2]})
    res.append(dict1)
    dict1 = {}
        
print(res)
print('\n')

#method 4
test_tuple = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10)) 
y = [({'key':x[0], 'value':x[1], 'id':x[2]}) for x in test_tuple]
print(y)


#method 5

test_tuple = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10)) 
keys = ['key', 'value', 'id'] 

res = [{key:value for key, value in zip(keys,x)} for x in test_tuple]
print(res)



#Python – Order Tuples by external List

#Input : test_list = [(‘Gfg’, 10), (‘best’, 3), (‘CS’, 8), (‘Geeks’, 7)]
#ord_list = [‘Geeks’, ‘best’, ‘CS’, ‘Gfg’] 
#Output : [(‘Geeks’, 7), (‘best’, 3), (‘CS’, 8), (‘Gfg’, 10)] 

#Input : test_list = [(‘best’, 3), (‘CS’, 8), (‘Geeks’, 7)], ord_list = [‘Geeks’, ‘best’, ‘CS’] 
#Output : [(‘Geeks’, 7), (‘best’, 3), (‘CS’, 8)]

#method 1
input_list = [('Gfg', 10), ('rx',20),('best', 3), ('CS', 8), ('Geeks', 7),('dj',4)]
ord_list = ['dj','Geeks', 'best', 'CS', 'rx','Gfg']     



for i in range(len(input_list)):
    index = ord_list.index(input_list[i][0])
    if index!=i:
        input_list[i],input_list[index]=input_list[index], input_list[i]
print(input_list)

#method 2
input_list = [('Gfg', 10), ('rx',20),('best', 3), ('CS', 8), ('Geeks', 7)]
ord_list = ['Geeks', 'best', 'CS', 'rx','Gfg']  
temp=dict(input_list)
res = [ (x,temp[x]) for x in ord_list]
print(res)

#method 3
input_list = [('Gfg', 10), ('rx',20),('best', 3), ('CS', 8), ('Geeks', 7)]
ord_list = ['Geeks', 'best', 'CS', 'rx','Gfg']  
temp=dict(input_list)
y = list(map(lambda x: (x,temp[x]),ord_list))
print(y)
######################## Learn functools #############################
######################## itemgetter ##################################

#method 4

input_list = [('Gfg', 10), ('rx',20),('best', 3), ('CS', 8), ('Geeks', 7),('dj',4)]
ord_list = ['dj','Geeks', 'best', 'CS', 'rx','Gfg'] 
lst1 = []
lst2 = []

for i in input_list:
    lst1.append(i[0])
for i in ord_list:
    if i in lst1:
        lst2.append(input_list[lst1.index(i)])
        
print(lst2)

#easy way to order
from operator import itemgetter
input_list = [('Gfg', 10), ('Rx',20),('Best', 3), ('CS', 8), ('Geeks', 7),('Dj',4)]
ord_list = ['Dj','Geeks', 'Best', 'CS', 'Rx','Gfg'] 

ord_list = sorted(input_list, key=itemgetter(1))
print(ord_list)

ord_list = sorted(input_list, key=itemgetter(0))
print(ord_list)

#method 5
test_list = [('Gfg', 10), ('Best', 3), ('CS', 8), ('Geeks', 7)]
ord_list = ['Geeks', 'Best', 'CS', 'Gfg']
y = sorted(test_list, key = lambda x: ord_list.index(x[0]))
print(y)
################### learn reduce function ######################


#Python – All pair combinations of 2 tuples

#Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8) 
#Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)] 
#Input : test_tuple1 = (9, 2), test_tuple2 = (7, 8) 
#Output : [(9, 7), (9, 8), (2, 7), (2, 8), (7, 9), (7, 2), (8, 9), (8, 2)]

# method 1
test_tuple1 = (7, 2) 
test_tuple2 = (3, 5) 
lst = []
for i in test_tuple1:
    for j in test_tuple2:
        lst.append((i,j))
for j in test_tuple2:
    for i in test_tuple1:
        lst.append((j,i))
print(lst)

# method 2
test_tuple1 = (7, 2) 
test_tuple2 = (3, 5) 
lst = []
for i in test_tuple1:
    for j in test_tuple2:
        lst.append((i,j))
        lst.append((j,i))
print(lst)

#method 3
test_tuple1 = (7, 2) 
test_tuple2 = (3, 5) 

y = (tuple([(i,j) for i in test_tuple1 for j in test_tuple2] + [(i,j) for i in test_tuple2 for j in test_tuple1]))
print(y)


#method 4
from itertools import chain, product

y = chain(product(test_tuple1,test_tuple2), product(test_tuple2, test_tuple1))
print(tuple(y))


#Python – Remove tuples of length K
#Input : test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)], K = 2 
#Output : [(4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)] 
#Explanation : (4, 5) of len = 2 is removed. 

#Input : test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)], K = 3 
#Output : [(4, 5), (4, ), (1, ), (3, 4, 6, 7)] 
#Explanation : 3 length tuple is removed.

#method 1
#test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)] 
#K = 2 
test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)] 
K = 3 
output = []

for x in test_list:
    count=0
    for y in x:
        count+=1
    if count ==K:
        continue
    else:
        output.append(x)
print(output)

#method 2
test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)] 
K = 3 
y = [x for x in test_list if len(x)!=K]
print(y)

#method 3

test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)] 
K = 3 
y = list(filter(lambda x: len(x)!=K, test_list))
print(y)



#Python – Extract digits from Tuple list
#Input : test_list = [(15, 3), (3, 9)] 
#Output : [9, 5, 3, 1]

#Input : test_list = [(15, 3)] 
#Output : [5, 3, 1] 


#method 1
#test_list = [(15, 3), (3, 9)] 
test_list = [(15, 3)] 
output=[]

for x in test_list:
    for y in x:
        z = str(y)
        for i in z:
            output.append(int(i))
print(list(set(output)))

#method 2

test_list = [(15, 3)] 
output= [int(i) for x in test_list for y in x for i in str(y)]
print(output)

################ learn re ###################

#method 3
test_list = [(15, 3)] 
output= [i for x in test_list for y in x for i in str(y)]
print(list(map(int,output)))

"""""
TBD
ython – Maximum and Minimum K elements in Tuple
Python – Closest Pair to Kth index element in Tuple
"""







     




