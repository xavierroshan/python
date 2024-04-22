#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#Python | Ways to find length of list

#method 4

lst = [1,2,3,4,5,6,1,2,2]
for i, j in enumerate(lst):
    i
print(i+1)

#method 4
lst = [1,2,3,4,5,6,1,2,2]
from collections import Counter
Counter(lst).values()


#method 5

def count_recur(lst):
    count = 0
    if not lst:
        return 0
    else: 
        count+=1 + count_recur(lst[1:])
    return count
        
lst = [1,2,3,4,5,6,1,2]
print(count_recur(lst))
        

lst = [1,2,3,4,5,6,1,2]    
from operator import length_hint
print(length_hint(lst))


#Python | Ways to check if element exists in list

lst =[1,2,3,4,5,6,1,2,2]
x = 1

#method 1
if x in lst:
    print("yes")
else:
    print("no")
    
#method 2
print(x in lst)

#method 3
for i in range(len(lst)):
    if lst[i] == x:
        print("yes")
        break
    
#method 4
print(lst.count(x)>0)

#method 5
try:
    print(0 <= lst.index(x) <= len(lst)-1)
except:
    print("not in the list")

#method 6



lst =[1,2,3,4,5,6,1,2,2]
if ''.join(list(map(str,lst))).find('2') == -1: 
    print(False)
else: 
     print(True)
     
#Different ways to clear a list in Python

#method 1

lst =[1,2,3,4,5,6,1,2,2]
lst.clear()
print(lst)

#method 2
lst =[1,2,3,4,5,6,1,2,2]
for i in range(len(lst)):
    lst.pop()
print(lst)

#method 3
lst =[1,2,3,4,5,6,1,2,2]
lst = []
print(lst)

#method 4
lst =[1,2,3,4,5,6,1,2,2]
lst*=0
print(lst)

#method 5
lst =[1,2,3,4,5,6,1,2,2]
del lst[:]
print(lst)


    # Python | Cloning or Copying a list
#method 1
lst1 = [1,2,3,4]
lst2 = []
lst2.extend(lst1)
print(lst2)
print(id(lst2))
print(lst1)
print(id(lst1))
print('\n')

#method 2
import copy
lst1 = [1,2,3,4]
lst2 = copy.copy(lst1)
print(lst2)
print(id(lst2))
print(lst1)
print(id(lst1))
print('\n')


#method 3
lst1 = [1,2,3,4]
lst2 = [x for x in lst1]
print(lst2)
print(id(lst2))
print(lst1)
print(id(lst1))
print('\n')

#method 4
lst1 = [4, 8, 2, 10, 15, 18]
lst2 = list(map(int,lst1))
print(lst2)
print(id(lst2))
print(lst1)
print(id(lst1))
print('\n')

#method 5
from collections import deque
lst1 = [4, 8, 2, 10, 15, 18]
lst2 = deque(lst1)
print(lst2)
print(id(lst2))
print(lst1)
print(id(lst1))
print('\n')

########### lEarn functools#############


#Python | Count occurrences of an element in a list

#method 1
lst =[1,2,3,4,5,6,1,2,2]
x = 2
print(lst.count(2))

#method 2
lst =[1,2,3,4,5,6,1,2,2]
x = 2
count = 0
for i in lst:
    if i == x:
        count+=1
print(count)

#method 3
lst =[1,2,3,4,5,6,1,2,2]
x = 2
count = 0
while x in lst:
    lst.pop(lst.index(x))
    count+=1
    
print(count)

#method 4
lst =[1,2,3,4,5,6,1,2,2]
x=2
print(sum(1 for i in lst if i ==x ))

#method 5
lst =[1,2,3,4,5,6,1,2,2]
x=2
print(sum([1 for i in lst if i ==x ]))

#method 6
from collections import Counter
lst =[1,2,3,4,5,6,1,2,2]
print(Counter(lst)[2])


#method 6
import operator
lst =[1,2,3,4,5,6,1,2,2]
print(operator.countOf(lst,2))


#method 7

lst = ['a', 'd', 'd', 'c', 'a', 'b', 'b', 'a', 'c', 'd', 'e']
x ={item:lst.count(item) for item in lst}
print(x)
lst =[1,2,3,4,5,6,1,2,2]
x ={item:lst.count(item) for item in lst}
print(x)
print(x[2])


#Python | Remove empty tuples from a list

#method 1


tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), (), (), (',')]

print([i for i in tuples if type(i)==tuple and i!=()])
print('\n')




#method 2

tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), (), (), (',')]
print([i for i in tuples if i])
print('\n')

#method 3

tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), (), (), (',')]
print(list(filter(None, tuples)))
print('\n')

#method 4

tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), (), (), (',')]
while () in tuples:
    tuples.remove(())
print(tuples)

#method 5


tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), (), (), (',')]

print([i for i in tuples if type(i)==tuple and len(i)!=0])
print('\n')

############## learn recursion ################

#method 1
lst = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
dict1 = {item:lst.count(item) for item in lst}
lst2 = []
for x,y in dict1.items():
    if y >1:
        lst2.append(x)
        print(x,y)
print(lst2)

#method 2
#method 2
from collections import Counter
lst = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
dict1 = Counter(lst)
y=list([items for items in dict1 if dict1[items]>1])
print(y)



#method 3
lst = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
lst2 = []
lst3 = []
for x in lst:
    if x not in lst2:
        lst2.append(x)
    else:
        lst3.append(x)
        
print(lst2)
print(list(set(lst3)))

#method 4 - brute forse
lst = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
n = len(lst)
lst2 = []
for i in range(n):
    for j in range(i):
        if lst[i]==lst[j] and lst[i] not in lst2:
            lst2.append(lst[j])
        else:
            continue
print(lst2)


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

#method 7
lst = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
lst2 = []
for i in lst:
    if lst.count(i)>1 and i not in lst2:
        lst2.append(i)
print(lst2)


#method 7
lst = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
x = [item for item in lst if lst.count(item)>1]
print(set(x))

#method 8: Using list-dictionary approach (without any inbuild count function)
dict1, lst1 = {}, []
lst = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20] 

for i in lst:
    if i not in dict1:
        dict1[i]= 1
    else:
        dict1[i]+=1 
        
print(dict1)

for x in dict1.keys():
    if dict1[x]>1 :
        lst1.append(x)
        
print(lst1)


# Python program to find Cumulative sum of a list
#method 1
lst = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
n = len(lst)
for i in range(n-1,-1,-1):
    sum = 0
    for j in range(i+1):
        sum = sum+lst[j]        
    lst[i]=sum
print(lst)

#method 2
lst=[10,20,30,40,50]
new_list=[] 
n = len(lst)
for i in range(n):
    sum = 0
    for j in range(i+1):
        sum+=lst[j]
    new_list.append(sum)
print(new_list)


#method 3 - interesting
lst=[10,20,30,40,50]
new_list=[] 
j=0
for i in range(len(lst)):
    j+=lst[i]
    new_list.append(j)
print(new_list)


#method 4
lst=[1,2,3,4,5,6,7,8,9,10]
print([sum(lst[0:x:1]) for x in lst])


# Python | Sum of number digits in List
#method 1
lst = [19, 213, 3456, 29834, 234567]
lst1 = list(map(str,lst))
n = len(lst1)
print(lst1)

    

for i in range(n):
    str1 = lst1[i]
    lst2 = list(str1)
    lst3 = list(map(int,lst2))
    sum(lst3)
    lst1[i]= sum(lst3)
print(lst1)

#method 2
lst = [19, 213, 3456, 29834, 234567]
lst2 = []

for x in lst:
    sum = 0
    for digit in str(x):
        sum+=int(digit)
    lst2.append(sum)
    
print(lst2)

#method 3



def digit_sum_func(num):
    digit_sum = 0
    while num >0:
        digit_sum+= num%10
        num = num//10
    return (digit_sum) 

lst = [19, 213, 3456, 29834, 234567]
lst2 = []

for x in lst:
    lst2.append(digit_sum_func(x))

print(lst2)

method 4
test_list = [12, 67, 98, 34]
res = (list(str(x) for x in test_list))
res = ((sum(int(digit) for digit in str(x)) for x in test_list))
print(list(res))
# below 
#print(res.__next__())
#print(res.__next__())
#print(res.__next__())
#print(res.__next__())

method 5
test_list = [12, 67, 98, 34]
res = map(lambda x: sum(int(digit) for digit in str(x)), test_list)
print(list(res))

# Break a list into chunks of size N in Python
#method 1
lst = [1,2,3,4,5,6,7,8,9,10,11,12, 13,14,15,16,17]
n = len(lst)
N=4
num_of_arr = n//N
last_arr_len = n % N 
l,r=0,4
print(last_arr_len)
for i in range(num_of_arr):
    print(lst[l:r])
    l+=N
    r+=N
if last_arr_len >0:
    print(lst[l:(l+last_arr_len)])
    
    
#method 2
    
lst = [1,2,3,4,5,6,7,8,9]
start = 0
end = len(lst)
step = 3
for x in range(start, end, step):
    print(lst[x:x+step])
    

#method 3
def break_list(lst,n):
    for i in range(0,len(lst),n):
        yield lst[i:i+n]


lst = [1,2,3,4,5,6,7,8,9]
n = 3
print(list(break_list(lst, n)))

#method 4

lst = [1,2,3,4,5,6,7,8,9]
n = 3
print([lst[i:i+n] for i in range(0,len(lst),n)])

#method 5

lst = [1,2,3,4,5,6,7,8,9]
n = 3

print(list(map(lambda i:lst[i:i+n], range(0,len(lst),n))))

#Sfind second largest number in the list

#method 1
import sys
largest = second=-sys.maxsize
lst2 = [70, 11, 20, 4, 100,200,1000]

for x in lst2:
    if x > largest:
        second=largest
        largest = x
    elif x > second:
        second =x
    else:
        continue
print(largest, second)


#method 1 - for three numbers
import sys
largest = second=third=-sys.maxsize
lst2 = [70, 11, 20, 4, 100,200,1000, 2000]

for x in lst2:
    if x > largest: 
        third = second
        second = largest
        largest = x
    elif x > second:
        third = second
        second = x
       
    elif x > third:
        third = x
print(largest, second, third)

#method 2

lst1 = [70, 11, 20, 4, 100,200,1000,2000]
lst2 = list(set(lst1))
lst2.sort(reverse=True)
print(lst2[1])

#method1

### Python Program to Check if a String is Palindrome or Not
#Python program to check if a string is palindrome or not
str1 = '21malayalam12'
lst = list(str1)
l,r = 0, len(lst)-1
flag = True
while l<r:
    if lst[l]!=lst[r]:
        flag = False
        break
    else:
        l+=1
        r-=1
if flag == True:
    print("Paliandrome")
else:
    print("Not Paliandrome")  
    
#method2
str1 = '1malayalam12'
lst1 = list(str1)
lst2 = []
print(lst1)

for i in range(len(lst1)-1, -1, -1):
    lst2.append(lst1[i])
if lst1 == lst2:
    print("Palindrome")
else:
    print("Not Palindrome")
    
#method 3
str1 = 'malayalam'
lst = list(str1)
lst1 = lst.copy()
n = len(lst1)
lst2 = []
print(lst)
print(lst2)
for i in range(len(lst1)-1,-1,-1):
    lst2.append(lst1.pop())
if lst == lst2:
    print("Palindrome")
else:
    print("Not Palindrome")

print(lst)
print(lst2)

#method 4
str1 = '1malayalam12'
str2 = ''

for x in str1:
    str2 = x+str2
if str1 == str2:
    print("Palindrome")
else:
    print("Not Palindrome")
    
#method 5
str1 = 'malayalam'
str2 = str1[::-1]
if str1 == str2:
    print("Palindrome")
else:
    print("Not Palindrome")
    
# Reverse words in a given String in Python
#method 1
string = "geeks quiz practice code"
print(string[::-1])

#method2
string = "geeks quiz practice code"
string1 = ''
for x in string:
    string1 = x+string1
print(string1)


#method3
string = "geeks quiz practice code"
lst = list(string)
lst1 = []
for i in range(len(lst)):
    lst1.append(lst.pop())
print(''.join(lst1))


#method4
string = "geeks quiz practice code"
lst = list(string)
lst1 = []
for i in range(len(lst)-1,-1,-1):
    lst1.append(lst.pop())
print(''.join(lst1))


#method 5
string = "geeks quiz practice code"
print(''.join(list(reversed(string))))

# Ways to remove i’th character from string in Python
#Input: 'Geeks123For123Geeks'
#Output: GeeksForGeeks



#Using translate()
str1 = 'Geeks123For123Geeks'
translation_table = {ord(i):None for i in '123'}
result = str1.translate(translation_table)
print('Using transtation method..')
print(result)
print('\n')

#Using str.replace()
str1 = 'Geeks123For123Geeks'
str2 = str1.replace('123', '',1)
print(str2)


#Using Native Method
str1 = 'Geeks123For123Geeks'
pos = 5
str2 = ''

for i in range(len(str1)):
    if i != 5:
        str2 = str2 + str1[i]
print(str2)  

# #Using slice + concatenation
str1 = 'Geeks123For123Geeks'
pos = 5
str2 = str1[:4]+str1[6:]
print(str2)

#Using str.join()
str1 = 'Geeks123For123Geeks'
lst = list(str1)
print(lst.index('1'))
lst.remove('2')
print(lst)
print(''.join(lst))
print(lst.index('1'))
lst.pop(lst.index('1'))
print(''.join(lst))

#Using removeprefix()
str1 = 'Geeks123For123Geeks'
print(str1[:8])
print(str1[:8].removesuffix('123'))
print(str1[8:11])
print(str1[11:19].removeprefix('123'))
str2 = str1[:8].removesuffix('123') + str1[8:11] + str1[11:19].removeprefix('123')
print(str2)

############### use recursion method ########


#translation method is awesome
str1 = 'Geeks123For123Geeks'
translation_table1 = {ord(i):None for i in '123'}
translation_table2 = {ord(i):'x' for i in 'es'}
result1 = str1.translate(translation_table1)
print(result1)
result2 = str1.translate(translation_table2)
print(result2)

#Find length of a string in python (6 ways)

#method 1
str1 = 'Geeks13For123Geeks'
count = 0
for x in str1:
    count+=1
print(count)

#method 2
str1 = 'Geeks13For123Geeks'
print(len(str1))

#method 3
str1 = 'Geeks13For123Geeks'
counter = 0
while str1[counter:]:
    counter+=1
print(counter)


#method 4
str1 = 'Geeks13For123Geeks'
print(sum(1 for i in str1))


#method 5
str1 = 'Geeks13For123Geeks'
print(sum([1 for i in str1]))

#method 6
str1 = 'Geeks13For123Geeks'
i=0
for i, a in enumerate(str1):
    i+=1
print(i)

#method 7
str1 = 'Geeks13For123Geeks'
random_str = 'xxx'
str2 = random_str.join(str1)
print(str2.count('xxx')+1)

#Python | Maximum frequency character in String

#method1
str1 = 'Geeks123For123Geeks'
set1 = set(str1)
lst1 = list(set1)
dict1 = {}
for z in lst1:
    j=str1.count(z)
    dict1[z]=j
print(dict1)
print(max(dict1, key=dict1.get))

#method2
str1 = 'Geeks123For123Geeks'
my_dict = {}
for i in str1:
    if i in my_dict:
        my_dict[i]+=1
    else:
        my_dict[i]=1
print(my_dict)
print(max(my_dict, key=my_dict.get))


 
# Function to find the least frequent characters
#method 1
def least_frequent_char(input_str):
    freq_dict = {}
    for char in input_str:
        freq_dict[char]=freq_dict.get(char,0)+1
    
    min_value = min(freq_dict.values())
    least_frequent_char = ''
    
    for x,y in freq_dict.items():
        if y == min_value:
            least_frequent_char=x
            return(least_frequent_char)
 
 
# Driver Code
input_str = "geeksforgeeks"
 
print(least_frequent_char(input_str))


#Python program to accept the strings which contains all vowels
#Input : geeksforgeeks
#Output : Not Accepted
#All vowels except 'a','i','u' are not present

#Input : ABeeIghiObhkUul
#Output : Accepted

#method 1
#input_str= 'ABeeIghiObhkUul'
input_str= 'geeksforgeeks'
check_str= 'aeiou'
lst = []

for i in check_str:
    if i in input_str.lower():
        if i not in lst:
            lst.append(i)
        else:
            continue
    else:
        continue
print(''.join(lst)==check_str)

#method 2
#input_str= 'ABeeIghiObhkUul'
input_str= 'geeksforgeeks'

check_str = 'aeiou'
set1 = set(input_str.lower())
set2 = set(check_str)
set3 = set()
for i in set2:
    if i in set1:
        set3.add(i)
print(len(set3) == len(set2))



#method 3
#input_str= 'ABeeIghiObhkUul'
input_str= 'geeksforgeeks'
check_str = 'aeiou'

y = [input_str.lower().count(x) for x in check_str]
print(all([x>0 for x in y]))



#method 4
#set operators: Union |, intersection &, difference -, symmetric difference ^, 
# subset <=, superset >=
#input_str= 'ABeeIghiObhkUul'
input_str= 'geeksforgeeks'
check_str = 'aeiou'
set1 = set(input_str.lower())
set2 = set(check_str)
print(set1 >=set2)






#method 5
#input_str= 'ABeeIghiObhkUul'
input_str= 'geeksforgeeks'
check_str = 'aeiou'

lst = [char for char in input_str.lower() if char in check_str]
set1 = set(lst)
lst1 = sorted(list(set1))
print(lst1 == sorted(list(check_str)))


#method 6
input_str= 'ABeeIghiObhkUul'
#input_str= 'geeksforgeeks'
check_str = 'aeiou'

lst = [char for char in input_str.lower() if char in check_str]
set1 = set(lst)
lst1 = sorted(list(set1))
print(lst1 == sorted(list(check_str)))


#method 7
#input_str= 'ABeeIghiObhkUul'
#nput_str= 'geeksforgeeks'
check_str = 'aeiou'

lst = [char for char in input_str.lower() if char in check_str]
print(lst)
dict1,lst1 = {}, []
for i in lst:
    dict1[i]= lst.count(i)
for x,y in dict1.items():
    lst1.append(y)
print(all([1 for x in lst1 if x >0]) and len(lst1)==5)


#Python | Check if a Substring is Present in a Given String
#Input: Substring = "geeks" 
#String="geeks for geeks"



#method 1 - Using In Operator
    
Substring = "geeks" 
Substring = "geeks1" 
String="geeks for geeks"

print(Substring in String)

#method2 - Checking using split() method
#example of split
str1 = "geeks for geeks"
lst1 = str1.split(' ')
print(lst1)
#Actual code
Substring = "geeks" 
String="geeks for geeks"
str1 = "geeks for geeks"
lst1 = str1.split(' ')
flag = False
for i in lst1:
    if i == Substring:
        flag = True
print(flag)

#method 3 - Using find() method
Substring = "geeks" 
String="geeks for geeks"
print(String.find(Substring)>=0)
print(String.find(Substring, 0, len(String))>=0)

#method 4 - Using “count()” method
Substring = "geeks1" 
String="geeks for geeks"
print(String.count(Substring)>0)
print(String.count(Substring,0, len(String))>0)

#method 5 - Using index() method
Substring = "geeks" 
String="geeks for geeks"
print(String.index(Substring)>=0)



#method 6 - Using list comprehension 
Substring = "geeks" 
String="geeks for geeks"
print([True if String in Substring else False][0])

#method 7 - Using lambda function 
str2 = "geeks" 
str1="geeks for geeks"
x =list(filter(lambda x:(str2 in str1), str1.split() ))
print(x)
print(["yes" if x else "no"])


#method 8 - Using  __contains__” magic class.
str2 = "geeks" 
str1="geeks for geeks"
print(str1.__contains__(str1))

#method 9 - using operator contains() 
import operator as op
str2 = "geeks1" 
str1="geeks for geeks"
print(op.contains(str1, str2))

#method 10 - Using regular expressions
import re
str2 = "geeks1" 
str1="geeks for geeks"
if re.search(str2,str1):
    print(True)
else:
    print(False)
    
#method 11 - 


def is_substring(string, substring):
    for i in range(len(string) - len(substring)+1):
        if string[i:i+len(substring)] == substring:
            return True
    return False
string = "A geeks in need is a geek indeed"
substring = "geeks1234"
print(is_substring(string,substring))


#method 1
str1 = "geeksforgeeks"
str2 = ''
for i in str1:
    if i not in str2:
        str2 = str2+i
print(str2)


#method 2

import operator as op

str1 = "geeksforgeeks"
str2 = ''

for i in str1:
    if op.countOf(str2, i) > 0:
        pass
    else:
        str2 = str2+i
print(str2)













        




"""

