class Animal:
    name = "lion" # public attribute
    _age = 12 # protected attributes
    __height = 120 # private attributes

    @classmethod
    def speak(self): # public object method
        print('the lion roars')

    def _walk(self): # protected object method
        print('the lion is walking')   

    def __sleep(self): # private method
        print("the lion is sleeping")  

obj1 = Animal()
print(obj1.name)
obj1.__sleep

# private attributes and method cannot be accessed by
# your object and inherited class

