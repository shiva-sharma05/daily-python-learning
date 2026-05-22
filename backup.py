'''
 a = 10
print(hex(id(a)))
# it is the memory address of variable a

# string sliceing

name = "shiva"
print(name[0:4])
'''
'''
attendence = 80
if attendence >= 85:
    print("never go college")
elif attendence >= 75:
    print("we will think")
else:
    print("jao college")       
    '''

# tenrary if else

#attendence = 45
#print("no college" if attendence >= 75 else "go college") 

#attendence = 65
#print("no college" if attendence >= 85 else "can go to college" if attendence >= 75 else "go to college")

''' 
for i in range (1,11):
    if i % 2 == 0:
       print(f"{i} is even number")
    else :
        print(f"{i} is not even")
    
for i in range(2,11,2):
    print(i)

'''
'''
list = [] 
1 can have multiple data type
2 can have duplicate 
3 list have unique things
4 you can change the value

age = [] # empty list
age = [21,22,23]
print(age[2])

l = [1,2,3,4,5,6,7]
l[3] = 10
'''

# rotate a list by k element

l = [10,20,30,40,50]

k = 2
for i in range(k):
    last = l[len(l)-1]
    for j in range(len(l)-1,0,-1):
        l[j] = l[j-1]
    l[0] = last

print(l)        


