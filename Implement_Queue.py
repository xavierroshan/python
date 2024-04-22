# Implement queue
class Queue:
    def __init__(self):
        self.queue = []
        
    def add(self, value):
        self.queue.append(value)
        
    def remove(self):
        self.queue.pop(0)
        
    def print_queue(self):
        print(self.queue)
 
queue_instance = Queue()
queue_instance.add(1)
queue_instance.add(2)
queue_instance.add(3)
queue_instance.add(4)
queue_instance.add(5)
queue_instance.print_queue()
queue_instance.remove()
queue_instance.print_queue()


