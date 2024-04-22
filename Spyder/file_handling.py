#Eliminating repeated lines from a file using Python
## test
"""file1 = 'MOCK_DATA.csv'
f1 = open(file1, 'r')
file2 = 'MOCK_DATA_update.csv'
lst = []
for line in f1:
    print(line)"""
    
##method 1


file1 = 'MOCK_DATA.csv'
f1 = open(file1, 'r')
file2 = 'MOCK_DATA_update.csv'
f2 = open(file2, 'w')
uni_lst = []
dup_lst = []
for line in f1:
    if line in uni_lst:
        dup_lst.append(line)
    else:
        f2.write(line)
        uni_lst.append(line)

f1.close()
f2.close()


##method 2
file1 = 'MOCK_DATA.csv'
f1 = open(file1, 'r')
file2 = 'MOCK_DATA_update.csv'
f2 = open(file2, 'w')
unique_lines = set()
for line in f1:
    if line not in unique_lines:
        unique_lines.add(line)
    else:
        f2.write(line)
        
        
f1.close()
f2.close()


##method 3
file1 = 'MOCK_DATA.csv'
f1 = open(file1, 'a')
file2 = 'MOCK_DATA_update.csv'
f2 = open(file2, 'w')
unique_lines = set()
for line in f1:
    if line not in unique_lines:
        unique_lines.add(line)
    else:
        f2.write(line)
        
        
f1.close()
f2.close()
########################Learn fileinput module##################3
########################Learn shutil module##################3


##Python – Append content of one text file to another

file1 = 'fiirst_file_1.csv'
f1 = open(file1, 'r')
file2 = 'fiirst_file_2.csv'
f2 = open(file2, 'a')
data = f1.read()
f2.write(data)

f1.close()
f2.close()


#Python Program to merge two files into a third file
##method 1
file1 = 'MOCK_DATA.csv'
f1 = open(file1, 'r')
file2 = 'MOCK_DATA_update.csv'
f2 = open(file2, 'r')
file3 = 'MOCK_DATA_update_2.csv'
f3 = open(file3, 'w')
data = f1.read()
data += f2.read()
f3.write(data)
f1.close()
f2.close()


##method 2
##method 2
file1 = 'MOCK_DATA.csv'
file2 = 'MOCK_DATA_update.csv'
outfile = 'MOCK_DATA_update_2.csv'
with open(outfile, 'w') as outfile:
    for file in [file1,file2]:
        with open(file,'r') as infile:
            outfile.write(infile.read())

            
#Python program to Reverse a single line of a text file
file = 'fiirst_file_1.csv'
f = open(file, 'r')
choice = 2
lines = f.readlines()
f.close()
line = lines[choice]
reversed_choice = ' '.join((reversed(line.split())))
lines.pop(choice)
print(lines)
lines.insert(choice, reversed_choice)
print(lines)
    

f1 = open(file, 'w')
f1.writelines(lines)
f1.close()


#Python program to reverse the content of a file and store it in another fileS
# reversing each line
file = 'fiirst_file_1.csv'
f = open(file, 'r')
lines = f.readlines()
lines_final = []
f.close()
for line in lines:
    line = ' '.join(reversed(line.split()))
    lines_final.append(line)
    lines_final.append('\n')

f = open(file, 'w')
f.writelines(lines_final)
f.close()
#sorting lines
file = 'fiirst_file_1.csv'
f = open(file, 'r')
lines = f.readlines()
print
lines_final = lines[::-1]
print(lines_final)


f = open(file, 'w')
f.writelines(lines_final)
f.close()

#reverse the complete file
file = 'fiirst_file_1.csv'
f = open(file, 'r')
lines = f.read()
lines_final = lines[::-1]


f = open(file, 'w')
f.write(lines_final)
f.close()


#Python Program to Reverse the Content of a File using Stack

####behavior test
file1 ='MOCK_DATA.csv' 
f1 = open(file1,'r')
file2 ='MOCK_DATA_update.csv' 
f2 = open(file2,'w')
data = f1.readlines()
i = 2
for line in data:
    f2.write(line)
f1.close()
f2.close()
#######behaviour test#######3

# implementation of stack
class Stack:
 
    def __init__(self):
 
        # Creating an empty stack
        self._arr = []
 
    # Creating push() method.
    def push(self, val):
        self._arr.append(val)
 
    def is_empty(self):
 
        # Returns True if empty
        return len(self._arr) == 0
 
    # Creating Pop method.
    def pop(self):
 
        if self.is_empty():
            print("Stack is empty")
            return
 
        return self._arr.pop()
    
    
def reverse_file(file):
    S = Stack()
    original = open(file, 'r')
    for line in original:
        S.push(line.strip())
    original.close()
    
    output = open(file, 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n' )
    output.close()
    
file ='MOCK_DATA_update.csv'
reverse_file(file)
    

#Python Program to read List of Dictionaries from File
# parsing the file
def parse(l):
    dictionary = dict ()
    pairs = (l.strip('{}')).split(',')
    for pair in pairs:
        key, value = pair.split(':')
        dictionary[key] = value
    return dictionary



#driver Code


file = 'dictcsv.csv'
f = open(file,'r')
lines = f.read().split('\n')
lst = []
for l in lines:
    if l!= '': 
        lst.append(parse(l))

for l in lst:
    print(l)

f.close()



                     
        
        