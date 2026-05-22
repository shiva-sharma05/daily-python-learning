# logical operator 
 
# 1 is and 
'''
print(123 == 123 and 143 ==143)

cgpa = float(input("WHAT IS YOUR CGPA :- "))
back = int(input("HOW MANY BACKS YOU HAVE NOW :- "))

if(cgpa >= 7.00 and back <=1 ):
    print("YOU ARE ABLE FOR THIS COMPANY ")
    print("YOU ARE SELECTED FOR CODING ROUND")
else:
    print("YOU ARE NOT ABLE FOR THIS COMPANY")    
'''

print("GAME : GUESS THE NUMBER IN HUNDERD")
b = 67

while True:
 a = int(input(" WHAT IS YOUR NUMBER :- "))
if(a < 0 or a > 100):
    print("ERROR : INVALID INPUT")
    break
elif a == b:
    print("YOU GUESS THE NUMBER")
    break          
elif a < 59:
    print("YOU GUESSING VERY LOW")
elif a > 71:
    print("YOU GUESSING VERY HIGH")    
elif a > 60 and a > 70:
    print("YOU ARE VERY NEAR")  

else :
    print("ERROR : INVALD INPUT")       
    print("TRY AGAIN")
    