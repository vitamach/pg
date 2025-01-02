from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod #povinnost
    def area(self):
        """Abstraktní šablona"""
        pass

class Rectangle(Shape): #podtřída
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

if __name__ == "__main__":
    obdelnik = Rectangle(4, 5)
    print(f"Plocha obdélníku: {obdelnik.area()}")
    
    kruh = Circle(3)
    print(f"Plocha kruhu: {round(kruh.area(), 1)}")