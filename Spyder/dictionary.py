#Python program to find the sum of all items in a dictionary
#Input : {‘a’: 100, ‘b’:200, ‘c’:300}
#Output : 600

#Input : {‘x’: 25, ‘y’:18, ‘z’:45}
#Output : 88

#method 1
#input_dict = {'a': 100, 'b':200, 'c':300}
input_dict = {'x': 25, 'y':18, 'z':45}
sum_num = 0
for key,value in input_dict.items():
    sum_num+=value 
print(sum_num)

#method 2
input_dict = {'a': 100, 'b':200, 'c':300}
x=[value for key,value in input_dict.items()]
print(sum(x))

#method 3
input_dict = {'a': 100, 'b':200, 'c':300}
x=(value for key,value in input_dict.items())
print(sum(x))

#method 4
input_dict = {'a': 100, 'b':200, 'c':300}
lst = []
for i in input_dict:
    lst.append(input_dict[i])
print(sum(lst))

#method 4
input_dict = {'a': 100, 'b':200, 'c':300}
sum1=0
for i in input_dict.values():
    sum1+=i
print(sum1)


#method 5
input_dict = {'a': 100, 'b':200, 'c':300}
sum1=0
for i in input_dict:
    sum1+=input_dict[i]
print(sum1)



#Python – Extract Unique values dictionary values

#method 1
test_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}
lst = []
for value in test_dict.values():
        lst.extend(value)
print(list(set(lst)))

#method 2
test_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}
lst =[]
[lst.extend(value) for value in test_dict.values()]
print(list(set(lst)))

#method 3
test_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}
lst =[]

lst1 = [x for value in test_dict.values() for x in value  if x not in lst]
print(list(set(lst1)))

#method 4 

test_dict = {'gfg' : [5, 6, 7, 8],
'is' : [10, 11, 7, 5],
'best' : [6, 12, 10, 8],
'for' : [1, 2, 5]}

result = list(set(sum(test_dict.values(), [])))


#method 5
import operator as op
# initializing dictionary
test_dict = {'gfg' : [5, 6, 7, 8],
			'is' : [10, 11, 7, 5],
			'best' : [6, 12, 10, 8],
			'for' : [1, 2, 5]}

output = []
res = []
for x in test_dict.values():
    output.extend(x)
print(output)
    
for i in output:
    if op.countOf(res,i) == 0:
        res.append(i)
print(res)


# Python3 code to demonstrate working of
# Extract Unique values dictionary values
# initializing dictionary
from collections import Counter
test_dict = {'gfg': [5, 6, 7, 8],
			'is': [10, 11, 7, 5],
			'best': [6, 12, 10, 8],
			'for': [1, 2, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

valuesList = []
for key, values in test_dict.items():
	for value in values:
		valuesList.append(value)
freq = Counter(valuesList)
uniqueValues = list(freq.keys())
uniqueValues.sort()

# printing result
print("The unique values list is : " + str(uniqueValues))



#Python | Ways to remove a key from dictionary

#Before remove key:   {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21}
#Operation Perform:   del test_dict['Mani']
#After removing key:  {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22}


#method 1
bef_list =  {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21}
key = 'Mani'
del bef_list['Mani']
print(bef_list)


#method 2
bef_list =  {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21}
aft_list = {}
for x,y in bef_list.items():
    if x == 'Mani':
        continue
    else:
        aft_list[x] = y
print(aft_list)



#method 3
bef_list =  {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21}
bef_list.pop('Mani')
print(bef_list)


#method 4
bef_list =  {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21}
aft_list = {key:value for key,value in bef_list.items() if key!='Mani'}
print(aft_list)


#method 5
bef_list =  {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21}
aft_list = {key:bef_list[key] for key in bef_list if key!='Mani'}
print(aft_list)

### delete all using clear
bef_list =  {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21}
bef_list.clear()
print(bef_list)


#Python – Merging two dictionay

#Input: dict1 = {'a': 10, 'b': 8}
#          dict2 = {'d': 6, 'c': 4}
#Output: {'a': 10, 'b': 8, 'd': 6, 'c': 4}

#method 1
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict3 = {}
for x,y in dict1.items():
    dict3[x]= y
for x,y in dict2.items():
    dict3[x]= y
print(dict3)

#method 2
for z in [dict1,dict2]:
    for x,y in z.items():
        dict3[x]= y
print(dict3)


#method 3
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict1.update(dict2)
print(dict1)

#method 4
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

print({**dict1, **dict2})
    
#method 5
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
print(dict1 | dict2)

#method 6
from collections import ChainMap
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict3 = ChainMap(dict1,dict2)
print(dict3)
print(dict3['a'])
print(dict3['b'])
print(dict3['c'])
print(dict3['d'])


#Counting the frequencies in a list using dictionary in Python
#Input:  [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
#Output:  1 : 5
#         2 : 4
#         3 : 3
#         4 : 3
#         5 : 2


#method 1
from collections import Counter
input_lst = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
output = Counter(input_lst)
print(dict(output))

#method 2
input_lst = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
dict1 = {}
lst2= {k:input_lst.count(k) for k in input_lst}
print(lst2)


#method 3
input_lst = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
freq = {}
for i in input_lst:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)


#method 4
from collections import defaultdict
input_lst = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
freq = defaultdict(int)
for i in input_lst:
        freq[i]+=1

print(freq)


#method 5

input_lst = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
count = {}
for i in input_lst:
    count[i]= count.get(i,0)+1
print(count)
    

#method 6
import operator as op
input_lst = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
count ={}
for i in input_lst:
    if i not in count:
        count[i]=op.countOf(input_lst,i)
print(count)


#Python | Convert a list of Tuples into Dictionary

#Input : [('A', 1), ('B', 2), ('C', 3)]
#Output : {'B': [2], 'A': [1], 'C': [3]}

#method1
tuple1 = [('A', 1), ('B', 2), ('C', 3)]
print(dict(tuple1))

#method2
tuple1 = [('A', 1), ('B', 2), ('C', 3)]
dict1 = {x[0]:x[1] for x in tuple1 }
print(dict1)


#method3
tuple1 = [('A', 1), ('B', 2), ('C', 3)]
dict1 = {}
for x in tuple1:
    dict1[x[0]]= x[1]

print(dict1)

#method 4
# see how setdefault works in dictionary

tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
        ("suraj", 20), ("akhil", 25), ("ashish", 30)]
di = {}
for a,b in tups:
    di.setdefault(a,[]).append(b)
print(di)


#method 5

tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
        ("suraj", 20), ("akhil", 25), ("ashish", 30)]
di = {}
for t in tups:
    if t[0] in di:
        di[t[0]].append(t[1])
    else:
        di[t[0]]=t[1]
        
print(di)


#method 6

tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
        ("suraj", 20), ("akhil", 25), ("ashish", 30)]
di = {}
for k,v in tups:
    di.setdefault(k,v)
print(di)





#Python | Sort Python Dictionaries by Key or Value

#Input: {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
#Output: {'rajnish': 9, 'ravi': 10, 'sanjeev': 15, 'suraj': 32, 'yash': 2}

#method 1 - sort by key
from collections import OrderedDict
input_dict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
lst = list(input_dict.keys())
lst.sort()
output_dict = {}
for i in lst:
    output_dict[i]=input_dict[i]
print(output_dict)

input_dict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
lst = list(input_dict.keys())
lst.sort()
output_dict = OrderedDict()
for i in lst:
    output_dict[i]=input_dict[i]
print(output_dict)
    
#method 2 - sort by value
input_dict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
lst_key = list(input_dict.keys())
lst_key.sort()
output_dict = {x:input_dict[x] for x in lst_key}
print(output_dict)

#method 3 - sort by key
from collections import OrderedDict
input_dict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
output =OrderedDict(sorted(input_dict.items()))
print(output)

#method 4
key_value = {}

key_value[2] = 56
key_value[1] = 2
key_value[5] = 12
key_value[4] = 24
key_value[6] = 18
key_value[3] = 323

print(sorted(key_value.items(), key = lambda kv: (kv[0],kv[1])))

#Python – Convert key-values list to flat dictionary

#The original dictionary is : {‘name’: [‘Jan’, ‘Feb’, ‘March’], ‘month’: [1, 2, 3]} 
#Flattened dictionary : {1: ‘Jan’, 2: ‘Feb’, 3: ‘March’}

#method 1
org_dict = {'name': ['Jan', 'Feb', 'March'], 'month': [1, 2, 3]} 
lst_name = org_dict['name']
lst_mon = org_dict['month']
flat_dict = {}
for x,y in zip(lst_mon, lst_name):
    flat_dict[x]= y
print(flat_dict)

#method 2
org_dict = {'name': ['Jan', 'Feb', 'March'], 'month': [1, 2, 3]} 
lst_name = org_dict['name']
lst_mon = org_dict['month']
{x:y for x,y in zip(lst_mon,lst_name)}

#method 3

# initializing dictionary
test_dict = {'month' : [1, 2, 3],
			'name' : ['Jan', 'Feb', 'March']}
x = list(test_dict.values())
a=x[0]
b=x[1]
d={}
for i in range(len(a)):
    d[a[i]]=b[i]
print(d)

#method 4
org_dict = {'name': ['Jan', 'Feb', 'March'], 'month': [1, 2, 3]} 
lst_name = org_dict['name']
lst_mon = org_dict['month']
flat_dict = dict(zip(lst_mon, lst_name))
print(flat_dict)

#method 5
org_dict = {'name': ['Jan', 'Feb', 'March'], 'month': [1, 2, 3]} 
flat_dict
for x in range(len(org_dict['month'])):
    flat_dict[org_dict['month'][x]]=org_dict['name'][x]
print(flat_dict)
    



# Python3 code to demonstrate working of
# Convert key-values list to flat dictionary
# initializing dictionary

#method 1
test_dict = {'month' : [1, 2, 3],
			'name' : ['Jan', 'Feb', 'March']}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert key-values list to flat dictionary
x=list(test_dict.values())
a=x[0]
b=x[1]
d=dict()
for i in range(0,len(a)):
	d[a[i]]=b[i]
# printing result
print("Flattened dictionary : " + str(d))


#method 2
input_dict = {'month' : [1, 2, 3],
			'name' : ['Jan', 'Feb', 'March']}
dict1 = dict(zip(input_dict['month'], input_dict['name']))
print(dict1)


#method 3

input_dict = {'month' : [1, 2, 3],
			'name' : ['Jan', 'Feb', 'March']}
dict1 ={input_dict['month'][x]:input_dict['name'][x] for x in range(len(input_dict['month']))}
print(dict1)


#method 4

input_dict = {'month' : [1, 2, 3],
			'name' : ['Jan', 'Feb', 'March']}
dict1 ={input_dict['month'][x]:input_dict['name'][x] for x in range(len(input_dict['month']))}
print(dict1)


#Ways to sort list of dictionaries by values in Python – Using itemgetter

###Learn Itemgetter################
from operator import itemgetter
List = [10,9,8,7,3,11,4]
element = itemgetter(2)
print(element(List))

data = {'name': 'John', 'age': 30, 'city': 'New York'}
element = itemgetter('name', 'age')
print(element(data))


# method1
people = [
    ('Alice', 25, 160),
    ('Bob', 30, 175),
    ('Charlie', 22, 155),
    ('David', 28, 180),
]

people1 = sorted(people, key =itemgetter(1))
print(people1)
people1= sorted(people, key = itemgetter((2)))
print(people1)


lst= [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]
lst2 = sorted(lst, key = itemgetter(('name')))
print(lst2)
lst= [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]
lst2 = sorted(lst, key=itemgetter('age'))
print(lst2)


#Ways to sort list of dictionaries by values in Python – Using lambda function
lst= [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]
lst2 = sorted(lst, key = lambda x:x['age'] )
print(lst2)
lst2 = sorted(lst, key = lambda x:x['name'])
print(lst2)


from collections import defaultdict

#Handling missing keys in Python dictionaries
#method 1
ele = {'a': 5, 'c': 8, 'e': 2}
if 'd' in ele: 
        print(ele['d'])
else:
    print("key not found")
 
    
#method 2
country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}
country_code_japan = country_code.get('Japan', 'None')
print(country_code_japan)


#method 3
country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}
country_code.setdefault('Japan', 'none')
print(country_code['Japan'])


#method 4
country_code = {'India': '0091',
                'Australia': '0025',
                'Nepal': '00977'}
 
try:
    print(country_code['India'])
    print(country_code['USA'])
except KeyError:
    print('Not Found')
    
####### defautdict ########
# definition: my_dict = defaultdict(factory_method)
from collections import defaultdict
country_code = defaultdict(int)
country_code['India']= 91
print(country_code['Canada'])

####understand the difference between below two code snippets
###factory_method####
##1##
from collections import defaultdict

def default_factory():
    return 'Not Found'

my_default_dict = defaultdict(default_factory)

print(my_default_dict['a'])  # Output: 'Not Found'


##2##
def default_factory():
    return 'Key not found'

my_default_dict = defaultdict(default_factory)
my_default_dict = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}
#print(my_default_dict['India'])
print(my_default_dict['Canada'])


# method 6
from collections import defaultdict

defd = defaultdict(lambda : 'Key Not found')

defd['a'] = 1 
defd['b'] = 2

print ("The value associated with 'a' is : ",end="")
print (defd['a'])

print ("The value associated with 'c' is : ",end="")
print (defd['c'])


#Python – Insertion at the beginning in OrderedDict

#method 1
from collections import OrderedDict
 
# Initialising ordered_dict
iniordered_dict = OrderedDict([('akshat', '1'), ('nikhil', '2')])
 
# Inserting items in starting of dict
iniordered_dict.update({'manjeet': '3'})
iniordered_dict.move_to_end('manjeet', last=False)
 
# Printing result
print("Resultant Dictionary : "+str(iniordered_dict))


#method 2
from collections import OrderedDict
 
# initialising ordered_dict
ini_dict1 = OrderedDict([('akshat', '1'), ('nikhil', '2')])
ini_dict2 = OrderedDict([("manjeet", '4'), ("akash", '4')])
 
# adding in beginning of dict
both = OrderedDict(list(ini_dict2.items()) + list(ini_dict1.items()))
 
# print result
print ("Resultant Dictionary :"+str(both))

#method 3
from collections import OrderedDict
 
# Initialising ordered_dict
ini_dict = OrderedDict([('akshat', '1'), ('nikhil', '2')])
 
# Creating a iniordered ordered dict
iniordered_dict = OrderedDict()
 
# Inserting new key-value pair at the beginning of iniordered_dict
iniordered_dict.update({'manjeet':'3'})
iniordered_dict.move_to_end('manjeet', last = False)
 
# popitem() method to remove and insert key-value pair at beginning
while ini_dict:
    iniordered_dict.update({ini_dict.popitem(last=False)})
 
# Print result
print("Resultant Dictionary :" + str(iniordered_dict))

#Check order of character in string using OrderedDict( )

#Input: 
#string = "engineers rock"
#pattern = "er";
#Output: true
#Explanation: 
#All 'e' in the input string are before all 'r'.

#Input: 
#string = "engineers rock"
#pattern = "gsr";
#Output: false
#Explanation:
#There are one 'r' before 's' in the input string.
from collections import OrderedDict
#method 1
string = "engineers rock"
pattern = "neers x"

try:
    j = 0
    for char in string:
        if char == pattern[j]:
            j+=1
            
        if j==len(pattern):
            print(True)
            break
except IndexError as er:
    print(er, 'false')
    
#method 2
from collections import Counter
input_dict =['john','johnny','jackie','johnny',
            'john','jackie','jamie','jamie',
            'john','johnny','jamie','johnny',
            'john', 'john'] 
dict1 = Counter(input_dict)
dict2 = {}

for value in dict1.values():
    dict2[value] = []
print(dict2)

for key, value in dict1.items():
    dict2[value].append(key)
print(dict2)
name = dict2[max(dict2.keys())][0]
print(name)
    
#Python – Append Dictionary Keys and Values ( In order ) in dictionary
#Input : test_dict = {“Gfg” : 1, “is” : 2, “Best” : 3} 
#Output : [‘Gfg’, ‘is’, ‘Best’, 1, 2, 3] 

#method 1
test_dict = {'Gfg' : 1, 'is' : 2, 'Best' : 3} 
lst_key = []
lst_value = []
for x,y in test_dict.items():
    lst_key.append(x)
    lst_value.append(y)
print(lst_key +lst_value)



#method 2
test_dict = {'Gfg' : 1, 'is' : 2, 'Best' : 3} 
lst_key = list(test_dict.keys())
lst_value= list(test_dict.values())

print(lst_key + lst_value)

#method 3
from itertools import chain

test_dict = {'Gfg' : 1, 'is' : 2, 'Best' : 3} 
lst_key = list(test_dict.keys())
lst_value= list(test_dict.values())
lst = list(chain(lst_key,lst_value))
print(lst)
lst1 = lst_key.copy()
lst1.extend(lst_value)
print(lst1)

#Python dictionary with keys having multiple inputs

#method 1
#x+y-z
tuple1= ((1,2,3),(4,5,6),(7,8,9))
print(type(tuple1))
my_dict = {}
for a in tuple1:
    my_dict[a]=a[0]+a[1]+a[2]
    
print(my_dict)

#method 2
tuple1= ((1,2,3),(4,5,6),(7,8,9))
print(type(tuple1))
my_dict = {}
for a in tuple1:
    my_dict[a]=a[0]+a[1]+a[2]
{my_dict[a]:a[0]+a[1]+a[2] for a in tuple1}
    
print(my_dict)

#method 3

 # Creating a dictionary with multiple inputs for keys
data = {
    (1, "John", "Doe"): {"a": "geeks", "b": "software", "c": 75000},
    (2, "Jane", "Smith"): {"e": 30, "f": "for", "g": 90000},
    (3, "Bob", "Johnson"): {"h": 35, "i": "project", "j": "geeks"},
    (4, "Alice", "Lee"): {"k": 40, "l": "marketing", "m": 100000}
                          }

print(data[(1, "John", "Doe")]["a"])
print(data[(2, "Jane", "Smith")]["f"])
print(data[(3, "Bob", "Johnson")]["j"])

#method 4
# dictionary containing longitude and latitude of places
places = {("19.07'53.2", "72.54'51.0"):"Mumbai", ("28.33'34.1", "77.06'16.6"):"Delhi"}

print(places)
print('\n')

# Traversing dictionary with multi-keys and creating
# different lists from it
lat = []
long = []
plc = []
for i in places:
	lat.append(i[0])
	long.append(i[1])
	plc.append(places[i])

   
print(lat)
print(long)
print(plc)


#Python | Remove all duplicates words from a given sentence
#Input : Geeks for Geeks
#Output : Geeks for

#Input : Python is great and Java is also great
#Output : is also Java Python and great

#method 1
#sentence = 'Geeks for Geeks'
sentence = 'Python is great and Java is also great'
words = sentence.split(' ')
lst_uni = []
for word in words:
    if word not in lst_uni:
        lst_uni.append(word)
print(lst_uni)




from collections import Counter
#method 2
#sentence = 'Geeks for Geeks'
sentence = 'Python is great and Java is also great'
words = sentence.split(' ')
word_count = dict(Counter(words))
lst = []
for x,y in word_count.items():
    lst.append(x)
print(lst)


# method 3
sentence = 'Python is great and Java is also great'
words = sentence.split(' ')
print(list(set(words)))



# method 4
sentence = 'Python is great and Java is also great'
words = sentence.split(' ')
lst = []
for word in words:
    if words.count(word) == 1:
        lst.append(word)
    else:
        if word not in lst:
            lst.append(word)
print(lst)
    

# method 5
sentence = 'Python is great and Java is also great'
words = sentence.split(' ')
print(' '.join(dict.fromkeys(words)))

### Test ###

test_dict = {'Gfg' : 1, 'is' : 2, 'Best' : 3} 
print(' '.join(dict.fromkeys(test_dict)))


###################

# method 4
import operator as op
sentence = 'Python is great and Java is also great'
words = sentence.split(' ')
lst = []
for word in words:
    if op.countOf(words,word) == 1:
        lst.append(word)
    else:
        if word not in lst:
            lst.append(word)
print(lst)



#Python – Keys associated with Values in Dictionary
#input : test_dict = {‘abc’ : [10, 30], ‘bcd’ : [30, 40, 10]} 
#Output : {10: [‘abc’, ‘bcd’], 30: [‘abc’, ‘bcd’], 40: [‘bcd’]} 

#Input : test_dict = {‘gfg’ : [1, 2, 3], ‘is’ : [1, 4], ‘best’ : [4, 2]} 
#Output : {1: [‘is’, ‘gfg’], 2: [‘gfg’, ‘best’], 3: [‘gfg’], 4: [‘is’, ‘best’]}

#method 1
from collections import defaultdict
dict1 = {'abc' : [10, 30], 'bcd' : [30, 40, 10]} 
lst1 = []
for x,y in dict1.items():
    lst1.extend(y)
lst2 = list(set(lst1))
dict2 = defaultdict()

for x in lst2:
    dict2[x]=[]   

for x,y in dict1.items():
    for i in y:
        dict2[i].append(x)
print(dict2)

#method 2
from collections import defaultdict
dict1 = {'abc' : [10, 30], 'bcd' : [30, 40, 10]} 
dict2 = defaultdict(list)

for key,val in dict1.items():
    for ele in val:
        dict2[ele].append(key)
print(dict2)        
        
        
#method 3
dict1 = {'abc' : [10, 30], 'bcd' : [30, 40, 10]} 
dict2 = {}

for key, val in dict1.items():
    for ele in val:
        if ele in dict2:
            dict2[ele].append(key)
        else:
            dict2[ele]=[key]

print(dict2)

#method 4
test_dict = {'gfg' : [1, 2, 3], 'is' : [1, 4], 'best' : [4, 2]} 

print("The original dictionary is : " + str(test_dict))

result_dict = {}
for key, val in test_dict.items():
	for ele in val:
		result_dict.setdefault(ele, []).append(key)

# printing result 
print(result_dict)


result_dict = {}

for key, value in test_dict.items():
    for ele in val:
        result_dict.setdefault(ele, []).append(key)
        
print(result_dict)



#Python dictionary, set and counter to check if frequencies can become same
#Input  : str = 'xyyz'
#Output : Yes
#We can remove character ’y’ from above 
#string to make the frequency of each 
#character same. 

#Input : str = 'xyyzz'
#Output : Yes
#We can remove character ‘x’ from above 
#string to make the frequency of each 
#character same.

#Input : str = 'xxxxyyzz'
#Output : No
#It is not possible to make frequency of 
#each character same just by removing at 
#most one character from above string.

from collections import Counter
str1 = 'xxxxyyzz'
count = Counter(str1)
lst = list(set(dict(count).values()))
print(lst)
if len(lst) == 2 and abs(lst[1]-lst[0])==1:
    print(True)
else:
    print(False)
  




#Python Dictionary to find mirror characters in a string
#Input : N = 3
#        paradox
#Output : paizwlc
#We mirror characters from position 3 to end.

#Input : N = 6
#        pneumonia
#Output : pneumlmrz


#str1 = 'paradox'
str1 = 'pneumonia'
n = 6
lst = list(str1)

original = 'abcdefghijklmnopqrstuvwxyz'
reverse = 'zyxwvutsrqponmlkjihgfedcba'
lst1 = lst[0:n-1]
print(lst1)

for i in range(n-1,len(lst)):
    print(lst[i])
    print('$$$$$$$$$$$$$$$')
    for x,y in zip(original, reverse):
        if lst[i] == x:
            print(x,y)
            lst1.append(y)
    print('*************')
print(lst)
print(lst1)
        

#Check if binary representations of two numbers are anagram
#Input : a = 8, b = 4 
#Output : Yes
#Binary representations of both
#numbers have same 0s and 1s.

#Input : a = 4, b = 5
#Output : No

from collections import Counter
a,b = 10,6 
a_bin = bin(a)
b_bin = bin(b)
d = abs(len(a_bin)-len(b_bin))


if len(a_bin)>len(b_bin):
    for i in range(d):
        b_bin = '0'+b_bin
else:
    for i in range(d):
        a_bin = '0'+a_bin
    
print(a_bin)
print(b_bin)

count_a_bin = Counter(a_bin)
count_b_bin = Counter(b_bin)
if count_a_bin == count_b_bin:
    print(True)
else:
    print(False)
    
    
#Python counter and dictionary intersection example 
#(Make a string using deletion and rearrangement)

#Input : s1 = ABHISHEKsinGH
#      : s2 = gfhfBHkooIHnfndSHEKsiAnG
#Output : Possible

#Input : s1 = Hello
#      : s2 = dnaKfhelddf
#Output : Not Possible

#Input : s1 = GeeksforGeeks
#      : s2 = rteksfoGrdsskGeggehes
#Output : Possible

from collections import Counter
s1 = 'GeeksforGeeks'
s2 = 'rteksfoGrdsskGeggehes'

s1_counter =(Counter(s1))
s2_counter = (Counter(s2))


result = s1_counter & s2_counter
print(result)
if result == s1_counter:
    print("Possible")
else:
    print("Not Possible")
    
    
#Possible Words using given characters in Python

# Input : Dict = ["go","bat","me","eat","goal","boy", "run"]
#        arr = ['e','o','b', 'a','m','g', 'l']
#Output : go, me, goal. 

#method 1
from collections import Counter
Dict = ["go","bat","me","eat","goal","boy", "run"]
arr = ['e','o','b', 'a','m','g', 'l']
lst = []



for x in Dict:
  if (Counter(x) & Counter(arr)) == Counter(x):
      lst.append(x)
print(lst)


#method 2



def charsCount(word):
    dict1 = {}
    for x in word:
        dict1[x]=dict1.get(x,0)+1
    return(dict1)

def possibleWords(arr1, arr2):
    for x in arr1:
        flag = 1
        char_set = charsCount(x)
        for key in char_set:
            if key not in arr2:
                flag = 0
            else:
                if char_set[key] < arr2.count(key):
                    flag = 0
        if flag == 1:
            print(x)
   
                
    
    
arr1 = ["go","bat","me","eat","goal","boy", "run"]
arr2 = ['e','o','b', 'a','m','g', 'l']
possibleWords(arr1, arr2)

#method 3 - assumes there is norepeatition in the arr2


def possible_words(Dict, arr):
    arr_set = set(arr)
    result = []
    for word in Dict:
        if set(word).issubset(arr_set):
            result.append(word)
    return result
 
 
Dict = ["go", "bat", "me", "eat", "goal", "boy", "run"]
arr = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
print(possible_words(Dict, arr)) 

##############check recursion method########### 

#Python Counter to find the size of largest subset of anagram words

"""Input: 
ant magenta magnate tan gnamate
Output: 3
Explanation
Anagram strings(1) - ant, tan
Anagram strings(2) - magenta, magnate,
                     gnamate
Thus, only second subset have largest
size i.e., 3

Input: 
cars bikes arcs steer 
Output: 2"""

#method 1

def charCount(word):
    char_Count = {}
    for i in word:
        char_Count[i]=char_Count.get(i,0)+1
    return char_Count

def count_dict(sentence):
    my_dict = {}
    for x in sentence:
        char_Count = charCount(x)
        my_dict[x]=char_Count
    return(my_dict)

def ana_dict(my_dict):
    dict2 = {}
    for x, y in my_dict.items():
        dict2.setdefault(tuple(sorted(y.items())), []).append(x)
    return(dict2)

    
sentence = 'ant magenta magnate tan gnamate'
sentence = sentence.split(' ')
my_dict =count_dict(sentence)
dict2 =ana_dict(my_dict)

# Print the largest subset size
largest_subset_size = max(len(subset) for subset in dict2.values())
print("Output:", largest_subset_size)

#method 2
from collections import Counter
    
input_str = 'ant magenta magnate tan gnamate'
input_lst = input_str.split(' ')
print(input_str)
print(input_lst)
output_lst = []
for x in input_lst:
    output_lst.append(''.join(sorted(x)))
print(output_lst)
print(Counter(output_lst))
print(max(Counter(output_lst).values()))


#Print anagrams together in Python using List and Dictionary
#Input: arr = [‘cat’, ‘dog’, ‘tac’, ‘god’, ‘act’]

#Output: ‘cat tac act dog god’

def charCount(word):
    char_Count = {}
    for i in word:
        char_Count[i]=char_Count.get(i,0)+1
    return char_Count

def count_dict(arr):
    my_dict = {}
    for x in arr:
        char_Count = charCount(x)
        my_dict[x]=char_Count
    return(my_dict)

def ana_dict(my_dict):
    dict2 = {}
    for x, y in my_dict.items():
        dict2.setdefault(tuple(sorted(y.items())), []).append(x)
    return(dict2)

def final_arr(dict2):
    final_lst = []
    for x,y in dict2.items():
        final_lst.extend(y)
    return final_lst
        


arr = ['cat', 'dog', 'tac', 'god', 'act']
my_dict = count_dict(arr)
dict2 = ana_dict(my_dict)
final_lst = final_arr(dict2)
print(final_lst)






    """
    K-th Non-repeating Character in Python using List Comprehension and OrderedDict
    """
    
    
    
    
    
    

        
















    


    
























    

    

        






















    







