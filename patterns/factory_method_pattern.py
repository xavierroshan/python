#Factory Method Pattern

from abc import ABC, abstractmethod
class Animal (ABC):
    @abstractmethod
    def speak(self):
        pass
    
class Dog (Animal):
    def speak(self):
        print("Woof")
        
class Cat (Animal):
    def speak(self):
        print("Meow")
        
class Animalfactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass
    
class Dogfactory(Animalfactory):
    def create_animal(self):
        return Dog()
        
class Catfactory(Animalfactory):
    def create_animal(self):
        return Cat()
        

def animal_factory(animal_factory):
    pet = animal_factory.create_animal()
    return pet.speak()

dog_factory = Dogfactory()
cat_factory = Catfactory()
dog_sound = animal_factory(dog_factory)
cat_sound = animal_factory(cat_factory)
