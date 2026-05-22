#n = int(input("give the number"))
#sum = 0

#while n > 0:
 #   sum = sum + (n%10)
  #  n = n//10

#print(sum)

#reverse a number
''' 
n = int(input("give the number :- "))
rev = 0
copy = n

while n > 0:
    rev = rev * 10+(n % 10)
    n = n//10

print(rev)
if copy == rev:
    print("palindrome")
else:
    print("not palindrome")

'''
'''

import random
num = random.randint(1,51)
tries = 0
#print(num)

while True:
    n = int(input("entre your number :- "))
    if num == n:
        tries += 1
        print("you are winner")
        print(f"you guess the number in {tries} try") 
        break
    elif num > n:
        tries += 1
        print(" you are guessing lower") 
    elif num < n:
        tries += 1
        print(" you are guessing higher")      
    else:
        tries += 1
        print("you guessing wrong")   
   '''
'''
n = int(input("enter your digit :- ")) 
digit = ""

#print(n[::-1])    

for i in str(n)[::-1]:
    digit += i

print(digit)        
'''
'''
n = int(input("enter the range :- " ))
a = 0
b = 1

for i in range(n):
  print(a)
  a , b = b ,a + b
'''
'''
# print the largest digit in a number

n = (input("enter the value :- "))
largest = 0

for i in str(n):
    a = int(i)
    if largest < a:
        largest = a

print(largest)

'''
'''
#Q4 guessing game

import random

n = random.randint(1,50)
print(n)

for i in range(5):
    num  = int(input("enter your number :- "))
    if num == n:
        print("you won")
        break

    if num < n:
        print("you gussing smaller")   

    if num > n:
        print("you gussing higher")        

else:
    print("bhaiya haar gaye")    
    '''
'''
# cheak a num is paillndrom or not

num = 1221
if str(num) == str(num)[::-1]:
    print(f"{num} is paillndrom") 
else:
    print(f"{num} is not paillndeom")      

    '''

# keep taking input until user enters 0 and print sum
'''
sum = 0

while True :
    n = int(input("enter your number :- "))
    if n == 0:
        break
    sum += n

print(sum)    
'''
'''
# armstrong number or not

n = 153
copy = n
length = len(str(n))
sum = 0

while n > 0:
    digit = n%10
    sum += digit**length
    n = n // 10

if copy == sum:
    print("armstrong number")
else:
    print("not")    
'''
'''
n = int(input(" number batao :- "))
a = 0
b = 1
while a <= n:
  print(a)
  a =  b
  b = a + b
 '''
# when we use return statement we use print function to print it
def countdigit(n):
 count = 0
 while n > 0:
    digit = n%10
    count += 1
    n = n//10

 return(count)

# find the sum of the number (eg -> 123 = 6)
def countsum(n:int):
  count = 0
  while n > 0:
    digit = n%10
    count += digit
    n = n//10
  return(count)  

# cheak a number is armstrong or not
def cheakarmstrong(n):
  copy = n
  sum = 0
  length = len(str(n))
  while n > 0:
     digit = n%10
     power = digit**length
     n = n//10
     sum += power
  if sum == copy:
    print("number is armstrong") 
  else:
    print("not a armstrong number")
 

def cheakpalindrome(n):
  copy = n
  rev = 0

  while n > 0:
    digit = n%10
    rev = rev*10 + digit
    n = n//10

  if copy == rev:
     print(' number is palindrome')
  else:
     print('number is not palindrome')  
  

def armstrong(n):
  sum = 0
  copy = n
  length = len(str(n))

  while n > 0:
    digit = n%10
    power = digit**length
    sum += power
    n = n//10

  if sum == copy:
    print("num is armstrong")
  else:
    print("num is not armstrong")    
  
def greet(a,b,c,d,e=str):
  
  print(f"{a} {b} {c} {d} {e} bhaiyo kaise ho aap")


greet(7,"vikash","shiva","rishi",7)
