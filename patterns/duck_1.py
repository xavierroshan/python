class Dog:
    def speak():
        print("Woof")
        
class Cat:
    def speak():
        print("Meow")
        
class Duck:
    def speak():
        print("Quack")
        
def Animal_speak(animal):
    animal.speak()
    
dog = Animal_speak(Dog)
cat = Animal_speak(Cat)
duck = Animal_speak(Duck)