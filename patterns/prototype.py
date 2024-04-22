import copy

class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
    def __str__(self):
        print(f"{self.color} {self.model} Car")
    def clone(self):
        return copy.deepcopy(self)

car = Car("Blue", "Sedan")
car.__str__()
clone_car = car.clone()
clone_car.__str__()
clone_car.color = "Red"
clone_car.model ="Hatchback"
clone_car.__str__()