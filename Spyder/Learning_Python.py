"""
# split()

str = "my name is roshan"
list1 = str.split()
print(list1)

date = "2023-11-27"
list1 = date.split("-")
print(list1)

time = "12:30:45"
hour, minute,second = time.split(':')
print(hour, minute, second)

csv_data = 'roshan, deepa, vincent, danile'
personal_info = csv_data.split(',')
print(personal_info)

sample = 'this is a sample sentance'
sample1 = sample.split(' ', 2)
print(sample1)

# splitting and stripping white spaces
sample = "   this is a great opportunity for us  "
sample1 = sample.split()
print(sample1)
"""

"""
a = input("Enter your name")
print(a)
b= int(input("Enter yor age:"))
print(b)
c = float(input("Enter your salary:"))
print(c)



while True: 
    try: 
        age = int(input("Enter integer value:"))
        break
    except ValueError:
        print("Enter the correct input type")
        
print(f"My age is{age}")


arr = input("Enter two numbers separated by a space").split()
num1, num2 = map(float,arr)
print (num1, num2)



x,y = [int(x) for x in input("Enter two values:").split()]
print(x,y)



x = [int(x) for x in input("Enter multiple values:").split()]
print(x)

from getpass import getpass
username = input("Enter your username:")
password = getpass("Enter your password")
print(username, password)


# eval()
exp = '2+4+6**8+4^3'
result = eval(exp)
print(result)
x = 2+4+6**8+4^3
print(x)


# Execute code with eval function




def execute_code():
    code_to_execute = input("Enter Python code to execute: ")
    result = eval(code_to_execute)
    print("Result:", result)

execute_code()


print("select an option")
print("1. Option1")
print("2. Option2")
choice = input("enter your choice:")
print(f"your choice is {choice}")


def get_user_input(prompt):
    return (prompt)


username = get_user_input(input("Enter username:"))
print(username)


#Interactive Loop with Exit Option:
while True:
    action = input("Enter quit or exit to exit the loop:")
    if action == 'quit' or action =='exit':
        break
    else:
        print("continue")


print("exited the loop")



a,b = 10,20
print("the first number is a, {} and the second number is b, {}".format(a,b))



for i in range(10):
    print(i, end=" ")
print("\n")
for i in reversed(range(10)):
    print(i, end=" ")


import time
count_time = 3
for i in reversed(range(count_time+1)):
    if i >0:
        time.sleep(1)
        print(i,">>>", end="")
    else:
        time.sleep(1)
        print("start")
        time.sleep(1)


import time
 
count_seconds = 3
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end='>>>', flush = True)
        time.sleep(1)
    else:
        print('Start')
        


import io
dummy_file = io.StringIO()
print("my name is roshan", file=dummy_file)
print(dummy_file.getvalue())



print("geek for geeks", file= open("textfile.txt", "w"))




arr = [1,2,3,4,5,6,7,8,9]
print(*arr)


import sys 
sys.stdout.write("Geek for Geeks")
sys.stdout.write("the best python training")


print("04", "02", "1980", sep="-" )
print("17", "02", "2023", sep="-" )



# string modulo operator

name= "roshan xavier" 
age = 34
salary = 3000.0

print("my name is {}, and my age is {} and i earn {}".format(name, age, salary))
print(f"my name is {name}, and my age is {age} and i earn {salary}")
print()
print("my age is %2d" % 1200000)
print("my salary is %2.2f" % 3000)
print("my name is")
print("my name is {0}, and my age is {1} and i earn {2}".format(name, age, salary))
print("my name is {0}, and my age is {2} and i earn {1}".format(name, age, salary))



print(f"i am {name} my age is {age} and I earn {salary}")
print("i am {} my age is {} and I earn {}".format(name, age, salary))
print("i am {0} my age is {1} and I earn {2}".format(name, age, salary))
print("I earn {2},my age is {1} and my name is {0}".format(name, age, salary))
print("my age is {0:2d} and my salary is {1:5.2f}".format(age, salary))
print("i am {name} my age is {age} and I earn {salary}".format(name="deepa", age="36", salary=4000.00))
cstr = "i love GeeksforGeeks"
print(cstr.center(40, "#"))
print(cstr.ljust(40,"="))
print(cstr.rjust(40, "+"))
dict1= {"name":"roshan", "age": 43, "salary":3000.00}
print("my name is {name}, my age is {age} and salary is {salary}".format(**dict1))

# combining positional and keyword arguments
print('Number one portal is {0}, {1}, and {other}.'
     .format('Geeks', 'For', other ='Geeks'))
print("my name is {name} and age is {age} and salary is {salary}"
      .format(name ="roshan", age=34, salary=3000))

print("Geeks :{0:2d}, Portal :{1:8.2f}".
      format(12, 00.546))
 
# Changing positional argument
print("Second argument: {1:3d}, first one: {0:7.2f}".
      format(47.42, 11))
 
print("Geeks: {a:5d},  Portal: {p:8.2f}".
     format(a = 453, p = 59.058))


cstr = "I love geeksforgeeks"
 
# Printing the center aligned string with fillchr
print("Center aligned string with fillchr: ")
print(cstr.center(40, '#'))
 
# Printing the left aligned string with "-" padding
print("The left aligned string is : ")
print(cstr.ljust(40, '-'))
 
# Printing the right aligned string with "-" padding
print("The right aligned string is : ")
print(cstr.rjust(40, '-'))


tab = {'geeks': 4127, 'for': 4098, 'geek': 8637678}
 
# using format() in dictionary
print('Geeks: {0[geeks]:d}; For: {0[for]:d}; '
    'Geeks: {0[geek]:d}'.format(tab))
 
data = dict(fun ="GeeksForGeeks", adj ="Portal")
 
print("I love {fun} computer {adj}".format(**data))




a=5
b=2 
print(a is b)
print(a is not b)
a, b = 4,5
x = a if a>b else b
print(x)
y = [x for x in range(10) if x%2 ==0]
print(y)
a, b = 4,4
print("Both a and b are equal" if a==b else "a and b are not equal")



a, b = 10, 20

print((b,a)[a < b])


class Myclass:
    
    def __init__(self, value):
        self.value=value
    def __truediv__(self, other):
        return Myclass(self.value and other.value )

a = Myclass(True)
b = Myclass(False)
c=a/b
print(a.value)
print(b.value)
print(c.value)


class Myclass:
    
    def __init__(self, value):
        self.value=value
    def __add__(self, other):
        return Myclass(self.value + other.value )

a = Myclass(5)
b = Myclass(7)
c=a+b
print(c.value)


class Myclass:
    def __init__(self,value):
        self.value=value
    def __sub__(self,other):
        return Myclass(self.value-other.value)
a = Myclass(5)
b = Myclass(7)
c=a-b
print(c.value)

class Myclass:
    def __init__(self, value):
        self.value = value
    def __mul__(self, other):
        return Myclass(self.value*other.value)
a = Myclass(5)
b = Myclass(7)
c=a*b
print(c.value)


#Operator overloading
class Myclass:
    
    def __init__(self, value):
        self.value=value
    def __add__(self, other):
        return (self.value + other.value )

a = Myclass(5)
b = Myclass(7)
c=a+b
print(c)

x= Myclass("Geek")
y= Myclass("for Geeks")
z=x+y
print(z)

print(Myclass.__add__(a,b))
print(Myclass.__add__(x,y))


class Myclass:
    
    def __init__(self, value):
        self.value=value
    def __gt__(self, other):
        if self.value > other.value :
            return True
        else:
            return False
        
a=Myclass(7)
b=Myclass(6)
print(a>b)



print(any([False, False, False]))
print(any([True, False, False]))
print(any([True, True, True]))
print(all([False, False, False]))
print(all([False, True, False]))
print(all([True, True, True]))


list1 = []
list2 = []
for i in range(1,11):
    list1.append(4*i)
    
for i in range(0,10):
    list2.append(list1[i]%5==0)
print(any(list2))

list1 = []
list2 = []
for i in range(1,11):
    list1.append(4*i)
    
for i in range(0,10):
    list2.append(list1[i]%4==0)
print(list1)
print(list2)
print(all(list2))


import operator
print(operator.add(4,3))
print(operator.sub(4,3))
print(operator.mul(4,3))
print(operator.pow(4,3))
print(operator.truediv(4,3))
print(operator.floordiv(4,3))
print(operator.mod(4,3))
print(operator.lt(4,3))
print(operator.gt(4,3))
print(operator.le(4,3))
print(operator.ge(4,3))


import operator
arr = [1,2,3,4,5,6,8,9]
operator.setitem(arr, 1, 200)
print(arr)
operator.delitem(arr,2)
print(arr)
print(operator.getitem(arr, 5))
operator.setitem(arr, slice(2,3), [100,200])
print(arr)
operator.delitem(arr, slice(2,3))
print(arr)
print(operator.getitem(arr, slice(2,4)))
arr = "geek"
arr_1= "forgeeks"
print(operator.concat(arr, arr_1))
print(operator.contains(arr_1, arr))



arr1 = []
arr2 = []
arr3 = arr1
print(id(arr1))
print(id(arr2))
print(id(arr3))
print(arr1 == arr2)
print(arr1 is arr2)
print(arr1 is arr3)
print(arr1 == arr3)



list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]

for item in list1:
    if item in list2:
        print("overlapping")
    else:
        print("not overlapping")

        
x = 24
y = 20
list = [10, 20, 30, 40, 50]
if x in list:
    print(f"{x} is in list")
else:
    print(f"{x} is not in list")
if y in list:
    print(f"{y} is in list")
else:
    print(f"{y} is not in list")

     

# Python program to illustrate the use
# of 'is' identity operator
x = 5
y = 5
print(x is y)
print(id(x))
print(id(y))
 


x = "Hello World"
print(type(x))
x = 50
print(type(x))
x = 60.5
print(type(x))
x = 3j
print(type(x))
x = ["geeks", "for", "geeks"]
print(type(x))
x = ("geeks", "for", "geeks")
print(type(x))
x = range(10) 
print(type(x))
x = {"name": "Suraj", "age": 24}
print(type(x))
x = {"geeks", "for", "geeks"}
print(type(x))
x = frozenset({"geeks", "for", "geeks"})
print(type(x))
x = True
print(type(x))
x = b"Geeks"
print(type(x))
x = bytearray(4)
print(type(x))
x = memoryview(bytes(6))
print(type(x))
x = None
print(type(x))

 
 
String1 = 'Welcome to the Geeks World'
print(String1)

String1 = "I'm a Geek"
print("\nString with the use of Double Quotes: ")
print(String1)
print(type(String1))



String1 = '''I'm a Geek and I live in a world of "Geeks"'''
print("\nString with the use of Triple Quotes: ")
print(String1)
print(type(String1))
 
String1 = '''Geeks 
            For 
            Life'''
print("\nCreating a multiline String: ")
print(String1)
String2 = '''Geeks
             for
             geeks
             kkksksk
             '''
print(String2)


List = []
print("Initial blank List: ")
print(List)



List = ['GeeksForGeeks']
print("\nList with the use of String: ")
print(List)

List = ["Geeks", "For", "Geeks"]
print("\nList containing multiple values: ")
print(List[0])
print(List[2])
List = [['Geeks', 'For'], ['Geeks']]
print("\nMulti-Dimensional List: ")


tuple = ()
print(tuple)
tuple = ("Geek", "Geeks")
print(tuple)
tuple1 = (1,2,3)
tuple2 = ('a','b','c')
print(tuple1)
print(tuple2)
tuple3 = (tuple1, tuple2)
print(tuple3)
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[-1])
print(List)




set1 = set()
print("Initial blank Set: ")
print(set1)
set1 = set("GeeksForGeeks")
print("\nSet with the use of String: ")
print(set1)


print("\nSet with the use of String: ")
print(set1)

set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of List: ")
print(set1)

set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values")
print(set1)


set1 = {"Geeks", "For", "Geeks"}
print(set1)

for x in set1:
    print(x)

    
dict1 = dict()
print(dict1)
dict1={1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(dict1)
dict1 = dict([(1,"Geek"), (2,"for"), (3,"Geeks")])
print(dict1)


dict1 = {"Alice": {"math":95, "Science":85, "Arts": 90}, "Bob": {"math":99, "Science":80, "Arts": 92}}
print(dict1["Alice"])
print(dict1.get("Alice", {}))
print(dict1.get("Charles", {}))
grade=dict1.get("Charles", {})
grade['math']= 99
print(grade)
print(dict1)

print(dict1.setdefault("Charles", {}))
print(dict1)
dict1['Charles']={"math":98, "Science":90, "Arts": 92}
print(dict1)




arr = [1,2,3,5,4,7,6]
print(arr)
arr.sort(reverse=False)
print(arr)
arr.sort(reverse=True)
print(arr)
arr1 = sorted(arr, reverse=True)
print(arr1)
arr1 = sorted(arr, reverse=False)
print(arr1)
arr = "geekforgeeks"
print(arr[::-1])
print(arr)
arr =[arr]
print(arr)
print(arr[0])
arr = [1,2,3,5,4,7,6]
arr.reverse()
print(arr)


    
arr = ["my","name", "is","anthony","golzalvas"]
print(arr)
str = ' '.join(arr)
print(str)
tuple1 = ("my","name", "is","anthony","golzalvas")
print(tuple1)
str = ' '.join(tuple1)
print(str)
str1 = str.split()
print(str1)
str2 = ''.join(str1)
print(str2)
str3 = '-'.join(str2)
print(str3)
str4 =''.join(reversed(str2))
print(str4)
str5=reversed(str2)
print(str5)

    
String1 = "My name"
print(String1) 
String2 = " is roshan"
print(String1+String2)
String3 = String1[0:]+String2[-5:-1]
print(String3)
String1 = "roshan xavier"
print(String1[:])
del String1
print(String1)


String1 = '''I'm a "Geek"'''
print(String1) 
String1 = '''I'm a          
      "Geek"'''        
print(String1 )
String1  ="im a a \"Geek\""
print(String1)
String1 = "C://users/roshan/desktop/test"
print(String1)
String1 = r"C://users/roshan/desktop/test"
print(String1)
String1 = R"C://users/roshan/desktop/test"
print(String1)
String1 = "C:\\Users\roshan\desktop\test"
print(String1)
String1 = r"C:\\Users\roshan\desktop\test"
print(String1)
String1 = "C:\\\\Users\\roshan\\desktop\\test"
print(String1)
String1="roshan\nxavier"
print(String1)
String1="roshan\txavier"
print(String1)



# String alignment 
String1 ="|{0:<10}|{0:^10}|{0:>10}|".format("roshan", "deepa", "vincent")
print(String1)

    
    
String = 'GEEKSFORGEEKS'
 
# Using indexing sequence
print(String[0:14:2])
print(String[-1:-14:-2])


String = 'GEEKSFORGEEKS'
print(String.slice(3,10))

    
# reverse string 1

String = 'GEEKSFORGEEKS'
String2 = ''
for i in String:
    String2  = i+String2
print(String2)

# reverse string 2

String = 'GEEKSFORGEEKS'
String1=String[::-1]
print(String1)

# reverse string 3
String ='GEEKSFORGEEKS'
String1 = ''.join(reversed(String))
print(String1)

# reverse string 4
String ='GEEKSFORGEEKS'
String=list(String)
print(String)
String.reverse()
print(''.join(String))

# reverse string 5
String= 'GEEKSFORGEEKS'
list = [String[i] for i in range(len(String)-1,-1,-1)]
print(''.join(list))

# reverse string 6
def reverse_string(String):
    n=len(String)
    arr = list(String)
    arr1=[]
    for i in range(n):
        arr1.append(arr.pop())
    print( ''.join(arr1))

String="GeekforGeeks"
reverse_string((String))

# reverse string 7
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
 
 
s = "Geeksforgeeks"
print(reverse(s))     


import re
match = re.search('portal', 'GeeksforGeeks: A computer science portal for geeks') 
print(match)
print('start index:', match.start())
print('End index', match.end())
x='GeeksforGeeks: A computer science portal for geeks'

match = re.findall('Geek', 'GeeksforGeeks: A computer science portal for gGeks')
print(match)

import re

match = re.search('roshan', 'roshanxavier')
print(match.start())
print(match.end())


match = re.findall('r', 'roshanxavier')
print(match)

match = re.search('[A-Za-z0-9]', '099876')
print(match)
print(match.start())
print(match.end())

match = re.search('[^A-Za-z]', 'r')
print(match)

match = re.search('Gee[a-z][a-z]', 'GeekforGeeks')
print(match)

match = re.findall('Gee[a-z][a-z]', 'GeekforGeeks')
print(match)


match = re.search('\AG', 'GeekforGeeks')
print(match)


match = re.search('\w', 'GeekforGeeksG')
print(match)

match = re.search('\W', '$GeekforGeeksG')
print(match)

match = re.search('\s', ' GeekforGeeks')
print(match)

match = re.search('\s', 'GeekforGeeks')
print(match)

match = re.search('\S', 'GeekforGeeks')
print(match)

match = re.search('\S', ' GeekforGeeks')
print(match)

match = re.search('ks\Z',' GeekforGeeks')
print(match)

match = re.search('\d',  '9GeekforGeeks')
print(match)

match = re.search('\d',  'GeekforGeeks')
print(match)

match = re.search('\D', 'GeekforGeeks')
print(match)


match = re.search(r'eks\b', 'GeekforGeeks')
print(match)

match = re.search(r'\bGee', 'GeekforGeeks')
print(match)


import re 


  
  
# Beginning of String 
match = re.search(r'^Geek', 'Campus Geek of the month') 
print('Beg. of String:', match) 
  
match = re.search(r'^Geek', 'Geek of the month') 
print('Beg. of String:', match) 
  
# End of String 
match = re.search(r'Geeks$', 'Compute science portal-GeeksforGeeks') 
print('End of String:', match) 

import re

match = re.search(r'P.T.O.', 'PYTHON')
print(match)
match = re.search(r'P.....', 'PYTHON')
print(match)

match = re.search(r'colo?r', 'color')
print(match)
match = re.search(r'colo?r', 'colour')
print(match)

# repetetion date pattern dd-mm-yyy
match = re.search(r'\d{2}-\d{2}-\d{4}', '20-04-1980')
print(match)
print(match.group())

#phone pattern 437-988-0199 or 437-9880-199
match = re.search(r'\d{3}-\d{3,4}-\d{3,4}', '437-988-0199')
print(match)
print(match.group())
match = re.search(r'\d{3}-\d{3,4}-\d{3,4}', '437-9880-199')
print(match)
print(match.group())



match = re.search(r'(\d{2})-(\d{2})-(\d{4})','26-08-2020') 
print(match.group(3))
print(match.groups())

import re

match = re.search(r'(?P<dd>\d{2})-(?P<mm>\d{2})-(?P<yyy>\d{4})', '26-08-2020')
print(match.group('mm'))



match = re.search(r'(?P<dd>\d{2})-(?P<mm>\d{2})-(?P<yyy>\d{4})','26-08-2020' )
print(match.group('mm'))
print(match.groupdict())

arr = [1,2,3,4]
arr1 = ["my", "name", "is", "roshan"]
arr.extend(arr1)
print(arr)
arr.append(arr1)
print(arr)
arr1.insert(2,0)
print(arr1)
arr1.insert(0, "xavier")
print(arr1)
arr1.remove("xavier")
print(arr1)
arr1.pop(3)
print(arr1)
print(arr1.index("roshan"))
arr1.extend(["roshan", "roshan"])
print(arr1.count("roshan"))
arr2 = arr1.copy()
print(arr2)
arr2.clear()
print(arr2)

arr = [1,2,3,4]
arr1 = [4,5,6,7]
print(sum(arr))
print(max(arr))
print(min(arr))


arr = ["apple", "bannana", "orange"]
for x,y in enumerate(arr):
    print(x,y)
    
    # filter in python

    def is_even(num):
        return num%2 ==0


    arr1 = [0,1,2,3,4,5,6,7,8,9,10]
    arr2 = filter(is_even, arr1)
    arr2 = list(arr2)
    print(arr2)


    def is_negative(num):
        return num<0


    arr1 = [0,1,2,3,4,5,6,7,8,9,10,-6]
    arr2 = filter(is_negative, arr1)
    arr2 = list(arr2)
    print(arr2)
    
    
# filter in python

def is_even(num):
    return num%2 ==0


arr1 = [0,1,2,3,4,5,6,7,8,9,10]
arr2 = filter(is_even, arr1)
arr2 = list(arr2)
print(arr2)


def is_negative(num):
    return num<0


arr1 = [0,1,2,3,4,5,6,7,8,9,10,-6]
arr2 = filter(is_negative, arr1)
arr2 = list(arr2)
print(arr2)

numbers = [1, 2, 3, 4, 5]
string_numbers = map(str, numbers)
result_list = list(string_numbers)
print(result_list)

numbers = [1, 2, 3, 4, 5]
number_square = map(lambda x: x**2, numbers)
print(list(number_square))

numbers = ["roshan", "xavier", "deepa", "joseph"]
number_reverse = map(lambda x: x[::-1], numbers)
print(list(number_reverse))

numbers = [1, 2, 3, 4, 5]
number_div = map(lambda x: x%2==0, numbers)
print(list(number_div))

num = 5
number_sq = map(lambda x:x**2, range(0,5))
print(list(number_sq))


import math
num = [25,64,121,625]
num_sqrt = map(math.sqrt, num)
print(list(num_sqrt))


words = ['apple', 'banana', 'cherry']
letter_count= map(lambda x:len(x), words)
print(list(letter_count))

words = ['apple', 'banana', 'cherry']
capitalize = map(lambda x:x.capitalize(), words)
print(list(capitalize))


numbers = [1, 2, 3]
words = ['apple', 'banana', 'cherry']
enum = map(lambda x,y: (x,y), numbers, words)
print(list(enum))

number1 = [1, 2, 3]
number2 = [6,5,4]
enum = map(lambda x,y: x+y, number1, number2)
print(list(enum))   


# Yield in Python

def range_list(r1,r2):

    while r1 <= r2:
        yield(r1)
        r1+=1
        
        
# range        
for value in range_list(0,9):
    print(value) 
    
    r1 = 10
    r2 = 20

    while r1 < r2:
        print(r1)
        r1+=1
        


def print_range(r1,r2):
        while r1 < r2:
            arr.append(r1)
            r1+=1
        return(arr)

r1 = 10
r2 = 20
arr = []
print(*print_range(r1,r2))
    
    
import itertools

r1 = 10
r2 = 20

y = itertools.chain(range(r1, r2))
print(list(y))


##########Example of recursion####################
def create_list(r1, r2, lst):
    # Base case: if r1 is equal to r2, return the list
    if r1 == r2+1:
        return lst
    # Otherwise, append r1 to the list and call the function again with r1 + 1
    else:
        lst.append(r1)
        return create_list(r1 + 1, r2, lst)
    ##########Example of recursion##############################Example of recursion####################
    
# Define a function to count the number of elements in a list using recursion
def count_elements_recursion(lst):
    # Base case: if the list is empty, return 0
    if not lst:
        return 0
    # Recursive case: add 1 to the count of the remaining elements in the list
    return 1 + count_elements_recursion(lst[1:])
 
 
# Test the function with a sample list
lst = [1, 2, 3, 4, 5]
print("The length of the list is:", count_elements_recursion(lst))
 
# Output: The length of the list is: 5
##########E##########E##########E##########E##########E##########E

test_list = [1, 4, 5, 6, 7]

y=[(i, test_list[i]) for i in range(0, len(test_list))]
print(list(y))

for x,y in enumerate((test_list)):
    print(x,y)
    
for index, value in  zip(range(len(test_list)),test_list):
    print(index, value)
    
test_list = [1, 4, 5, 6, 7]
list_len = sum(1 for i in test_list)
print(list_len)
print(sum(1 for i in test_list))

            
#method 1
arr = [1,4,3,5,6,7,8,10]
x=100
if x in arr:
    print(x)
else:
    print("not in array")
    
    
#method 2  
arr = [1,4,3,5,6,7,8,10]   
x=100 
count=0
for i in arr:
    if i == x:
        print(x)
        break
    else:
        count+=1
if count == len(arr):
    print("not in array")
    

#method 3

try: 
    arr = [1,4,3,5,6,7,8,10]   
    x=10
    lst = [i for i in arr if i == x]
    print(lst.pop())
except:
    print("Error: not in the list")
    

#method 4

arr = [1,4,3,5,6,7,8,10]   
x=10
count = arr.count(x)
if count >=1:
    print("exists")
else:
    print("doesnt exist")
    
    

#method 5
arr = [1,4,3,5,6,7,8,10]   
x=100
try: 
    if arr.index(x) >= 0:
       print("exists")
except:
    print("does not exist")
    
    
#method 5
arr = [1,4,3,5,6,7,8,10]   
x='100'
arr = list(map(str,arr))
arr = ''.join(arr)
print(arr)
index=arr.find(x)
print("Index", index)
if index >=0:
    print("exists")
else:
    print("does not exist")
    
#clearing the list
lst = [1,2,3,4,5]
lst.clear()
print(lst)


lst = [1,2,3,4,5]
lst*=0
print(lst)


lst = [1,2,3,4,5]
del lst[:]
print(lst)

lst = [1,2,3,4,5]
n = len(lst)
for i in range(n):
    lst.pop()
print(lst)


#reversing 1
def reversing_list(arr):
    l, r = 0, len(arr)-1
    while l<r:
        arr[l], arr[r]=arr[r], arr[l]
        l+=1
        r-=1
    return(arr)
arr = [1,2,3,4,5,6]

print(reversing_list(arr))


#reversing 2
def reversing_list1(arr):
    arr1 = []
    for i in range(0, len(arr)):
        arr1.append(arr.pop())
    return arr1
        
arr = [1,2,3,4,5,6]
print(reversing_list1(arr))


#reversing 3
def reversing_list1(arr):
    arr1 = []
    for i in range(0, len(arr)):
        arr1.insert(0,arr[i])
    return arr1
        
arr = [1,2,3,4,5,6]
print(reversing_list1(arr))

#################################recursive####################################
# Python program to remove given element from the list
#defining recursive function to remove element
def remove_element(begin,oldlist,value,newlist):
if begin==len(oldlist): #base condition
	return newlist
if value !=oldlist[begin]: #check is element is not specified value
	newlist.append(oldlist[begin])
return remove_element(begin+1,oldlist,value,newlist) #recursive call

lst = [1, 9, 8, 4, 9, 2, 9]
value=9
# Printing initial list
print("Original list:", lst)


# Using recursive approach to remove the element
result = remove_element(0,lst,value,[])


# Printing list after removal
print("List after element removal:", result)
#This code is contributed by tvsk
#################################recursive####################################

lst = [1,2,3,4,5,6]
lst.remove(4)
print(lst)
set1 = set(lst)
set1.discard(5)
print(list(set1))
lst = [1,2,3,4,5,6]
x = 5
print([i for i in lst if i!=x ])
lst = [1,2,3,4,5,6]
x = 5
y = filter(lambda i: i != x, lst)
print(list(y))

#concat 1
lst1 = ["Geek", "for", "Geeks"]
lst2 = ["-Geek", "f-or", "G-eeks"]
lst3 = []

for i in range(0,len(lst1)):
    lst3.append(lst1[i]+lst2[i])
print(lst3)

#concat 2

print([i+j for i,j in zip(lst1,lst2)])

lst1 = ["Geek", "for", "Geeks"]
lst2 = ["-Geek", "f-or", "G-eeks"]

x =map(lambda i, j: i + j, zip(lst1, lst2))


print(list(x))


### Dictionary
# Defining dictionary
dict1 = {}
print(dict1)
dict1 = {1:"roshan", 2:"deepa", 3:"vincent", 4:"danile"}
print(dict1)
dict1 = dict([(1,"roshan"), (2,"deepa"), (3,"vincent")])
del dict1[1]

print(dict1)


# Adding elements to the dictionary
dict1 ={}
dict1["name"] = "roshan"
dict1["address"] = {"house no": 251, "Street": "Livery Street", "City": "Stittsville", "zip": "K2V )A5"}



# Accessing elements to the dictionary
print(dict1)
print(dict1["name"])
print(dict1.get("address", "default address"))
print(dict1.get("address", {}))


# Adding elements to the dictionary
dict1 ={}
dict1["name"] = "roshan"
dict1["address"] = {"house no": 251, "Street": "Livery Street", "City": "Stittsville", "zip": "K2V )A5"}



# Accessing elements to the dictionary
print(dict1)
print(dict1["name"])
print(dict1.get("address", "default address"))
print(dict1.get("address", {}))

# items in dictionary
for x,y in dict1.items():
    print(x,y)
    
#copy, keys, values, pop  
dict2 = dict1.copy()
print(dict2)
dict2.clear()
print(dict2)
print(dict1.keys())
print(dict1.values())

dict1 = {1:"roshan", 2:"deepa", 3:"vincent", 4:"daniel"}
print(dict1)
dict1.popitem()
print(dict1)
dict1.pop(1)
print(dict1)

#set default, 
dict1 = {1: "roshan", 2: "deepa", 3: "vincent"}
dict1.setdefault(4, None)
print(dict1)

#set default, 
dict1 = {1: "roshan", 2: "deepa", 3: "vincent"}
dict1.setdefault(4, None)
print(dict1)

#length
dict1 = {1: "roshan", 2: "deepa", 3: "vincent"}
print(len(dict1))     


# Merging two dictionaries

dict1 = {1:"roshan", 2:"deepa"}
dict2 =  {3:"vincent", 4:"daniel"}
dict1.update(dict2)
print(dict1)


# Merging to lists to dic
roll_no = [10, 20, 30, 40, 50]
names = ['Ramesh', 'Mahesh', 'Kamlesh', 
         'Suresh', 'Dinesh']

dict1 = dict(zip(roll_no,names))
print(dict1)

#converting list to dictionary

vegetables = ['Carrot', 'Raddish','Brinjal', 'Potato']
print(dict(enumerate(vegetables)))


#Merge using operator
veg1 = {0: 'Carrot', 1: 'Raddish'}
veg2 = {2: 'Brinjal', 3: 'Potato'}
veg3 = (veg1 | veg2)
print(veg3)
veg1|=veg2
print(veg1)


#Accesing key and values
dict1 = {1: "roshan", 2: "deepa", "son": "vincent"}
for i in dict1:
    print(i, dict1[1])
    
#comprehension
print([(k,v) for k,v in dict1.items()])
print([(k, dict1[k]) for k in dict1])
print([i for i in enumerate(dict1.items())])


# delete a dictionary
dict1 = {1: "roshan", 2: "deepa", "son": "vincent"}
del dict1[1]
print(dict1)
del dict1
print(dict1)






#update
dict1 = {1: "roshan", 2: "deepa", 3: "vincent"}
dict1.update({4:"Daniel"})
print(dict1)


# Adding to a dictionary

D = {} 
 
L = [['a', 1], ['b', 2], ['a', 3], ['c', 4]]

for i in range(len(L)):
    if L[i][0] in D:
        D[L[i][0]].append(L[i][1])
    else:
        D[L[i][0]] = []
        D[L[i][0]].append(L[i][1])
print(D)



D = {} 
 
L = [['a', 1], ['b', 2], ['a', 3], ['c', 4]]
D['a']= []
D['a'].append(1)
print(D)
D['b']= []
D['b'].append(2)
print(D)
D['c']=[]
D['c'].append(4)
print(D)
D['a'].append(3)
print(D)

#########################################################

# Key to be added
key_ref = 'More Nested Things'
my_dict = {
    'Nested Things': [{'name', 'thing one'}, {'name', 'thing two'}]
}
 
# Value to be added
my_list_of_things = [{'name', 'thing three'}, {'name', 'thing four'}]
 
# try-except to take care of errors
# while adding key-value pair
try:
    my_dict[key_ref].append(my_list_of_things)
     
except KeyError:
    my_dict = {**my_dict, **{key_ref: my_list_of_things}}
     
print(my_dict)

#########################################################



###Python Control flow
for letter in 'geeksforgeeks':
 
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)
    
print('\n') 
    
for letter in 'geeksforgeeks':
 
    # break the loop as soon it sees 'e'
    # or 's'
    if letter == 'e' or letter == 's':
        break
 
print('Current Letter :', letter)

print('\n') 



for letter in 'geeksforgeeks':
 
    # break the loop as soon it sees 'e'
    # or 's'
    if letter == 'e' or letter == 's':
        break
 
    print('Current Letter :', letter)
    
# An empty loop
for letter in 'geeksforgeeks':
    pass
print('Last Letter :', letter)

count = 0
while (count < 3):
    count = count + 1
    print("Hello Geek")
print(count)


a = [1,2,3,4,5]

while a:
    print(a.pop())
    
    
# Prints all letters except 'e' and 's'
a = 'geeksforgeeks'
i=0
while i < len(a):
    if a[i]=='e' or a[i]=='s':
        i+=1
        continue
    else:
        print(a[i])
        i+=1
        
        
        
    
    


# break the loop as soon it sees 'e'a = 'geeksforgeeks'
a='geeksforgeeks'
i=0
while i < len(a):
    if a[i]=='e':
        i+=1
        break
        
    else:
        print(a[i])
        i+=1
        
# break the loop as soon it sees 'e'a = 'geeksforgeeks'
a='geeksforgeeks'
i=0
while i < len(a):
    i+=1
    pass
print(a[i-1])

#While loop with else
i=0
while i < 4:
    print(i)
    i+=1
else:
    print(i, "no break\n")
    
i=0
while i < 4:
    i+=1
    print(i)
    break
else:
    print("break")
    
#infinite loop
i = 0

while True:

    print(i)
    i+=1
    if i == 10:
        break
    
#user input    
a = int(input("Enter a number (-1 to quit)"))
while a != -1:
    a=int(input("Enter a number (-1 to quit)"))
    
    

# print entire file
file = open("myFile0.csv", 'r')
for line in file:
    print(line)
    

#print 10 lines
file = open("myFile0.csv", 'r')
i=0
for line in file: 
    i+=1
    if i>10:
        break
    print(line)
    

#File handling - readline
file = open("myFile0.csv", 'r')
x = file.readline(200)
print(x)
x= file.readline()
print(x)
file.close()

with open("myFile0.csv", 'r') as file:
    data =file.readline()
print(data)


with open("myFile0.csv", 'r') as file:
    for data in file:
      print(data)

import os
# writing to a file
file = open('myFile0_copy.csv', 'w')
file.write("#############Append this text at the end##############")
file.close()

with open ('myFile0_copy.csv', 'w') as file:
    file.write("replace with this text")
    file.close()
    
with open ('myFile0_copy.csv', 'a') as file:
    file.write("#############Append this text at the end##############")
    file.close()
    

os.rename('myFile0_copy.csv', 'myFile0_copy1.csv')
###os.remove('filename')



# local and global variables


def print_func():
    s= "roshan xavier"
    print(s)
s = "deepa joseph"
    
print_func()
print(s)


def print_func1():
    print(s)
    
s = "vincent roshan"
print_func1()
print(s)


def print_func2():
    global s
    print(s)
    s = "roshan xavier"
    print(s)
s= "Daniel Roshan"
print(s)
print_func2()  
print(s)

a = 15
 
 
# function to change a global value
def change():
    global a
    # increment value of a by 5
    b = a + 5
    a = b
    print(a)
 
 
change()


arr = [10, 20, 30]
 
def fun():
    for i in range(len(arr)):
        arr[i] += 10
 
 
print("'arr' list before executing fun():", arr)
fun()
print("'arr' list after executing fun():", arr)


arr = [10, 20, 30]
 
 
def fun():
    global arr
    arr = [20, 30, 40]
 
 
print("'arr' list before executing fun():", arr)
fun()
print("'arr' list after executing fun():", arr)

##############Needs analysis#############
    
import global_variables
print(a)
print(b)
##############Needs analysis#############


def add():
    x = 15
    
    def change():
        global x
        x = 20
        print("printing after change:", x)

    
    print("printint before change:", x)
    change()
    print("printint before change:", x)



add()
print("final value", x)


## functions
def shout():
    print("shout")
    
def scream():
    print("scream")
    
def noise(func):
    geetings = func()
    print("greet \n")
    

noise(shout)

noise(scream)



def create_adder(x):
    def adder(y):
        return x+y
    return adder
    
add = create_adder(15)
print(add(10))

##
def outerfunction(text):
    def innerfunction():
        print(text)
    innerfunction()
    
if __name__ =="__main__":
    outerfunction("roshan")
  
##    
    
def outerFunction(text): 
 
    def innerFunction(): 
        print(text) 
 
    # Note we are returning function
    # WITHOUT parenthesis
    return innerFunction  
 
if __name__ == '__main__': 
    myFunction = outerFunction('Hey!') 
    myFunction() 
    
    
############# Needs Analysis #########
# Python program to illustrate 
# closures 
import logging 
logging.basicConfig(filename='example.log',
                    level=logging.INFO) 
 
def logger(func): 
    def log_func(*args): 
        logging.info( 
            'Running "{}" with arguments {}'.format(func.__name__,
                                                    args)) 
        print(func(*args)) 
         
    # Necessary for closure to
    # work (returning WITHOUT parenthesis) 
    return log_func             
 
def add(x, y): 
    return x+y 
 
def sub(x, y): 
    return x-y 
 
add_logger = logger(add) 
sub_logger = logger(sub) 
 
add_logger(3, 3) 
add_logger(4, 5) 
 
sub_logger(10, 5) 
sub_logger(20, 10) 



##python opp

# Python3 program to
# demonstrate instantiating
# a class
class Dog:
 
    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"
 
    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)
 
 
# Driver code
# Object instantiation
Rodger = Dog()
 
# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()
print(Dog.attr1)
print(Dog.attr2)

###
class Dog:
    animal = 'dog'
    
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
        


Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)
 
print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)
 
# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)

##
class Myclass:
    def __init__(self, name=None):
        if name == None:
            print("Default constructor called")
        else:
            self.name = name
            print("parameterized constructor called with name", self.name)
    def method(self):
        if hasattr(self, 'name'):
            print("Method called with name", self.name)
        else:
            print("Method called without name")
            
obj1 = Myclass()
obj2 = Myclass("roshan")
obj1.method()
obj2.method()


# Python program to illustrate destructor
  
class Employee:
    def __init__(self):
        print("Employee created")
        
    def __del__(self):
        print("Destructor called")
        
        
def create_obj():
    print("creating object..")
    obj = Employee()
    print("created object")
    return obj


print("Create object function")
obj=create_obj()
obj.__del__()
#del obj


###### Go through destructor in OPP #########

class Base:
    def __init__(self, name):
        self.name = name
        
    def getName(self):
        return self.name
    
class Child(Base):
    def __init__(self, name, age):
        Base.__init__(self,name)
        self.age = age

        
    def getAge(self):
        return self.age
    
class GrandChild(Child):
    def __init__(self, name, age,address):
        Child.__init__(self, name, age)
        self.address = address

        
    def getAddress(self):
        return self.address
    
g = GrandChild("vincent", 12, "251 Livery St")
print(g.getAddress())
print(g.getAge())
print(g.getName())
        
        
class C:
    def __init__(self):
        self.c = 42
        self._d = 21
        
class D(C):
    def __init__(self):
        self.e =20
        C.__init__(self)
        
obj = D()
print(obj.e)
print(obj.c)
print(obj._d) 

##Multilevel in heritance

class Grandfather:
    
    def __init__(self, gfName):
        self.gfName = gfName
        

class Father(Grandfather):
    
    def __init__(self, fName, gfName):
        self.fName = fName
        Grandfather.__init__(self, gfName)
        
        
class Son(Father):
    
    def __init__(self, name, fName, gfName):
        self.name = name
        Father.__init__(self, fName, gfName, )
        
    def __str__(self):
        print(self.name, self.fName, self.gfName)
        
son = Son("Vincent", "roshan", "xavier")
son.__str__()

#Hierarchical Inheritance

class Parent:
    def func(self):
        print("This is the parent")
        
        
class Child1(Parent):
    def func1(self):
        print("This is child1")
        
class Child2(Parent):
    def func2(self):
        print("This is child2")
        
        
child1 = Child1()
child1.func()
child1.func1()

child2 = Child2()
child2.func()
child2.func2()

# Python program to demonstrate
# hybrid inheritance
 
 
class School:
    def func1(self):
        print("This function is in school.")
 
 
class Student1(School):
    def func2(self):
        print("This function is in student 1. ")
 
 
class Student2(School):
    def func3(self):
        print("This function is in student 2.")
 
 
class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")
 
 
# Driver's code
object = Student3()
object.func1()
object.func2()

# Encapsulation

class Base:
    
    def __init__(self):
        self.a = 23
        self._b = 24
        
        
class Derived(Base):
    
    def __init__(self):
        self.c = 25
        super().__init__()
        # Basic.__init__(self)
        
        
    def display(self):
        print(self.c)
        print(self.a)
        print(self._b)
        
base = Base()
derived = Derived()
print(base.a)
print(base._b)
print(derived.c)
print(derived.a)
print(derived._b)

derived.display()


# Polymorphism


def add(a,b,c=0):
    return (a+b+c)

print(add(1,2,3))
print(add(1,2))

#Polymorphism in classes
class India:
    
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is spoken widely in India")
    def type(self):
        print("India is a developing country")
        
class USA:
    
    def capital(self):
        print("Washington DC is the capital of India")
    def language(self):
        print("English is spoken widely in India")
    def type(self):
        print("US is a developed country")
        
obj1 = India()
obj2 = USA()

for obj in (obj1, obj2):
    obj.capital()
    obj.language()
    obj.type()
    
#Polymorphism in inheritance
class Bird:
  def intro(self):
    print("There are many types of birds.")
     
  def flight(self):
    print("Most of the birds can fly but some cannot.")
   
class sparrow(Bird):
  def flight(self):
    print("Sparrows can fly.")
     
class ostrich(Bird):
  def flight(self):
    print("Ostriches cannot fly.")
     
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
 
obj_bird.intro()
obj_bird.flight()
 
obj_spr.intro()
obj_spr.flight()
 
obj_ost.intro()
obj_ost.flight()

#Polymorphism in classes
class India:
    
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is spoken widely in India")
    def type(self):
        print("India is a developing country")
        
class USA:
    
    def capital(self):
        print("Washington DC is the capital of India")
    def language(self):
        print("English is spoken widely in India")
    def type(self):
        print("US is a developed country")
 
#Code 1        
obj1 = India()
obj2 = USA()

for obj in (obj1, obj2):
    obj.capital()
    obj.language()
    obj.type()
    
#Code 2
def fun(obj):
    obj.capital()
    obj.language()
    obj.type()
    
obj_india = India()
obj_USA = USA()
fun(obj_india)
fun(obj_USA)

#Polymorphism
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")


class Dog(Animal):
    def speak(self):
        print("Woof Woof")

class Cat(Animal):
    def speak(self):
        print("Meow Meow")
        
animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
    
    
#Static Variable

class CSSclass:
    stream = 'cse'
    def __init__(self, name, roll):
        self.roll = roll
        self.name = name
        
a = CSSclass("roshan", 45)
b = CSSclass("vincent", 50)

for obj in (a,b):
    print(obj.name)
    print(obj.roll)
    print(obj.stream)
print(CSSclass.stream)
CSSclass.stream = 'mech'
print(CSSclass.stream)
print(a.stream)
print(b.stream)

#Static Variable

class MyStatic:
    static_var =0
    def __init__(self):
        MyStatic.static_var+=1
        self.instance_var = MyStatic.static_var
        
obj1 = MyStatic()
print(obj1.static_var)
print(obj1.instance_var)

obj2= MyStatic()
print(obj2.static_var)
print(obj2.instance_var)
        


#Static methods

class StaticClass:
    @staticmethod
    def static_method():
        print("This is a static method")

# Call the static method without creating an instance of the class
StaticClass.static_method()

obj = StaticClass()
obj.static_method()

#Static methods

class MathUtility:
    
    @staticmethod 
    def add(x,y):
        return(x+y)
    
    @staticmethod 
    def product(x,y):
        return(x*y)
    
print(MathUtility.add(2,3))
print(MathUtility.product(2,3))

#Class  methods

class Addition:
    count = 0
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        Addition.count+=1
        
    def add(self):
        return (self.num1+self.num2)
    
    @classmethod 
    def display_counter(cls):
        print(cls.count)
    
    
    

    
addition = Addition(20,30)
addition = Addition(30,30)
addition = Addition(40,30)
print(addition.add())
addition.display_counter()
Addition.display_counter()


###Error Handling

try:
    x = 10
    y = 0
    z= x/y
except ZeroDivisionError as error:
    print("Error:", error)
finally:
    print("GeekforGeeks")
    
    
###Error Handling

try:
    amount = 200
    if amount < 2000:
        raise ValueError("please add money to your account")
    else:
        print("value is greater than 2000")
except ValueError as ve:
    print("Error:", ve)
finally:
    print("GeekforGeeks")
    
###Error Handling Index Error

try:
    lst =[1,2,3]
    print(lst[4])

except IndexError as ie:
    print("Error:", ie)
finally:
    print("GeekforGeeks")
    

###Error Handling - Arithemetic error
try:   
    a = 10/0  
    print (a) 
except ArithmeticError:   
        print ("This statement is raising an arithmetic exception.") 
else:   
    print ("Success.")
    

###Error Handling - Attribute error

class Attribute:
    pass

obj = Attribute()
obj.attr1



try:
    class Attribute:
        pass
    obj = Attribute()
    obj.attr1
except AttributeError:
    print("no attribute")
    
    
###Error Handling - module not found


try: 
    import module_does_not_exist 
except ModuleNotFoundError:
    print("ModuleNotFoundError: No module named 'module_does_not_exist'")
    
###Error Handling - OverflowError: math range error

try: 
    import math 
    print (math.exp(1000)) 
except OverflowError:
    print("OverflowError: math range error")
    
###Error Handling - keyerror

try:  
    dict ={"name": "roshan", "age": 26} 
    dict['gender']
except KeyError :
    print("KeyError: 'gender'")
    
###Error Handling - MemoryError


try:
    def fact(a): 
        factors = [] 
        for i in range(1, a+1): 
            if a%i == 0: 
                factors.append(i) 
        return factors  
      
    num = 600851475143
    print (fact(num)) 
except:
    print("error")
    

try:
    def func():
        print(x)    
    func()
except NameError as ne:
    print("NameError: name 'x' is not defined")
    
###Error Handling - ZeroDivisionError

try: 
    x = 10
    y = 0
    print(x/y)
except ZeroDivisionError:
    print("ZeroDivisionError")


###Error Handling - ValueError
try: 
    print(int('a'))
except ValueError:
    print("ValueError: invalid literal for int() with base 10: 'a'")
    
    
###Error Handling -  TypeError

try: 
    x = 5 + 'str'
except TypeError:
    print("TypeError: unsupported operand type(s) for +: 'int' and 'str'")
    
    
#Error handling - SyntaxError
    
    
try:
    print("roshan)
except SyntaxError:
    print("SyntaxError: EOL while scanning string literal")
    
    
#Error handling - StopIteration
    


try:
    Arr = [3, 1, 2] 
    i = iter(Arr)
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    
except StopIteration:
    print("StopIteration")
 
    
try:   
    def generator(): 
        for i in range(3):
          yield i
    gen = generator()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    
except StopIteration:
    print("StopIteration")
    
#Error handling - NotImplementedError
    

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the 'area' method")

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

# Creating an instance of Square
square = Square(5)

# Calling the abstract method 'area' in the base class
try:
    square_area = square.area()
except NotImplementedError as e:
    print(f"Error: {e}")
    


    """






































































 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 







































 











    


































