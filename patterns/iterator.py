#Iterator Interface
class Iterator:
    def next(self):
        pass
    def has_next(self):
        pass
#concrete Iterator
class ListIterator(Iterator):
    def __init__(self, iterator):
        self.iterator = iterator
        self.index = 0
    def next(self):
        if self.has_next():
            result = self.iterator[self.index]
            self.index+=1 
            return result
        else:
            raise StopIteration
    def has_next(self):
        return self.index < len(self.iterator)

listIterator = ListIterator([1,2,3])
print(listIterator.next())
print(listIterator.next())
print(listIterator.next())
print(listIterator.next())
            