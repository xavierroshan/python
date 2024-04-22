#1 Python Counter| Find all duplicate characters in string
#method 1
from collections import Counter
input_str = 'geeksforgeeeks'
lst = list(input_str)
count = Counter(lst)
lst1 = []
for x, y in count.items():
    if y >1:
        lst1.append(x)
print(lst1)


#method 2
input_str = 'geeksforgeeeks'
lst = list(input_str)
dup_str = []
uni_str = []
for x in lst:
    if x not in uni_str:
        uni_str.append(x)
    else:
        dup_str.append(x)
print(set(dup_str))

#method 3
input_str = 'geeksforgeeeks'
lst = list(input_str)
lst1 = list(set(lst))
dup_list = []
for x in lst1:
    if lst.count(x)>1:
        dup_list.append(x)
print(dup_list)

#method 4
input_str = 'geeksforgeeeks'
lst = set(filter(lambda x: input_str.count(x)>1, input_str))
print(lst)


#2 Python program to find uncommon words from two Strings
#Input : A = “Geeks for Geeks”,  B = “Learning from Geeks for Geeks”
#Output : [‘Learning’, ‘from’]

#Input : A = “apple banana mango” , B = “banana fruits mango”
#Output : [‘apple’, ‘fruits’]

#method 1
input_A = 'apple banana mango'
input_B ='banana fruits mango'
lst_A = input_A.split(' ')
lst_B = input_B.split(' ')
set_A = set(lst_A)
set_B = set(lst_B)
print(set_A^set_B)

#method 2
input_A = 'apple banana mango'
input_B ='banana fruits mango'
lst_A = input_A.split(' ')
lst_B = input_B.split(' ')
uncomm_lst = []
for x in lst_A:
    if x not in lst_B:
        uncomm_lst.append(x)
for x in lst_B:
    if x not in lst_A:
        uncomm_lst.append(x)
print(uncomm_lst)

#method 3
from collections import Counter
input_A = 'apple banana mango'
input_B ='banana fruits mango'
lst = (input_A + ' ' + input_B).split(' ')
count = Counter(lst)
uncomm_lst = []
for x,y in count.items():
    if y ==1:
        uncomm_lst.append(x)
print(uncomm_lst)


#method 4
input_A = 'apple banana mango'
input_B ='banana fruits mango'
lst_A = input_A.split(' ')
lst_B = input_B.split(' ')
count_A = Counter(lst_A)
count_B = Counter(lst_B)
uncomm_lst = []
for x in count_A:
    if x not in count_B:
        uncomm_lst.append(x)
for x in count_B:
    if x not in count_A:
        uncomm_lst.append(x)
print(uncomm_lst)


#method 5
count = {}
input_A = 'apple banana mango'
input_B ='banana fruits mango'
lst_A = input_A.split(' ')
lst_B = input_B.split(' ')

for word in  lst_A:
    count[word]= count.get(word,0)+1
for word in lst_B:
    count[word]= count.get(word,0)+1
print([word for word in count if count[word]==1])


#Find length of a string in python (4 ways)

#Input : 'hello world !'
#Output : 13

#method 1
input_str = 'hello world !'
print(len(input_str))

#method 2
count=0
for x in input_str:
    count+=1
print(count)

#method 3
input_str = 'hello world !'
lst = list(input_str)
count=0
while lst:
    lst.pop(0)
    count+=1
print(count)

#method 4
input_str = 'hello world !'
count = 0
for x,y in enumerate(input_str):
    count+=1
print(count)

#method 4
input_str = 'hello world !'
print(sum(1 for x in input_str))



#Python program to print even length words in a string
#Input: s = "This is a python language"
#Output: This is python language

#method 1
input_str = 'This is a python language'
input_lst = input_str.split()
lst = []
for x in input_lst:
    if len(x)%2 ==0:
        lst.append(x)
print(lst)

#method 2
input_str = 'This is a python language'
input_lst = input_str.split()
lst = [x for x in input_lst if len(x)%2==0 ]
print(lst)


#method 3
input_str = 'This is a python language'
input_lst = input_str.split()
lst = list(filter(lambda x: len(x)%2==0, input_lst))
print(lst)


#method 4
input_str = 'This is a python language'
input_lst = input_str.split()
lst = [x for y,x in enumerate(input_lst) if len(x)%2==0 ]
print(lst)



#Find words which are greater than given length k
#Input : str = "hello geeks for geeks is computer science portal" 
#k = 4
#Output : hello geeks geeks computer science portal

#method 1
input_str = 'hello geeks for geeks is computer science portal'
k=4
lst = list(input_str.split())
lst1 = []
for x in lst:
    if len(x)>4:
        lst1.append(x)
print(lst1)

#method 2
input_str = 'hello geeks for geeks is computer science portal'
k=4
lst = list(input_str.split())
lst1 = [x for x in lst if len(x)>4]
print(lst1)


#method 3
input_str = 'hello geeks for geeks is computer science portal'
k=4
lst = list(input_str.split())
lst1 = list(filter(lambda x: len(x)>4, lst))
print(lst1)

#method 4
sentence = "hello geeks for geeks is computer science portal"
length = 4
s = sentence.split()
print([a for i, a in enumerate(s) if len(a) > length]) 
        
#Python program to check whether the string is Symmetrical or Palindrome


#Input: khokho
#Output: 
#The entered string is symmetrical
#The entered string is not palindrome

#Input:amaama
#Output:
#The entered string is symmetrical
#The entered string is palindrome


def palindrome(input_str):
    if input_str == input_str[::-1]:
        print("String is palindrom")
    else:
        print("String is not palindrome")
    
    
def symmetrical(input_str):
    if input_str[0:len(input_str)//2] == input_str[len(input_str)//2:]:
        print("String is symmetrical")
    else:
        print("String is not symmetrical")



input_str = 'khokho'
input_str = 'amaama'
palindrome(input_str)
symmetrical(input_str)    


#Python – Words Frequency in String Shorthands
#Input : test_str = 'Gfg is best' 
#Output : {'Gfg': 1, 'is': 1, 'best': 1} 



#method 1
def word_fr(test_str):
    test_lst = test_str.split()
    test_dict = {}
    for x in test_lst:
        test_dict[x]= test_dict.get(x,0)+1
    print(test_dict)




#method 2

from collections import Counter
def word_fr1(test_str):
    test_lst = test_str.split()
    test_count = Counter(test_lst)
    print(dict(test_count))
    
    
#method 3
def word_fr2(test_str):
    test_lst = test_str.split()
    test_set = set(test_lst)
    test_dict = {x:test_lst.count(x) for x in test_set}
    print(test_dict)


#method 3
def word_fr3(test_str):
    test_lst = test_str.split()
    test_dict = {}
    test_dict = {x:test_dict.get(x,0)+1 for x in test_lst}
    print(test_dict)



# driver code
test_str = 'Gfg is best' 
word_fr(test_str)
word_fr1(test_str)
word_fr2(test_str)
word_fr3(test_str)


#PPython – Replace all occurrences of a substring in a string

#Input : test_str = “geeksforgeeks” s1 = “geeks” s2 = “abcd” 
#Output : test_str = “abcdforabcd” Explanation : We replace all occurrences of s1 with s2 in test_str. 

#Input : test_str = “geeksforgeeks” s1 = “for” s2 = “abcd” 
#Output : test_str = “geeksabcdgeeks”
        
#method 1
test_str = 'geeksforgeeks' 
s1 = 'geeks'
s2 = 'abcd'
print(test_str.replace(s1,s2))

#method 2
test_str = 'geeksforgeeks' 
s1 = 'for'
s2 = 'abcd'
print(test_str.replace(s1,s2))


#method 3
import re
test_str = 'geeksforgeeks' 
s1 = 'geeks'
s2 = 'abcd'
print(re.sub(s1,s2, test_str))


#method 4
test_str = 'geeksforgeeks' 
s1 = 'geeks'
s2 = 'abcd'
for i in range(len(test_str)):
    if test_str[i:i+len(s1)] == s1:
        test_str = test_str[0:i]+s2+test_str[i+len(s1):]
print(test_str)



#String slicing in Python to Rotate a String

#Input : s = "GeeksforGeeks"
#        d = 2
#Output : Left Rotation  : "eksforGeeksGe" 
#         Right Rotation : "ksGeeksforGee"  


#Input : s = "qwertyu" 
#        d = 2
#Output : Left rotation : "ertyuqw"
#         Right rotation : "yuqwert"

#method 1

s = "GeeksforGeeks"
l = list(s)
n = len(s)
d=2
for i in range(d): 
    k = l[n-1] 
    for i in range(n-2, -1,-1):
        l[i+1]=l[i]
    l[0]=k
print(''.join(l))
    
s = "GeeksforGeeks"
l = list(s)
n = len(s)
d=2
for i in range(d): 
    k = l[0] 
    for i in range(0, n-1):
        l[i]=l[i+1]
    l[n-1]=k
print(''.join(l))
    


#method 2
s = "GeeksforGeeks"
d =2
l = list(s)
for i in range(d): 
    x=l.pop(0)
    l.append(x)
print(''.join(l))



s = "GeeksforGeeks"
d = 2
l = list(s)
for i in range(2): 
    x=l.pop()
    s= x+''.join(l)
    l = list(s)
print(s)

#method 3
s = "GeeksforGeeks"
l = list(s)
n = len(s)
d=2
s_f = s[d:] + s[:d]
print(s_f)


s = "GeeksforGeeks"
l = list(s)
n = len(s)
d=2
s_f = s[-d:]+s[:-d]
print(s_f)

#method 3
from collections import deque

def rotate(s, d):
    deq = deque(s)
    if d>0: 
        deq.rotate(-d)
    else:
        deq.rotate(abs(d))
    return ''.join(deq)



#driver code
s = "GeeksforGeeks"
d = -2
print(rotate(s,d))


#Python | Check if a given string is binary string or not
#Input: str = "01010101010"
#Output: Yes

#Input: str = "01010101abc0"
#Output: No

#method 1
input_str = str = "01010101010"
flag = 0
for i in input_str:
    if i not in "01":
        flag = -1
        
if flag == 0: 
    print("String is binary")
else:
    print("String is not binary")
    
#method 2
input_str = str = "01010101abc0"
count = 0
for i in input_str:
    if i == '0' or i == '1':
        count+=1
if len(input_str) == count:
    print("String is binary")
else:
    print("String is not binary")
    
    
#method 3
input_str = str = "010101010"
if len(input_str) == input_str.count('0') + input_str.count('1'):
    print("String is binary")
else:
    print("String is not binary")
    
#method 4
s = "010101010"
for x in "01":
    s = s.replace(x,'')
if len(s)==0:
    print("String is binary")
else:
    print("String is not binary")
    
    
#method 5
s = "010101010"
flag =0
try:
    int(s, 2)
except ValueError:
    flag = -1
if flag == -1:
    print("String is not binary")
else:
    print("String is binary")
    
    
#method 6
s = "01010ab1010"
print(all((l in '01') for l in s))

#method 7

import re
s = "010101010"
match = re.search('[^01]', s)
if match:
    print("String is not binary")
else:
    print("String is binary")
    



#Generating random strings until a given string is generated
import random
import string
str1 = 'ros'
length = 3
char = string.ascii_letters
count = 0
str2=''
while str1!=str2: 
   str2=''.join(list((random.choice(char) for x in range(length))))
   count+=1 
print(count, str2, str1)


#Python | Count the Number of matching characters in a pair of string
#Input : str1 = 'abcdef'
#        str2 = 'defghia'
#Output : 4 
#(i.e. matching characters :- a, d, e, f)

#Input : str1 = 'aabcddekll12@'
#        str2 = 'bb22ll@55k'
#Output : 5 
#(i.e. matching characters :- b, 1, 2, @, k)

#method 1
str1 = 'aabcddekll12@'
str2 = 'bb22ll@55k'
count = 0
match = []
for x in str1:
    if x in str2 and x not in match:
        count+=1 
        match.append(x)
print(count, match)



#method 2
str1 = 'aabcddekll12@'
str2 = 'bb22ll@55k'
set_1 = set(str1)
set_2 = set(str2)
set_int = (set_1 & set_2)
print(len(set_int), set_int)



# Python3 code to demonstrate working of 
# Replace multiple words with K 
# Using join() + split() + list comprehension 


import re
# initializing string 
test_str = 'Geeksforgeeks is best for geeks and CS'
word_list = ["best", 'CS', 'for'] 
repl_wrd = 'gfg'
for x in word_list:
    test_str = re.sub(x, repl_wrd, test_str)
print(test_str)

import re
# initializing string 
test_str = 'Geeksforgeeks is best for geeks and CS'
word_list = ["best", 'CS', 'for'] 
repl_wrd = 'gfg'
print(' '.join([repl_wrd if x in word_list else x for x in (test_str.split(' '))]))













    
         














    

     


