'''
s = "Shery"
print(s[::-1])
print(len(s))
print("string in upper format ;- ",s.upper())
print("string in lower format :- ",s.lower())
'''
# 
'''
s = "ShEry"
lower ="" 
upper =""
for i in s:
    if i.islower():
        lower = lower + i
    elif i.isupper():
        upper = upper + i

print(lower+upper)        
       '''
'''
str1 = "PSDA4547$%%#^^"
alpha = 0
digit = 0
special =0
for i in str1:
    if i.isalpha():
        alpha = alpha+1
    elif i.isdigit():
        digit += 1
    else:
        special += 1

print(f"alpha count : {alpha}")   
print(f"digit count : {digit}") 
print(f"special count : {special}")  
'''
'''
str1 = "hello"
str2 = "hello"
if len(str1) == len(str2):
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            print("string are not same")
            break
    else:
        print("string are same ") 
else:
    print("both strings are not same be same length")   
    '''
'''
def countvowels(str1):

   count = 0
   for i in str1:
    if i in "aeiouAEIOU":
        count += 1
   return(f"total count of vowels are : {count}")    

print(countvowels("hello"))   
'''
'''
# reverse a string
str1 = "shiva"
rev = ""
#print(str1[::-1])
for i in str1[::-1]:
    rev += i

print(rev)    
'''
'''
# check string is pallindrome is not
def pallindrome(str1):
   rev = str1[::-1]
   if str1 == rev:
    print("string is pallindrome")
    
   else:
    print("string is not pallindrome")

pallindrome("shiva")   
'''
# count vowels and consonent from an string
'''
str1 = "shiva" 
vowels =""
conso = "" 
for i in str1:
    if i in "aeiouAEIOU":
        vowels += i
    else:
       conso += i

print(f"vowels are {vowels}")
print(f"consonent are {conso}")
'''

