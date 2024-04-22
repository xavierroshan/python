# Python | Print an Inverted Star Pattern

#method 1
for i in range(10):
    for j in range(10):
        if j >i:
            print('*', end='')
        else:
            print(' ', end='')
    print('')
    

    

for i in range(10):
    for j in range(10):
        if j >i:
            print(' ', end='')
        else:
            print('*', end='')
    print('')
    
    
for i in range(10,-1,-1):
    for j in range(10):
        if j >i:
            print('*', end='')
        else:
            print(' ', end='')
    print('')
    
for i in range(10,-1,-1):
    for j in range(10):
        if j >i:
            print(' ', end='')
        else:
            print('*', end='')
    print('')
    

#m3thod 2
# Python | Print an Inverted Star Pattern
for i in range(10):
    print((10-i)*' '+ i*'*')
for i in range(10):
    print((i)*' '+ (10-i)*'*')
for i in range(10,-1,-1):
    print((10-i)*' '+ i*'*')
for i in range(10,-1,-1):
    print((i)*' '+ (10-i)*'*')    
    
    
#Python 3 | Program to print double sided stair-case pattern

for i in range(1,11):
    if i in [1,2]: 
        print(4*' ' +  2*'*' + 4*' ')
    if i in [3,4]: 
        print(3*' ' +  4*'*' + 3*' ')
    if i in [5,6]: 
        print(2*' ' +  6*'*' + 2*' ')
    if i in [7,8]: 
        print(1*' ' +  8*'*' + 1*' ')
    if i in [9,10]: 
        print(0*' ' + 10*'*'+ 0*' ')
            
            

n =25
for i in range(1,n):
    if i%2 ==0:
        print(int((n-1-i)/2)*' ' + i*'*' + int((n-1-i)/2)*' ')
        print(int((n-1-i)/2)*' ' + i*'*' + int((n-1-i)/2)*' ')
        
#Program to print the pattern ‘G’
        
        
for i in range(7):
    for j in range(6):
        if (i == 0 or i == 6) and (j == 2 or j == 3 or j == 4):
            print('*', end='')
        elif (j == 1) and (i == 1 or (i == 2 or i == 4 or i == 5)):
            print('*', end='')
        elif (i == 3) and (j == 1 or j == 3 or j == 4 or j == 5):
            print('*', end='')
        elif (j == 5) and (i == 4 or i == 5):
            print('*', end='')
        else:
            print(' ', end='')

    print('')
    


n = 7    
for i in range(n):
    for j in range(n-1):
        if (i == 0 or i == n-1) and (j == 2 or j == 3 or j == 4):
            print('*', end='')
        elif (j == 1) and (i == 1 or (i == 2 or i == 4 or i == 5)):
            print('*', end='')
        elif (i == n//2) and (j == 1 or j == 3 or j == 4 or j == 5):
            print('*', end='')
        elif (j == n-2) and (i == 4 or i == 5):
            print('*', end='')
        else:
            print(' ', end='')

    print('')
    







