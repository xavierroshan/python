# Python program to accept the strings
# which contains all the vowels
 
# Function for check if string
# is accepted or not
 
#using all() method 
 
def check(string):
    vowels = "aeiou" #storing vowels
    if all(vowel in string.lower() for vowel in vowels):
        return "Accepted"
    return "Not accepted"
 
 
 
#initializing string
string = "SEEquoiaL"
# test the function
print(check(string))


from collections import OrderedDict
def removeDupWithoutOrder(str): 
    return "".join(set(str)) 
 

def removeDupWithOrder(str): 
    return (OrderedDict.fromkeys(str)) 
 
# Driver program 
if __name__ == "__main__": 
    str = "geeksforgeeks"
    print ("Without Order = ",removeDupWithoutOrder(str)) 
    print ("With Order = ",removeDupWithOrder(str)) 
    
    
"""Scraping And Finding Ordered Words In A Dictionary using Python"""












# Function to count number of characters, words, spaces and lines in a file
def counter(fname):

	# variable to store total word count
	num_words = 0
	
	# variable to store total line count
	num_lines = 0
	
	# variable to store total character count
	num_charc = 0
	
	# variable to store total space count
	num_spaces = 0
	
	# opening file using with() method
	# so that file gets closed
	# after completion of work
	with open(fname, 'r') as f:
		
		# loop to iterate file
		# line by line
		for line in f:
			
			# incrementing value of num_lines with each
			# iteration of loop to store total line count
			num_lines += 1
			
			# declaring a variable word and assigning its value as Y
			# because every file is supposed to start with a word or a character
			word = 'Y'
			
			# loop to iterate every
			# line letter by letter
			for letter in line:
				
				# condition to check that the encountered character
				# is not white space and a word
				if (letter != ' ' and word == 'Y'):
					
					# incrementing the word
					# count by 1
					num_words += 1
					
					# assigning value N to variable word because until
					# space will not encounter a word can not be completed
					word = 'N'
					
				# condition to check that the encountered character is a white space
				elif (letter == ' '):
					
					# incrementing the space
					# count by 1
					num_spaces += 1
					
					# assigning value Y to variable word because after
					# white space a word is supposed to occur
					word = 'Y'
					
				# loop to iterate every character
				for i in letter:
					
					# condition to check white space
					if(i !=" " and i !="\n"):
						
						# incrementing character
						# count by 1
						num_charc += 1
						
	# printing total word count
	print("Number of words in text file: ",
		num_words)
	
	# printing total line count
	print("Number of lines in text file: ",
		num_lines)
	
	# printing total character count
	print('Number of characters in text file: ',
		num_charc)
	
	# printing total space count
	print('Number of spaces in text file: ',
		num_spaces)
	
# Driver Code:
if __name__ == '__main__':
	fname = 'MOCK_DATA.csv'
	try:
		counter(fname)
	except:
		print('File not found')



#Python – Get number of characters, words, spaces and lines in a file

file1 = 'MOCK_DATA.csv'
f1 = open(file1, 'r')
line_num = 0
for line in f1:
    line_num+=1
print(line_num)
  
f1.close()


file1 = 'MOCK_DATA.csv'
f1 = open(file1, 'r')
word_num=0
for line in f1: 
    for word in line.split(','):
        word_num +=1
print(word_num)
f1.close()


file1 = 'MOCK_DATA.csv'
f1 = open(file1, 'r')
char_num=0
for line in f1: 
    for c in line:
        char_num +=1
print(char_num)
f1.close()

file1 = 'MOCK_DATA.csv'
f1 = open(file1, 'r')
space_num=0
for line in f1: 
    for c in line:
        if c == ' ':
          space_num +=1
print(space_num)
f1.close()


# Matrix multiplication
# Program to multiply two matrices using list comprehension

# take a 3x3 matrix
A = [[12, 7, 3],
	[4, 5, 6],
	[7, 8, 9]]

# take a 3x4 matrix
B = [[5, 8, 1, 2],
	[6, 7, 3, 0],
	[4, 5, 9, 1]]

# result will be 3x4
result = [[sum(a * b for a, b in zip(A_row, B_col)) 
						for B_col in zip(*B)]
								for A_row in A]

for r in result:
	print(r)





def matrix_multiply_recursive(A, B):
	# check if matrices can be multiplied
	if len(A[0]) != len(B):
		raise ValueError("Invalid matrix dimensions")

	# initialize result matrix with zeros
	result = [[0 for j in range(len(B[0]))] for i in range(len(A))]

	# recursive multiplication of matrices
	def multiply(A, B, result, i, j, k):
		if i >= len(A):
			return
		if j >= len(B[0]):
			return multiply(A, B, result, i+1, 0, 0)
		if k >= len(B):
			return multiply(A, B, result, i, j+1, 0)
		result[i][j] += A[i][k] * B[k][j]
		multiply(A, B, result, i, j, k+1)

	# perform matrix multiplication
	multiply(A, B, result, 0, 0, 0)
	return result


# example usage
A = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
B = [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]

result = matrix_multiply_recursive(A, B)
for row in result:
	print(row)

    
'String slicing in Python to check if a string can become empty by recursive deletion'
'Python | Permutation of a given string using inbuilt function'
'Python – Convert Snake case to Pascal case'

"""
Python – Replace duplicate Occurrence in String
Python | Check for URL in a String
"""