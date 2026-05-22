def hello(name):
    print(f"hello {name} bhai haal chaaal badhiya")

hello("rishi")

def palindrome(n):
    rev = ""
    for i in n[::-1]:
        rev += i
        if rev == n:
         print("string is palindrome")
         break
    else:
        print("string is not palindrome")
            
def countvowels(n):
   count = ""
   for i in n:
      if i in "aeiou":
         count += i

   print(count)     

def copmarestrings(a,b):
   if len(a) == len(b):
      for i in range(len(a)):
         if a[i] != b[i]:
            print("strings are not same ")
            break
      else:
         print("strings are same") 
   else:
      print("strings are not same in length")    

def countall(n):
   digit =""
   alpha =""
   spcisymbol =""
   for i in n:
      if i.isdigit():
         digit += i
      elif i.isalpha():
         alpha += i
      else:
         spcisymbol += i

   print("digit are",digit) 
   print("alpha are",alpha)
   print("special symbol are",spcisymbol)     

def saprate(n):
   upper =""
   lower =""
   for i in n:
      if i.isupper():
         upper += i
      elif i.islower():
         lower += i

   print(lower+upper)

def revstring(n):
   print(n[::-1])

def getnumber():
    return 10

def add(a,b):
   return a+b

def countdigit(n):
   count = 0
   while n > 0:
      digit = n%10
      count += 1
      n = n//10
   print(count)   

def countsum(n):
   sum = 0
   while n > 0:
      digit = n%10
      sum += digit
      n = n//10
   print(sum)   

def cheakarmstrong(n):
   sum = 0
   copy = n
   length = len(str(n))
   while n > 0:
      digit = n%10
      power= digit**length
      n = n//10
      sum += power
   if sum == copy:
        print("number is armstrong")   
   else:
      print("not a armstrong number ")   

def printnum(n):
   i = 1
   while i <= n:
      print(i)  
      i += 1 
 
def printrev(n):
   i = n
   while i > 0:
      print (i)
      i -= 1

def printeven(n):
   i = 1
   while i <= n:
      i += 1
      if i % 2 == 0:
         print(i)
        
def printodd(n):
   i = 0
   while i <= n:
      if i % 2 != 0:
         print(i)
      i += 1   

def printtable(n):

   i = 1
   while i <= 10:
      print(f"{n} * {i} = {2*i}") 
      i += 1     

def numsum(n):
   sum = 0
   while n > 0:
      digit = n%10
      sum += digit
      n = n//10
   print(sum)   

def revnum(n):
   rev = 0
   while n > 0:
      digit = n%10
      rev = rev*10 + digit
      n = n//10
   print(rev)   

def cheakpallindrome(n):
   rev = 0
   copy = n
   while n > 0:
      digit = n%10
      rev = rev*10 + digit
      n = n//10  
   if rev == copy:
      print("number is pallindrome")
   else:
      print("not a pallindrome number")

def countnum(n):
   count = 0
   while n > 0:
      digit = n%10
      count += 1
      n = n//10
   print(count)

def factorial(n):
   i = 1
   fact = 1
   while i <= n:
      fact = fact * i
      i += 1     
   print(fact)

def armstrong(n):
   sum = 0
   copy = n
   length = len(str(n))
   while n > 0:
      digit = n%10
      power = digit**length
      sum += power
      n = n//10
   if copy == sum:
      print("number is armstrong")
   else:
      print("not a armstrong number") 

def fibonacci(n):
   i = 1
   a ,b = 0 ,1
   while i <= n:
      i += 1
      print(a)
      a ,b = b ,a+b

def allfactor(n):
   i = 1
   while i <= n:
      i += 1
      if n%i == 0:
         print(i)

def numprime(n):
   i = 0
   sum = 0
   while i <= n:
      i += 1
      if n % i == 0:
         sum += 1
   if sum == 2:
      print("num is prime")
   else:
      print("not a prime num")   


