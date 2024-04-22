#Python program to add two Matrices

#method 1
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
    
    
Z=[]
for i in range(len(X)):
    z = []
    for j in range(len(X[0])):
        z.append(X[i][j]+Y[i][j])
    Z.append(z)
print(Z)

#method 2
import numpy as np
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]

Z = np.array(X)+np.array(Y)
print(Z)


#method 3
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]

Z= [[X[i][j]+Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
print(Z)

# Program to add two matrices using zip()

X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

result = [list(map(sum, zip(*t))) for t in zip(X,Y)]
print(result)


#####testing code#####

for t in zip(X,Y):
    print('*****')
    print(t)
    zip(*t)
    for t in zip(*t):
        print(t)
result = [list(zip(*t)) for t in zip(X,Y)]
print(result)
#####testing code#####



#Adding and Subtracting Matrices in Python

#method 1
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
    
    
Z=[]
for i in range(len(X)):
    z = []
    for j in range(len(X[0])):
        z.append(X[i][j]+Y[i][j])
    Z.append(z)
print(Z)

#method 2
import numpy as np
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]

Z = np.array(X)+np.array(Y)
print(Z)


#method 3
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]

Z= [[X[i][j]+Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
print(Z)



#Python | Matrix creation of n*n
# method 1
n =3
Z= []
for i in range(n):
    row = []
    for j in range(n):
        row.append(n*i+j)
    Z.append(row)
print(Z)


# method 2
n =3
Z= []

Z = [[n*i+j for j in range(n)] for i in range(n)]

print(Z)    



#Transpose a matrix in Single line in Python

#method 1
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
Z = []

for i in range(3):
    z= []
    for j in range(3):
        z.append(X[j][i])
    Z.append(z)
print(Z)

#method 2
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
Z = []

for i in range(3):
    z= []
    for j in range(3):
        z.append(X[j][i])
    Z.append(z)

Z= [[X[j][i] for j in range(3)] for i in range(3)]
print(Z)

#method 3
import numpy as np
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]

Z = np.transpose(X)
print(Z)


#method 3
import numpy as np
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
matrix = np.array(X)
print(matrix.T)


#Python | Get Kth Column of Matrix


#method 1
Z=[[0, 1,  2, 3,  4,  5,  6,  7], 
  [ 8, 9, 10, 11, 12, 13, 14, 15], 
  [16, 17, 18, 19, 20, 21, 22, 23], 
  [24, 25, 26, 27, 28, 29, 30, 31], 
  [32, 33, 34, 35, 36, 37, 38, 39], 
  [40, 41, 42, 43, 44, 45, 46, 47], 
  [48, 49, 50, 51, 52, 53, 54, 55], 
  [56, 57, 58, 59, 60, 61, 62, 63]]


n = len(Z)
k =3
lst = []
for i in range(n):
    for j in range(n):
        if j==k:
            lst.append(Z[i][j])
print(lst)

#method 2

Z=[[0, 1,  2, 3,  4,  5,  6,  7], 
  [ 8, 9, 10, 11, 12, 13, 14, 15], 
  [16, 17, 18, 19, 20, 21, 22, 23], 
  [24, 25, 26, 27, 28, 29, 30, 31], 
  [32, 33, 34, 35, 36, 37, 38, 39], 
  [40, 41, 42, 43, 44, 45, 46, 47], 
  [48, 49, 50, 51, 52, 53, 54, 55], 
  [56, 57, 58, 59, 60, 61, 62, 63]]

n = len(Z)
k =3
lst = [Z[i][j] for j in range(n) if j==k for i in range(n)]
print(lst)


#method 3
Z=[[0, 1,  2, 3,  4,  5,  6,  7], 
  [ 8, 9, 10, 11, 12, 13, 14, 15], 
  [16, 17, 18, 19, 20, 21, 22, 23], 
  [24, 25, 26, 27, 28, 29, 30, 31], 
  [32, 33, 34, 35, 36, 37, 38, 39], 
  [40, 41, 42, 43, 44, 45, 46, 47], 
  [48, 49, 50, 51, 52, 53, 54, 55], 
  [56, 57, 58, 59, 60, 61, 62, 63]]




n = len(Z)
k =3
lst = [x[k] for x in Z]
print(lst)

#method 4
Z=[[0, 1,  2, 3,  4,  5,  6,  7], 
  [ 8, 9, 10, 11, 12, 13, 14, 15], 
  [16, 17, 18, 19, 20, 21, 22, 23], 
  [24, 25, 26, 27, 28, 29, 30, 31], 
  [32, 33, 34, 35, 36, 37, 38, 39], 
  [40, 41, 42, 43, 44, 45, 46, 47], 
  [48, 49, 50, 51, 52, 53, 54, 55], 
  [56, 57, 58, 59, 60, 61, 62, 63]]




n = len(Z)
k =3
lst = list(map(lambda x:x[k], Z))
print(lst)


#Python program to multiply two matrices
#Input : X = [[1, 7, 3],
#             [3, 5, 6],
#             [6, 8, 9]]
#       Y = [[1, 1, 1, 2],
#           [6, 7, 3, 0],
#           [4, 5, 9, 1]]
 
#Output : [55, 65, 49, 5]
#         [57, 68, 72, 12]
#         [90, 107, 111, 21]

#method 1
import numpy as np
# take a 3x3 matrix
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
 
# take a 3x4 matrix
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]
 
result = np.dot(A,B)
print(result)

#Python program for Matrix Product
#method 1
lst = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
prod=1
for i in range(len(lst)):    
    for j in lst[i]:
        prod= prod*j
print(prod)


#method 2
import math
lst = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
prod = [math.prod(j for j in lst[i]) for i in range(len(lst))]
print(math.prod(prod))

#method 3
import math
lst = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
lst1 = []
for x in lst:
    lst1.extend(x)
print(math.prod(lst1))


#method 4
lst = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
lst1 = []
for x in lst:
    lst1.extend(x)
prod = 1
for x in lst1:
    prod*=x
print(prod)

# Python – Vertical Concatenation in Matrix
input_lst = [['Gfg', 'good', 'geeks'], ['is', 'for', 'best'], ['grf']] 
#input_lst = [['Gfg', 'good'], ['is', 'for'], ['Best']]
max_len=max([len(x) for x in input_lst])
for x in input_lst:
    if len(x) < max_len:
        for i in range(max_len-len(x)):
            x.append('')

n = len(input_lst)
m = len(input_lst[0])
temp = ''
i =0
j=0
output_lst = []
for j in range(m):
    for i in range(n):
        temp = temp+input_lst[i][j]
    print(temp)
    output_lst.append(temp)
    temp =''
        
print(output_lst)











        
        


















    