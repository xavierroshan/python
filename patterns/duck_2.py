class Circle:
    
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return (22/7*self.radius*self.radius)
        
class Square:
    
    def __init__(self, edge):
        self.edge = edge
    def area(self):
        print(self.edge*self.edge)
        
class Rectangle:
    
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        print(self.length*self.breadth)
        
def Area (Shape):
    Shape.area() # another way of this function below
    
def print_area(shape): # but here need to use return not print
    if hasattr(shape, 'area') and callable(getattr(shape, 'area')):
        # Check if the object has an 'area' method
        print(f"The area of the shape is: {shape.area()}")
    else:
        print("Cannot calculate area for this shape.")
    
    
    
circle = Circle(5)
square = Square(5)
rectangle = Rectangle(5,7)
circle_area=Area(circle)
square_area=Area(square)
rectangle_area=Area(rectangle)
print_area(circle)
        
        
        
        
        