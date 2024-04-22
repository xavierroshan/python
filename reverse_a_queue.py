#from collections import deque
queue = [5,4,3,2,1]
stack = []
    
while (queue):
    stack.append(queue[0])
    queue.pop(0)
print(queue)
#print(stack)

while (stack):
    queue.append(stack.pop())
    
print(queue)
#print(stack)
        



    