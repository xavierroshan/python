class family:
    def __init__(self, name, number):
        self.name = name
        self.number = number

obj = family("chirayil", 6)
print(hasattr(obj, "number"))
x=getattr(obj, "number")
print(x)
print(callable(family))
print(callable(obj))

#In Python, the callable() function returns True if the object appears callable (i.e., it can be called as a function), and False otherwise. In your example, the object obj is an instance of the family class, which is not inherently callable. Instances of regular classes, by default, are not callable unless they define a __call__ method.