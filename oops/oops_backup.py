"""class Factory:
    a = 12 

    def show():
        print('how are you')

Factory.show()

class hello:
    a= 12
    def speak(self):
        print('how are you')

obj = hello()  # created an object
print(obj.a) # object can also sccess attributes
obj.speak() # when we use objects to call any method inside class we always
# send location of my object"""

# class factory:
#     def __init__(self):
#         print(self)
#         print('hello how are you')

#     print('this is p23 batch')

# a = factory()
# b = factory()
# c = factory()

# class Factory:
#     def __init__(self,zip,pockets,material):
#         self.zip = zip
#         self.pockets = pockets
#         self.material = material

#     def details(self):
#         print('your dettails is :-')
#         print(self.zip)
#         print(self.pockets)
#         print(self.material)    

# reebok = Factory(2,2,"leather")  
# reebok.details()

# campus = Factory(4,2,"plastic")
# campus.details()

# class Registration:
#     age = 18
#     name ="shiva"
#     email = "siva@gmail.com"
#     number = 1245678876

#     def __init__(self,name,email,age,number):
#         if age >= Registration.age :
#           self.name = name # object attributes
#           self.email = email
#           self.number = number
#           self.age = age
#         else:
#            print('you cannot register you are underage')  
#            return


#     def details(self): # object method - it targect the location of object
#        print(self.name) # self will take the location of the object
#        print(self.email) # whichever object is calling
#        print(self.number)
#        print(self.age)
       
#     @classmethod
#     def dummy_details(cls):
#        print(cls.name) # self will take the location of the object
#        print(cls.email) # whichever object is calling
#        print(cls.number)
#        print(cls.age)

#     @staticmethod     # static method
#     def college_method(): # this method will not targect any location
#        print('hii how are you')   

       
# student = Registration("shiva","shiva@gmail.com",19,1234567876)

# student.dummy_details()
# student.college_method()

                           # inheritance

# one class attributes and method can be accessed by another class this thing is knowen
# as inheritance

# class BhopalFactory:
#    reg_num =1234098765
#    def __init__(self,colour,size,type):
#       self.colour=colour
#       self.size=size
#       self.type=type

#    def details(self):
      
#       print("your shoe details aree :-")
#       print(self.colour)
#       print(self.size)
#       print(self.type)


# class IndoreFactory(BhopalFactory):

#    def __init__(self,colour,size,type,price):
#       super().__init__(colour,size,type)
#       self.price = price

# class UjjainFactory(IndoreFactory):
#    def __init__(self, colour, size, type, price):
#       super().__init__(colour, size, type, price)



# shoe1 = BhopalFactory('red',8,"jordan")

# shoe2 = IndoreFactory("yellow",7,"sneakers",1000)

# shoe2.details()

# class animal:
#     def __init__(self,name):
#         self.name = name

#     def details(self):
#         print(self.name)    
        
# class human:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def speak():
#         print('hello human you speak')  

# class robot(animal,human):
#     def __init__(self, name,age):
#         human.__init__(self,name,age)          
                

# obj = robot("alpha" , 2)

# polymorphism

# class Animal:
#     name = 'lion'
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def details(self):
#         print('details are :- ')   
#         print(self.name) 
#         print(self.age)

# class human:
#     name = 'harsh' 
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def details(self):
#         print('details are :- ')   
#         print(self.name) 
#         print(self.age)
#         print(self.gender) 

# obj1 = Animal('lion' , 4) 
# obj2 = human('harsh',23,'male')   

# obj1.details()
# obj2.details()

               
        
# class BhopalFactory:
#    reg_num =1234098765
#    def __init__(self,colour,size,type):
#       self.colour=colour
#       self.size=size
#       self.type=type

#    def details(self):
      
#       print("your shoe details aree :-")
#       print(self.colour)
#       print(self.size)
#       print(self.type)


# class IndoreFactory(BhopalFactory):

#    def __init__(self,colour,size,type,price):
#       super().__init__(colour,size,type)
#       self.price = price

#    def details(self):
#       print(super().details())
#       print(self.price)

# obj = IndoreFactory('black',8,'jorden',180000)
# obj.details()        

# class Animal:
#    def hello(a):
#       pass
#    def hello(a,b):
#       pass
   
# obj = Animal()
# obj.hello(12,34)

# encapsulation 

# class Animal:


#     a = 12 # public attributes
#     _b = 23 # PROTECTED ATTRIBUTES
#     __c = 45 # private attributes


#     def hello(self): # public method
#         print('how are you')

#     def _hello2(self): # protected method
#         print('how are you 2')  
    
#     @classmethod
#     def __hello3(self): # private method
#         print('how are you 3')      

# obj = Animal() 


# abstraction 

from abc import ABC , abstractmethod

class person(ABC):

    @ abstractmethod
    def info():
        pass

    @ abstractmethod
    def register():
        pass


class Teacher(person):
    def info():
        pass

    def register():
        pass

class Student(person):
    def info():
        pass

    def register():
        pass

obj = Student()

