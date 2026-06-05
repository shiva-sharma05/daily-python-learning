class Animal :
    def speak (self):
        print('animals are shouting ')

class human :
    def speak(self):
        print('humans are intelligent so they are speaking')

obj1 = Animal()
obj2 = human()

obj1.speak()
obj2.speak()
'''

# both speak methods appears to be 
# same but both have different task and this is 
# known as polymorphism

class Reebok():
    def __init__(self, material,size):
        self.material = material
        self.size = size
        
    def details (self):
        print("your bag details is :")
        print(self.material)
        print(self.size)    

class campus(Reebok):
    def __init__(self,  material, size, color):
        super().__init__(  material, size, color)
        self.color = color

    def details (self):
        print(self.color)
        print(super().details())

obj1 = campus('leather',10,'black')

obj1.details()

# a child class object has the power to call methods and 
# attributes of a parent class but he cannot call the details 
# method of his  parent class cause that details method 
# is overidden and this concept  
 


class animal:
    def hello (self,a ):
        print('how are you ')

    def hello (self,a,b):
        print('how are you man ')'''


# method overloading is a concept where you define
# similar name methods inside a single class with
# different parameter