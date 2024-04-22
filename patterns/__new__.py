class Myclass:
    def __new__(cls, *args, **kwargs):
        instance =  super(Myclass, cls).__new__(cls)
        print("creating a new instance")
        return instance
        
    def __init__(self,value):
        print("initializing an instance")
        self.value = value
        
obj = Myclass(10)