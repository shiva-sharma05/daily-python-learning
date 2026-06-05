from abc import ABC , abstractmethod

"""class shapes(ABC):

    @abstractmethod
    def area():
        pass

    @abstractmethod
    def perimeter():
        pass


class Square(shapes):
    def __init__(self,side):
        self.side = side

    def area(self):
        print(4* self.side)

    def perimeter(self):
        print(self.side*self.side)  

class circle(shapes):
    def __init__(self,redius):
        self.redius = redius

    def area():
        pass

    def perimeter():
        pass    

obj = Square(10)
obj.area()"""

"""class Robots(ABC):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        print(f'hello my name is {self.name}')  

obj = Robots('alpha1')      
print(obj) """ 

class Numbers:
    def __init__(self,value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __eq__(self, value):
        return self.value == value.value

a = Numbers(10)
b = Numbers(10)

print(a+b)


            
