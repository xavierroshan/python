
# Reverese the stack

# Implement stack
class Stack:
    def __init__(self):
        self.stack = []
        
    def add(self, value):
        self.stack.append(value)
        
    def remove(self):
        self.stack.pop()
        
    def print_queue(self):
        print(self.stack)
 
stack_instance = Stack()
stack_instance.add(1)
stack_instance.add(2)
stack_instance.add(3)
stack_instance.add(4)
stack_instance.add(5)
stack_instance.print_queue()
stack_instance.remove()
stack_instance.print_queue()
stack_instance.remove()
stack_instance.remove()
stack_instance.remove()
stack_instance.print_queue()
