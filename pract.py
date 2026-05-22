'''
n = int(input("give the number :- "))
i = 1
while i <= n:
    print(i)
    i += 1

'''
'''
n = int(input("number batao :- "))
i = 1
while i <= n :
        print(i)
    i = i + n

'''
'''
n = 1234
digit =""
for i in str(n)[::-1]:
    digit += i

print(digit)    

'''
'''
# sum of the number 
n = 1234
sum = 0
for i in range (n):
    sum = sum + n%10
    n = n // 10

print(sum)
 '''
'''
n = 1215
rev = 0
copy = n

while n > 0:
    digit = n%10
    rev = rev * 10 + digit
    n = n//10

print(sum)    
if copy == rev :
    print("palindrome") 
else:
    print("not palindrome")       
'''
'''
n = int(input("nuber batao :- "))
a,b = 0,1
while a <= n:
    print(a)
    a,b = b,a+b
'''
'''
# keep takeing input until user inter 0 and print it sum
sum = 0

while True:
    n = int(input("batate raho number :- "))
    if n==0:
        break
    sum += n
print(sum)    
'''

'''
# armstrong number

n = 153

copy = n
length = len (str(n))
sum = 0

while n > 0:
    digit = n%10
    sum += digit**length
    n = n//10

if copy == sum:
    print("armstrong number")  
else:
    print("not a armstrong number")      
'''
'''
n = int(input("number batao :- "))
a = 1

while n > 0:
    a = a*n
    n = n-1

print(a)    
'''
'''
n = int(input("give the number :- "))
copy = n
rev = 0
length = len(n) 
while n > 0:
    digit = n%10
    rev += digit**length
    n = n//10

if copy == rev:
    print("armstrong number")
else:
    print("not a armstrong number")        
'''
'''
n = int(input("number batao :- "))
copy = n

rev = 0
while n > 0 :
    digit = n%10
    rev = rev * 10 + digit
    n = n//10
if copy == rev:
    print("palindrome")
else:
    print("not palindrome") 
'''
'''
n = int(input("number batao :- "))
rev = 0

#print(str(n)[::-1])
#for i in str(n)[::-1]:
 #   print(i,end="")
while n > 0:
    digit = n%10
    rev = rev * 10 + digit
    n = n//10

print(rev) 
'''
'''
n = int(input("number batao :- "))  
i = 1
while i <= n :
    if i % 2 == 0:
        print(f"{i} is even number")
    else:
        print(f"{i} is odd number")  

    i += 1
'''
'''
n = int(input("number batao :- "))
sum = 0
while n > 0:
    digit = n%10
    sum = sum + digit
    n = n//10

print(sum)
'''
'''
n = int(input("number batao :- "))
rev = 0
while n > 0:
    digit = n%10
    rev = rev*10 + digit
    n = n//10

print(rev)    
'''
'''
n = int(input("number batao :- "))
rev = 0
copy = n
while n > 0:
    digit = n%10
    rev = rev*10 + digit
    n = n//10
if copy == rev:
    print("palindrome")
else:
    print("not a palindrome")
    '''
'''
n = int(input("number batao :- "))    
sum = 0
length = len (str(n))
copy = n
while n > 0:
    digit = n%10
    sum += digit**length
    n = n//10
if sum == copy:
    print("armstrong number")
else:
    print("not a armstrong number")  
    '''
'''
n = int(input("number batao :- "))  
i = 1
a,b = 0,1

while n >= i:
   print(a)
   a,b = b,a+b
   i += 1
   '''
'''
n = int(input("number batao :- "))
i = 1
fact = 1
while i <= n:
    fact = fact * i
    i += 1

print(fact)    
'''
'''
n = int(input("number batao :- "))
rev = 0
copy = n

while n > 0:
    digit = n%10
    rev = rev * 10 + digit
    n = n//10

if copy == rev:
    print("palindrome") 
else:
    print("not a palindrome")       
'''
n = int(input("number batao :- "))
a = 0
b = 1
for i in range(n):
    print(a)
    a,b = b,a+b
