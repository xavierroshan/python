class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance == None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.value = None
        return cls._instance
        
singleton_instance1 = Singleton()
singleton_instance2 = Singleton()
print(singleton_instance2 == singleton_instance1)
singleton_instance1.value = 42
print(singleton_instance2.value)