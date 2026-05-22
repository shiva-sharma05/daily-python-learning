'''
1
n = "shiva"
print(n[::-1])
print(n.upper())
print(n.lower())
print(len(n))
'''
'''
2
n = "ShiVA shaRma"
upper = ""
lower ="" 
for i in n :
    if i.islower():
        lower += i
    elif i.isupper():
        upper += i 

print(lower+upper)
'''
'''
3
n = "pwhf@$8765FGI^*&^%"
digit =""
alpha =""
spcichar =""
for i in n:
    if i.isalpha():
        alpha += i
    elif i.isdigit():
        digit += i
    else:
        spcichar += i        

print("digit are ",digit)
print("alphabates are ",alpha)
print("spcial char are ",spcichar)
'''
'''
4
str1 = "shiva"
str2 = "shivA"

if len(str1) == len(str2):
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            print("strings are not equal")
            break
    else:
         print("string are  equal")
else:
    print("string are not equal in the length")            
'''
'''
5
n = "how are you"
count = 0
for i in n:
    if i in "aeiou":
       count += 1
    
print(count)    
      '''
'''
6
n = "shiva sharma"
print(n[::-1])        
'''

7
n = "shihs"
rev = ""
for i in n[::-1]:
    rev += i

if rev == n:
    print("string is palindrome")    
else:
    print("string is not a palindrome")       

    