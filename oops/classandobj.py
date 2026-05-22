"""class SharmaVishnu:
    a = 'lolo' # class ke ander ke variable -> attributes

    def Sample(): # class ke ander ke function -> method
        print('this is a sample function')
    
SharmaVishnu.Sample()  
print(SharmaVishnu.a) """  

"""class Animal:
    name = 'animal'

    # method
    def greet(self): # ki jab bhi class ke ander ke function ko object ki help se call 
    # karo ge to ek parameter set karna hoga
        print('this is a animal class') 

tau = Animal() #here tau is a object.

#object ka naam same as hota hai as name of the variable

tau.greet()"""

"""class Vikash():
    def greet(self):
        print('hello from vikash class')

    def add(self):
        a = 10
        b = 10
        print(a+b)    

baba = Vikash()
baba.greet()
baba.add()
"""

# constructor -> represented by __init__() (dunder method) 
# constructor sabse pehle execute hone wala function hai doest't matter inke
# uper ya neeche koi function present ho


"""class sharmavishnu():
    def greet(self):
        print('this is a greet function')

    def __init__(self,name,age):
        self.name = name # instance attributes
        self.age = age
        print('this is s constructor function')

    def menu(self):
        print(self.name)
        print(self.age)
        print('panner kulche') 

obj = sharmavishnu("vikash",20)     
obj.menu() """      

"""class vikash():
    def __init__(self,no1,no2):
        self.no1 = no1
        self.no2 = no2

    def findmax(self):
        if self.no1 > self.no2:
            print(f'{self.no1} is greater')
        else:
            print(f'{self.no2} is greater') 

obj = vikash(7,5)
obj.findmax()"""

"""class animal:
    name = 'dog' 
    
    def greet(self,new):
        self.name = new
        print('this is a greet function')
        print(self.name)

obj = animal()
obj.greet('cat') """   


"""class animal:
    name = 'dog' # class attributes

    # instance (object) can never change you class attribute
    @classmethod
    def change(cls,new):
        cls.new = new
        print(cls.new)

cheeta = animal()
cheeta.change('cat')
print(animal.name) """       

        
# static method
"""class sharmavishnu:

    @staticmethod  # Independent of object , matb object bane ya na bane ghanta fark nahi padta
    def menu():
        print('paneer kulche')
        print('paneer tikka')
        print('cold coffee')

new_market = sharmavishnu
new_market.menu()  """  


