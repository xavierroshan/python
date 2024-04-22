class Stack:
    def __init__(self):
        self.stack = []
        
    def add(self, value):
        self.stack.append(value)
        
    def remove(self):
        self.stack.pop()
    
    def pop(self):
        return self.stack.pop()
        
    def print_stack(self):
        print (self.stack)
        
    def print_length(self):
        n = (len(self.stack))
        return (n)
        
stack_instance = Stack()
stack_instance.add(1)
stack_instance.add(2)
stack_instance.add(3)
stack_instance.add(4)
stack_instance.add(5)
stack_instance.print_stack()
n = stack_instance.print_length()
print(n)
stack_reverse = Stack()
for i in range(0,n):
    stack_reverse.add(stack_instance.pop())
stack_reverse.print_stack()


