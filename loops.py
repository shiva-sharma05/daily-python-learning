# for loop


#for i in range(1,11,1):
#    print(i)


#for i in range(20,30,1):
#print(i)

#for i in range(-12,11):
 #   print(i)

#for i in range(10,-11,-1):
#print(i)

#for i in range(18,181,18):
 #   print(i)

#a = int(input("tell me a number :"))
#for i in range(a,a*10+1,a):
 #   print(i)

#for i in range(100):
 #   print("hello world")

#n = int(input("give the value"))
#for i in range(1,n+1):
#    print(i)

#for i in range(1,6,1):
 #   print(i)

#for i in range(1,11):
 #print(i)

#for i in range(2,11,2):
 #   print(i)

#for i in range (1,10,2):
 #   print(i)

#for i in range (10,0,-1):
 #   print(i)

#for i in range(1,11):
 #   print("2 * ",i,"= "

# if we print loop in +ve diraction 



#for i in range(n,0,-1):
 #   print(i)

#for i in range(1,11):
 #   print(n," * ",i," = ",n*i)   

'''
1 
n = int(input("tell me your number :- "))
a = 1
for i in range(1,n+1):
    a = a * i

print(a)

# in this loop i is adding by one 
# and  we multiplying i with a with the previous value 
# 1 is starting value and n+1 is the stoping value
'''

'''
2
n =int(input("enter the value :- "))
a = 0

for i in range (1,n+1):
    a = a + i 

print(a)    

# in this loop i is adding by 1
# and we adding the previous value of a in a 
# 1 is the starting and n+1 is stoping of i  in the loop

'''

'''
3

n = int(input("enter the value :- "))

for i in range(1,n+1):
    if i%2 == 0 :
      print(i)


# in this code i is adding by 1 and when is divided by 2 it print i

'''

'''
4
n = int(input("enter the value :- "))

for i in range(1,n+1):
    if i%2 != 0 :
      print(i)
'''

'''
5
n = int(input("enter the value :- "))

for i in range(1,n+1):
    if i%5 == 0 :
      print(i)

      '''

'''
6
n = int(input(" enter the value"))
a = 0

for i in range(1,n+1):
    if i%2 == 0:
        a = a + i

print(a)



n = int(input(" tell me a val :-- "))
a = 1

for i in range(1,n+1):
    a = a * i

print(a)    

'''

'''
n = int(input("give me a number :- "))
a = 0
b = 0

for i in range(1,n+1):
    if i%2 == 0:
      a = a + i
    else:
       b = b + i

print(f"sum of even is {a} and odd sum is {b}") 

#print("sum of even is : ",a)
#print("sum of odd is : ",b)

'''

'''
n = int(input(" give me a val : "))

for i in range(1,n+1):
    if n%i == 0:
        print(i)
'''

'''
n = int(input(" give me the value :- "))
a = 0

for i in range(1,n+1):
    if i % 2 != 0:
        a = a + i

print(f"the sum of odd num is {a}")     
'''

'''
n = int(input(" give me the num "))

for i in range(n,0,-1):
    print(i)
'''

'''
n = int(input(" give me the val :- "))
a = 1

for i in range(1,n+1):
    a = i * i
    print(a)


n = int(input("give the number :- "))

for i in range(1,n+1):
   # print(f"{i} hellow world")
   print(i)


n = int(input(" give the value :- "))

for i in range(n,0,-1):
    print(i)

n = int(input("give the number to make the table :- "))

for i in range(1,11):
    print(f"{n} * {i} = {n*i}")


n = int(input("give the value :- "))
a = 0

for i in range(1,n+1):
    a = a + i

print(a)    


n = int(input("give the number :- "))
a = 1

for i in range(1,n+1):
    a = a * i

print(a)


n = int(input("give the val :- "))
a = 0
b = 0

for i in range(1,n+1):
    if i % 2 == 0:
        a = a + i
    else:
        b = b + i    

print(f"the sum of all even number {a} and sum of odd number is {b}")
 

n = int(input("give the val:- "))

for i in range(1,n+1):
    if n % i == 0:
        print(i)

        '''

'''
n = int(input("give the value :- "))
a = 0

for i in range(1,n):
    if n % i == 0:
        a = a + i
if a == n:
    print(f"{n} is a perfect number")        
else:
    print(f"{n} is not a perfect number")         
    '''
'''
n = int(input(" give me the value :- "))   

if n <= 1:
       print(f"{n} is not a prime number")
else:
      for i in range(2,n):
        if n % i == 0:
          print(f" {n} is not a prime number")
          break
        else:
          print(f"{n} is a prime number")  
'''            
'''
n = str(input("give me the string :- ")) 
a = ""

for i in range(len(n)-1,-1,-1):
    a = a + n[i]

if n == a:
        print("it is a pelindrome")
else :
        print("it is not a pelindrome")    

'''
'''
a =(input("give the input :- "))

char =""
spcsymbol = ""
dig = ""

for i in a:
    if i.isdigit():
        dig = dig + i
    elif i.isalpha():
        char = char + i
    else:
        spcsymbol = spcsymbol + i

print("character are = ",char) 
print("digits are = ",dig) 
print("special symbols are = ",spcsymbol)           

'''

'''
n = int(input("give me a number :- "))
a = 0

for i in range(1,n):
    if n % i == 0:
        a = a + i
   
if a == n :
    print("it is perfect number")
else:
    print("it is not a perfect number")

      '''


'''
n = int(input("give the number :- ")) 

for i in range(2,n):
    if n % i == 0:
        print(" it is a composite number")
        break
else :
   print("it is a prime number")
   


n = int(input("number batao :- "))

for i in range(2,(n//2)+1):
   if n % i == 0:
    print("your number is not prime")
    break

else:
  print("it is a prime number")   

'''
'''
n = str(input("give then string :- "))
c , b = "", ""

for i in n:
    if i.lower() in "aeiou":
        c = c + i
    elif i.isalpha():
        b = b + i        

print(f"vovels are :- {c}")
print(f"consonent are :- {b}")

# lower() it handle uppercase and cheak uppercase and lowercasr word are same or not
# isalpha() cheak is the word is alphabate or not


n = input("give the number :- ")

if n == n[::-1] :
    print("it is palendrone number") 
else :
    print("not a penlendrom number")       

    '''
'''
n = int(input("give the number :- "))

for i in range(2,(n//2)+1):
    if n % i == 0:
      print("composite number")
      break
else:
 print("prime number")

 '''

n = int(input("number batao:- "))





