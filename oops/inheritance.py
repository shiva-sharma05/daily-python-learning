"""
1 single inheritance
2 multiple inheritance
"""
# single inheritance
'''class parent:

    def __init__(self):
        print('this is parent class constructor')

    def greet(self):
        print('this is a parent class')

class child(parent):

    def __init__(self):
        print('this is child class constructor')

    def show(self):
        print('this is child class')     

obj  = child()
obj.greet()
obj.show()  '''         

"""class factory:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def show(self):
        print(f'bag has {self.name} and {self.color}')

class bata(factory):
    def __init__(self, name, color,zip,pocket):
        super().__init__(name, color) 
        self.zip = zip
        self.pocket = pocket

    def display(self):
        print(f"bag has {self.name} , {self.color} color , {self.zip} and {self.pocket} pockets")

rahul = bata()
rahul.display """     

#2. Multiple Inheritane -> 2 Parent, 1 Child
class Father: #Parent1

    def _init_(self):
        print('This is Father class constructor')

    def greet_father(self):
        print('This is Father class')

class Mother: #Parent2
    def _init_(self):
        print('This is Mother class constructor')

    def greet_mother(self):
        print('This is Mother class')


class Child(Mother,Father): #Child
    #If we have to run constructor of Father class first
    
    def _init_(self):
        Father._init_(self) #Sabse pehle Father class ka constructor will be run
        Mother._init_(self) #After Father class Mother class constructor will be run

obj = Child()
obj.greet_father()
obj.greet_mother()


