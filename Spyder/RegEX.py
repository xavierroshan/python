"""# Exaples 1
import re
match = re.search('portal', 'GeeksforGeeks: A computer science portal for geeks')
print(match) 
print(match.start())
print(match.end())


import re
match = re.findall('portal', 'GeeksforGeeks: A computer science portal for geeks portal')
print(len(match))


import re
match = re.search('[Gg]eek', 'GeeksforGeeks: A computer science portal for geeks')
print(match)

import re
match = re.findall('[Gg]eek', 'GeeksforGeeks: A computer science portal for geeks')
print(match)

import re
match = re.findall('[Gg][A-Za-z][A-Za-z]ks', 'GeeksforGeeks: A computer science portal for geeks')
print(match)


import re
match = re.search( '[^Geeks]', 'GeeksforGeeks: A computer science portal for geeks')
print(match)

import re
match = re.search( '[A.]', 'GeeksforGeeks: A computer science portal for geeks')
print(match)

import re
match = re.findall( '[A.]', 'GeeksforGeeks: A computer science portal for A geeks')
print(match)

import re
match = re.search( '[$Geeks]', 'GeeksforGeeks: A computer science portal for geeks')
print(match)


import re
match = re.findall( 'a|e|i|o|u', 'GeeksforGeeks: A computer science portal for geeks')
print(match)

import re
match = re.search('[aeiou]', 'GeeksforGeeks: A computer science portal for geeks')
print(match)


import re
match = re.findall( '[aeiou]', 'GeeksforGeeks: A computer science portal for geeks')
print(match)


import re
s = s = 'geeks.forgeeks'
match = re.search('.', s)
print(match)

match = re.search('\.', s)
print(match)


import re
string = "The quick brown fox jumps over the lazy dog"
pattern = '[s-z]'
match = re.search(pattern, string)
print(match)

import re
string = "The quick brown fox jumps over the lazy dog"
pattern = '[s-z]'
match = re.findall(pattern, string)
print(match)




import re
match = re.search( '[^G]', 'GeeksforGeeks: A computer science portal for geeks')
print(match)

import re
match = re.findall( '[^G]', 'GeeksforGeeks: A computer science portal for geeks')
print(match)


import re
match = re.search( '^Geeks', 'GeeksforGeeks: A computer science portal for geeks')
print(match)

import re
match = re.findall( '^Geeks', 'GeeksforGeeks: A computer science portal for geeks')
print(match)



import re
match = re.search( 'geeks$', 'GeeksforGeeks: A computer science portal for geeks')
print(match)

import re
match = re.findall( 'geeks$', 'GeeksforGeeks: A computer science portal for geeks')
print(match)

import re
string = "The quick brown fox jumps over the lazy dog."
pattern = r"brown.fox"
match = re.search(pattern, string)
if match:
    print("pattern match")
else:
    print("No pattern match")




import re
pattern = r'colou?r'
string = ['color', 'colour', 'flour']
for s in string:
    if re.search(pattern, s):
        print(f'Matches -  {s}')

import re
pattern ='2023-?'                
dates = ['2022-12', '2023', '2023-01']  
for s in dates:
    if re.search(pattern, s):
        print(f'Matches -  {s}')     
        
     
     
import re
pattern = 'ab*'
strings = ['ab', 'abc', 'abcc', 'abccc', 'abb', 'abbbbbc', 'kbbbcc']  
for s in strings:
    if re.search(pattern, s):
        print(f"Matches - {s}")
        
        
import re
string = '{{This is a great oppurtunity}} {{ for roshan xavier}}'
pattern = '{{.*}}'
match = re.search(pattern, string)
if match:
    print("Pattern Matches")
else:
    print("Pattern doesn not match")  

    
import re
pattern = 'ab*'
strings = ['ab', 'abc', 'abcc', 'abccc', 'abb', 'abbbbbc', 'kbbbcc']  
for s in strings:
    if re.search(pattern, s):
        print(f"Matches - {s}")

        
        
    
import re    
strings = ['ac', 'abc', 'abcc', 'abccc']
pattern = 'ab+'
for s in strings:
    if re.search(pattern, s):
        print(f"Matches - {s}")

 
import re
pattern = 'a{2,4}'
strings = ['bac', 'bbaacc', 'aaabc', 'aaaabbc', 'baaaaac']
for s in strings:
     if re.search(pattern, s):
         print(f"Matches - {s}")

 
import re
pattern = r'\Agat'
strings = ['The great', 'gatsby of india', 'The alexander the great']
for s in strings:
     if re.search(pattern, s):
         print(f"Matches - {s}")
         

 
import re
#pattern = r'\bapple\b'
#strings = ['apple', 'pineapple', 'applesauce']
pattern = r'\bThe'
strings = ['The great', 'gatsby of india', 'The alexander the great']

for s in strings:
    if re.search(pattern, s):
        print(f'Match: {s}')
        
import re
text = ['abc123xyz456', 'abcdhdjd', 'eeejjjj1ef3']
pattern = '\d'
for s in text:
    if re.search(pattern, s):
        print(f'Match: {s}')
        
import re
text = ['abc123xyz456', 'abcdhdjd', 'eeejjjj1ef3']
pattern = '\d{3}'
for s in text:
    if re.search(pattern, s):
        print(f'Match: {s}')

 
import re
text = ['abc123xyz456', 'abcdhdjd', 'eeejjjje3']
pattern = '\d'
for s in text:
    if re.search(pattern, s):
        print(f'Match: {s}')
        
import re
text = ['abc123xyz456', 'abcdhdjd', 'eeejjjje3']
pattern = '\D\d\d'
for s in text:
    if re.search(pattern, s):
        print(f'Match: {s}')
        


import re
text = ['abc123xyz 456', 'abcdhdjd', 'eeejjjje3']
pattern = '\s'
for s in text:
    if re.search(pattern, s):
        print(f'Match: {s}')
        
        
import re
text = ['abc123xyz 456', 'abcdhdjd', 'eeejjjje3']
pattern = '\S'
for s in text:
    if re.search(pattern, s):
        print(f'Match: {s}')
        
        



import re
text = ['abc123xyz456', 'abcdhdjd', 'eeejjj je3', '!@#$@%%']
pattern = '\w'
for s in text:
    if re.search(pattern, s):
        print(f'Match: {s}')


import re
text = ['abc123xyz456', 'abcdhdjd', 'eeejjjje3', '!@#$@%%']
pattern = '\W'
for s in text:
    if re.search(pattern, s):
        print(f'Match: {s}')



import re
text = ['abc123xyz456', 'abcdhdjd', 'eeejjj je3', '!@#$@%%']
pattern = 'djd\Z'
for s in text:
    if re.search(pattern, s):
        print(f'Match: {s}')
        
        
        
        

import re
grp = re.search(r'([\d]{2})-([\d]{2})-([\d]{4})','26-08-2020 mnmn, 11-08-2020') 
print(grp.group())
print(grp.group(1))
print(grp.group(2))

import re
grp = re.search(r'(?P<dd>\d{2})-(?P<mm>\d{2})-(?P<yyyy>\d{4})','26-08-2020 mnmn, 11-08-2020') 
print((grp.group('yyyy')))


import re
pattern = 'ab+'
pattern = re.compile(pattern)
string = "abccc, is a great word, abbb"
print(pattern.findall(string))
print(pattern.search(string).group())


import re
pattern = 'ab+'
pattern = re.compile(pattern)
string = "abccc, is a great word, abbb"
print(pattern.findall(string))
print(pattern.search(string).group())

#positive and negative look ahead
import re
string = 'MY name is Roshan Xavier not Roshan Daniel'
pattern = re.compile(r'Roshan(?= Xavier)')
print(pattern.search(string))
print(pattern.findall(string))
pattern = re.compile(r'Roshan(?! Xavier)')
print(pattern.search(string))
print(pattern.findall(string))



#Python Program to Check if String Contain Only Defined Characters using Regex
#Input: ‘657’ let us say regular expression contain following characters-(‘78653’)
#Output: Valid Explanation: The Input string only consist of characters present in the given string 
#Input: ‘7606’ let us say regular expression contain following characters-(‘102’) 
#Output: Invalid

import re
input_str = '6577'
check =  '78653'
pattern = re.compile('^[78653]+$')
print(pattern.search(input_str))


#1Python Program to find the most occurring number in a string using Regex

#input: "ThisIsGeeksforGeeks!, 123" 
#Output :
#No. of uppercase characters = 4
#No. of lowercase characters = 15
#No. of numerical characters = 3
#No. of special characters = 2

import re
input_str = "ThisIsGeeksforGeeks!, 123" 
pattern = re.compile('[A-Z]')
pattern1 = re.compile('[a-z]')
pattern2 = re.compile('\d')
pattern3 = re.compile('\W')
print("No. of uppercase characters =",len(pattern.findall(input_str)))
print("No. of lowercase characters =",len(pattern1.findall(input_str)))
print("No. of numerical characters =",len(pattern2.findall(input_str)))
print("No. of special characters =",len(pattern3.findall(input_str)))


#2The most occurring number in a string using Regex in python

#Input :geek55of55geeks4abc3dr2 
#Output :55

#Input :abcd1def2high2bnasvd3vjhd44
#Output :2

import re
from collections import Counter
input_str = 'geek55of55geeks4abc3dr2'
pattern = re.compile(r'[0-9]+')
lst = pattern.findall(input_str)
print(max(Counter(lst)))


#3Python Regex to extract maximum numeric value from a string
#Input : 100klh564abc365bg
#Output : 564
#Maximum numeric value among 100, 564 and 365 is 564.

#Input : abchsd0sdhs
#Output : 0

import re
input_str = '100klh564abc365bg'
pattern = re.compile(r'[0-9]+')
lst = pattern.findall(input_str)
str1 = max(lst)
num= int(str1)
print(num)


###Word Boundry#####
import re 
text = "The cat sat on the mat."
pattern = re.compile(r'\w+')
print(pattern.findall(text))



#4Python regex to find sequences of one upper case letter followed by lower case letters
#Input : Geeks
#Output : Yes

#Input : geeksforgeeks
#Output : No

import re
input_str = 'Geeks for Geeks'
pattern = re.compile(r'[A-Z][a-z]+')
lst = pattern.findall(input_str)
print(lst)
print(len(lst))


#5Python Regex | Program to accept string ending with alphanumeric character
#Input: ankitrai326
#Output: Accept
#Input: ankirai@
#Output: Discard


import re 
input_str = 'ankitrai326'
input_str = 'ankirai@'
pattern = re.compile(r'[\w]$')
if (pattern.search(input_str)):
    print("Accept")
else:
    print("Do not accept")
    
    
#6Python Regex – Program to accept string starting with vowel

#Input: animal
#Output: Accepted

#Input: zebra
#Output: Not Accepted

import re 
input_str = 'nnimal'
match = re.search(r'\A[A|E|I|O|U|a|e|i|o|u]',input_str)
if match:
    print("Accepted")
else:
    print("Not Accepted")
    
    
#7How to check if a string starts with a substring using regex in Python?
#Input: String: "geeks for geeks makes learning fun" 
#       Substring: "geeks" 
#Output: True 
#Input: String: "geeks for geeks makes learning fun" 
#       Substring: "makes" 
#Output: False

import re 
input_string= "geeks for geeks makes learning fun" 
substring= "makes"
pattern = '\A'+substring
match = re.search(pattern,input_string)
if match:
    print(True)
else:
    print(False)
    
    
#8Check if email address valid or not in Python

#Input:  ankitrai326@gmail.com
#Output: Valid Email

#Input: my.ownsite@ourearth.org
#Output: Valid Email

#Input: ankitrai326.com
#Output: Invalid Email 

import re 
#input_str =   'ankitrai326@gmail.com'
#input_str =  'my.ownsite@ourearth.org'
input_str =  'ankitrai326.com'
pattern = r'[A-Za-z0-9\W]+@[A-Za-z]+\.[A-Za-z]+'
match= re.search(pattern, input_str)
if match:
    print("Valid Email")
else:
    print("Invalid Email")

#9Python program to find files having a particular extension using RegEx
import re 
file_name = 'file.xmlx'
pattern = r'\.xml$'
match = re.search(pattern, file_name)
if match:
    print("This is an xml file")
else:
    print("This is not an xml file")
    
#10Check if an URL is valid or not using Regular Expression
#Input : str = “https://www.geeksforgeeks.org/” 
#Output : Yes 
#Explanation : 
#The above URL is a valid URL.
#Input : str = “https:// www.geeksforgeeks.org/” 
#Output : No 
#Explanation : 
#Note that there is a space after https://, hence the URL is invalid. 

import re 

input_str = 'https://www.geeksforgeeks.org/'
pattern = r'https?://(www\.)?[A-Za-z@:%._\\+~#?&//=]{2,256}\.[a-z]{2,6}'
match = re.search(pattern, input_str)
if match:
    print("The above URL is a valid URL.")
else:
    print("The above URL is a not valid URL.")
    
    
#11Python program to check the validity of a Password
#Minimum 8 characters.
#The alphabet must be between [a-z]
#At least one alphabet should be of Upper Case [A-Z]
#At least 1 number or digit between [0-9].
#At least 1 character from [ _ or @ or $ ].
import re 

def pass_check(str1):
    
    pattern1 = re.compile(r'[A-Z]')
    pattern2 = re.compile(r'[0-9]')
    pattern3 = re.compile(r'[_@$]')
    

    if len(str1) < 8:
        return (False)
    elif len(pattern1.findall(str1)) < 1:
        return (False)
    elif len(pattern2.findall(str1)) < 1:
        return (False)
    elif len(pattern3.findall(str1)) < 1:
        return (False)
    else:
        return True
    
str1 = 'Rama#fortu9e '
print(pass_check(str1))
        
       
#12#Categorize Password as Strong or Weak using Regex in Python
#Minimum 9 characters and maximum 20 characters.
#Cannot be a newline or a space
#There should not be three or more repeating characters in a row.
#The same string pattern(minimum of two character length) should not be repeating.

#Input1 : Qggf!@ghf3
#Output1 : Strong Password!

#Input2 : aaabnil1gu
#Output2 : Weak Password: Same character repeats three or more times in a row

#Input3 : Geeksforgeeks
#Output3 : Weak Password: Same character repeats three or more times in a row

#Input4 : Aasd!feasnm
#Output4 : Weak password: Same string pattern repetition

#Input5 : 772*hdf77
#Output5 : Weak password: Same string pattern repetition

#Input6 : " "
#Output6 : Password cannot be a newline or space!

import re 
def pass_check(str1):
    
    pattern1 = re.compile(r'[A-Z]')
    pattern2 = re.compile(r' ')
    pattern3 = re.compile(r'(.)\1\1')
    pattern4 = re.compile(r'(..)(.*?)\1')


    if (len(str1)) > 22 or (len(str1)) <9:
        print('length is not appropriate')
        return False
    elif len(pattern2.findall(str1)) > 0:
        print('contains a space')
        return False
    elif len(pattern3.findall(str1)) > 0:
        print('contains three or more repeating characters in a row')
        return False
    elif pattern4.search(str1):
        print('string pattern repeating')
        return False
    else:
        return True
    
str1 = 'Aasd!feasnm'
print(pass_check(str1))

#13How to check if a string starts with a substring using regex in Python?

#Input: String: "geeks for geeks makes learning fun" 
#       Substring: "geeks" 
#Output: True 
#Input: String: "geeks for geeks makes learning fun" 
#       Substring: "makes" 
#Output: False

import re
str1 ='geeks for geeks makes learning fun'
sub = 'for'
pattern = '\A'+sub
match = re.search(pattern, str1)    
if match:
    print (True)
else:
    print(False)
    
    
####Learn re.split()####
import re
string = 'Words, words , Words'
pattern = '\W+'
#print(re.split(pattern, string))
string = 'Word\'s, words , Words'
pattern = '\W+'
#print(re.split(pattern, string))
string = 'Word\'s, words , Words'
pattern = '\w+'
#print(re.split(pattern, string))
string = 'Word\'s, words , Words'
pattern = '[wW]'
print(re.split(pattern, string))
string = 'Word\'s, words , Words'
pattern = '[w]'
print(re.split(pattern, string,flags=re.IGNORECASE))
string='On 12th Jan 2016, at 11:02 AM'
pattern = '\d+'
#print(re.split(pattern, string))
####Learn re.split()####

####Learn re.sub()####
import re
pattern = 'ub'
replace = '##'
string = 'Subject has Uber booked already'
print(re.sub(pattern, replace, string, flags=re.IGNORECASE))
print(re.subn(pattern, replace, string, flags=re.IGNORECASE))
####Learn re.sub()####


####m.group#####
import re
match = re.search(r'(\w+), (\w+), \1', 'foo, baz, foo')
print(match.group())
match = re.search(r'(\w+), \1', 'foo, foo, baz')
print(match.group())
match = re.search(r'(\w+), (\w+), \1', 'foo, baz, foo')
print(match.group())
match = re.search(r'(\w+), (\w+), \2', 'foo, baz, baz')
print(match.group())
####m.group#####
import re
m = re.search('(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)', 'foo,quux,baz')
print(m.group('w1'))
####m.group#####

#14Python – Check whether a string starts and ends with the same character or not (using Regular Expression)
#Input :  abba
#Output :  Valid

#Input :  a
#Output :  Valid

#Input :  abc
#Output :  Invalid

import re 
string = 'a'
match = re.search(r'^(.).*\1$', string)
if match:
    print("valid")
else:
    print("not valid")
    
#16Python | Remove all characters except letters and numbers
import re 
string = 'My name is Rx and my age is 43 and my password os  @#$$$12'
pattern = '[A-Za-z0-9]'
replace = ''
print(re.sub(pattern, replace, string))

#16Python Program to put spaces between words starting with capital letters using Regex

#Input : BruceWayneIsBatman
#Output : bruce wayne is batman
#Input :  GeeksForGeeks
#Output :  geeks for geeks


import re 
string = 'BruceWayneIsBatman'
pattern= '[A-Z][a-z]*'
lst = re.findall(pattern,string)
print(' '.join(lst))


#17Python Program to Remove duplicate words from Sentence

#Input : Good Good bye bye for your journey
#Output : Good bye for your journey



import re 
string = 'Good Good bye bye for your journey'
pattern= '\w+'
lst = re.findall(pattern,string)
lst1 = []
for x in lst:
    if x not in lst1:
        lst1.append(x)
print(' '.join(lst1))

#18How to validate IP address
# Python3 program to validate
# IP address using Regex
import re

# Function for Validating IP


def Validate_It(IP):

	# Regex expression for validating IPv4
	regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

	# Regex expression for validating IPv6
	regex1 = "((([0-9a-fA-F]){1,4})\\:){7}"\
			"([0-9a-fA-F]){1,4}"

	p = re.compile(regex)
	p1 = re.compile(regex1)

	# Checking if it is a valid IPv4 addresses
	if (re.search(p, IP)):
		return "Valid IPv4"

	# Checking if it is a valid IPv6 addresses
	elif (re.search(p1, IP)):
		return "Valid IPv6"

	# Return Invalid
	return "Invalid IP"

# Driver Code


# IP addresses to validate
IP = "257.120.223.13"
print(Validate_It(IP))

IP = "fffe:3465:efab:23fe:2235:6565:aaab:0001"
print(Validate_It(IP))

IP = "2F33:12a0:3Ea0:0302"
print(Validate_It(IP))

# This code is contributed by avanitrachhadiya2155



#18Extract IP address from file using Python
# importing the module 
import re 

# opening and reading the file 
with open('C:/Users/user/Desktop/New Text Document.txt') as fh: 
fstring = fh.readlines() 

# declaring the regex pattern for IP addresses 
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})') 

# initializing the list object 
lst=[] 

# extracting the IP addresses 
for line in fstring: 
lst.append(pattern.search(line)[0]) 

# displaying the extracted IP addresses 
print(lst) 

        
"""

 
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
















         




 
 
 





        
        
        
        
        
        
        
        

        
        
