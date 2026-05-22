'''
# user defined function 
def greeting():  #difining function
    print("hello good morning !! ")

greeting() # calling function

def palindrome(n): # a and b are parameters
   rev = 0
   copy = n
   while n != 0:
       rev = rev * 10 + n%10
       n = n//10

   if copy == rev:
       print("pailndrome")
   else:
       print("not a palindrome")    
          
palindrome(121)
palindrome(1223)
palindrome(12221)
palindrome(1277)

def multiply(a,b): #fixed position
    print(a*b)

multiply(10,20)    # fixid positional argument

# if you give a value using default argument you always to give further 
# value using arguments using default arguments

def info(a,b,c,d,e):
    print(a,b,c,d,e)

info(12,34, e =67, c =12, e =86)    

# default parameters
'''
'''
def fibonacci(n):
   sum = 0
   a = 0
   b = 1

   while a <= n:
      print(a)
      a = b
      b = a+b
      
fibonacci(5)      
'''
'''
def hello():
    return "how are you"

def agecheaker(n):
    if n >= 18 :
        return True
    else:
        return False
    
age = int(input("tell your age :- "))   

if agecheaker(age):
    print("you can vote")
else:
    print("you cannot vote")    
'''
'''
def hello1():
    hello2()
    print("hello 1")


def hello2():
    hello3()
    print("hello 2")


def hello3():
    hello4()
    print("hello 3")


def hello4():
    print("hello 4")     

hello1()

'''



"""def numbers(n):
    if n == 101:
        return "done"
    # number(n+1)
    print(n)
    numbers(n+1)

numbers(1)"""

"""
args -> args value ko accept krte hai in the form of tupple
args -> *variable_name 
iska use -> jab hame nahi pata hota ki kitne parameters hone wale hai

"""

def add (*chacha):
    print(type(chacha))
    print(chacha)

add(10,20,30,40,50)

def polio(name,age,pin,contect):
    print(name,age,pin,contect)
# polio(neme="rishi",age=22,pin=1222,contect=00000000)


"""kwargs -> keyward arguments
denote -> **variable_name
kwargs -> accept krte hai sari value in the form of dictionary
parameter -> keys 
arguments woh -> value"""

def polio(**variable):
    print(type(variable))
    print(variable)
    for i in variable:
        print(f'parameter -> {i} and argument -> {variable[i]}')
polio(name="suresh",age=21,school="dps")

'''
lambda function -> jab ek function ek line me aa jaye
lambda -> keyword
a,b : a+b -> agar a and b variable mai kuch value aayegi toh hi a+b 
chale ga nahi to nahi chalega
'''
add = lambda a,b: a+b   
print(add(10,20))