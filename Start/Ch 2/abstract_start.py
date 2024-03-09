# Using Abstract Base Classes to enforce class constraints
from abc import ABC,abstractmethod
class GraphicShape(ABC):
    def __init__(self):
        super().__init__()
    #This indicates that there's no specific implementation in the class and it must be overwritten    
    @abstractmethod 
    def calcArea(self):
        pass 

class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius
    def calcArea(self):
        return 3.141516*(self.radius)

class Square(GraphicShape):
    def __init__(self, side):
        self.side = side
    def calcArea(self):
        return self.side**2
    
#g = GraphicShape()
c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())
