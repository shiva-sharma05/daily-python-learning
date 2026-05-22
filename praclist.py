#num = [1,2,3,4,5]

#num.append(6)
#num.insert(2,5)
#num.extend([5,5,5])
#num.remove(5)
#num.pop(3)
#num.count(5)
#num.sort()
#num.reverse()
#num.clear()
#print(num)

# Q1 print positive and negative element of an list
'''
l = [1,2,-3,-2,7,-3,8,3,-6,-7]

print("positive element are :")
for i in l:
    if i >= 0:
        print(i)

print("negative element are :")
for i in l:
    if i < 0:
        print(i)        
'''
# Q2 mean of list element
'''
l = [1,2,3,4,5,6,7]
sum = 0
for i in l:
    sum += i
print(sum/len(l))
'''
# Q3 find largest in list and index too
#l = [2,6,9,23,54,2,8]
#largest = l[0]
#index = 0

#for i in range(len(l)):
 #   if l[i] > largest:
  #      largest = l[i]
   #     index = i

#print(f"the largest num is {largest} at index {index}") 

# Q4 find the second largest
'''
largest = l[0]
seclargest = l[0]

for i in l:
     if i > largest:
          seclargest = largest
          largest = i
     elif i >= seclargest:
          seclargest = i     

print(seclargest,largest)   
'''
# Q5 cheak list is sorted or not 
'''
l = [2,5,8,12,34,56,67]

for i in range(len(l)-1):
    if l[i] < l[i+1]:
        continue
    else :
        print("list is not sorted")
        break
else:
    print("list is sorted")    
'''
'''
l = [1,2,-3,-2,7,-3,8,3,-6,-7]

print("positive numbers are : ")
for i in l :
    if i >= 0:
        print(i)

print(" negative num are : ")
for i in l:
    if i < 0:
        print(i)
        '''
'''
l = [1,2,3,4,5,6,7]
sum = 0

for i in l:
     sum += i

print(sum/len(l))     
'''
'''
l = [2,6,9,23,54,2,8]
largest = l[0]
index = 0

for i in range(len(l)-1):
    if l[i] > l[i+1]:
        largest = l[i]
        index = i

print(largest)      
'''

'''
l = [2,6,9,23,54,2,28]
largest = l[0]
seclargest = l[0]

for i in l:
    if i > largest:
        seclargest = largest
        largest = i
    elif i >= seclargest:
        seclargest = i   
       

print(seclargest,largest)        
'''
'''
l = [2,5,8,12,34,56,67]

for i in range(len(l)-1):
    if l[i] < l[i+1]:
        continue
    else:
        print("list is not sorted")
        break
else:
    print("list is sorted ")
  
      '''
'''
a = int(input("tell number of element : "))
l = []
for i in range(a):
    z = int(input("tell element"))
    l.append(z)

print(l)    
    '''
'''
a = [10,20,30,40,50]
#l = []
#1 a.reverse()

#2 for i in range(len(a)-1,-1,-1):
#     l.append(a[i])

z = len(a)-1

for i in range(len(a)//2):
    a[i],a[z] = a[z],a[i]
    z -= 1

print(a)    
    '''
'''
a = [12,43,76,78,98]
print("ans 1 ",a)

fruit = ["apple","banana","mango"]
print("ans 2 ",fruit)

print("ans 3 ",a[0])
print("ans 4 ",a[-1])

print("ans 5 ",len(a))

a.append(100)
print("ans 6 ",a)
     
a.remove(12)     
print("ans 7 ",a)
'''
'''
key = int(input("give the key :- "))
index = 0
for i in a :
    index += 1
    if key == i:
        print(f"{key} is present in the list at {index-1} index")
        break
else:
    print(f"{key} is not present in the list") 
     '''
'''
sum = 0
for i in a:
    print(i)  
    sum += i  

print("ans 10 ",sum)
'''
'''
# bubble sort
a = [56,12,34,54,23,65,54]
for j in range((len(a)-1)):
 for i in range(0,len(a)-1-j):
   if a[i] > a[i+1]:
      a[i],a[i+1] = a[i+1],a[i]

print(a)

#find the largest element with it index
a = [12,56,38,98,54,59,32,67]

largest = a[0]
index = 0

for i in range(len(a)-1):
  if a[i] > largest:
    largest = a[i]
    index = i

print(f"largest element is {largest} at the index {index}")

'''
'''
a = [12,56,38,98,54,59,32,67]
sum = 0
for i in a :
   sum += i
print(sum)   
'''
'''
a = [212,56,38,98,54,59,32,167]
min = a[0]
max = a[0]

for i in range(len(a)):
    if a[i] > max:
        max = a[i]       
    elif a[i] < min:
        min = a[i]
print(f"largest element in this list is {max} and smallest element is {min}")
'''
'''
a = [212,56,38,98,54,59,32,167]
z = len(a)-1
for i in range(len(a)//2):
    a[i],a[z] = a[z],a[i]
    z -= 1

print(a)
'''
'''
a = [212,56,38,98,54,59,32,167]
counteven = 0
countodd = 0

for i in a:
    if i%2 == 0:
        counteven += 1
    else:
        countodd += 1
print(f"odd nums are {countodd} and even are {counteven}")            

'''
'''
a = [212,56,38,98,54,59,32,167]

key =int(input("give the key :- "))

for i in a:
    if i == key:
        print(f"{key} is present in this list")
        break
else:
   print(f"{key} is not present in this list")
'''
'''
a = [23,54,33,87,34,98,33,36,33]
key = int(input("give the key :- "))
count = 0

for i in a:
    if i == key:
        count += 1
    
if count > 0 :
    print(f"key is present in list {count} times ")
else:
    print("key is not in the list ")    

'''
'''
l = [6,1,32,54,34,64,3,2]

for j in range(len(l)-1):
 for i in range(len(l)-1-j):
    if l[i] > l[i+1]:
        l[i],l[i+1] = l[i+1],l[i]

print(l)      
 '''
'''
l = [6,1,32,54,34,64,3,55]

largest = l[0]
seclargest = l[0]
largest_index = 0
seclargest_index = 0

for i in range(len(l)):
    if l[i] > largest:
        seclargest = largest
        largest = l[i]
        seclargest_index = largest_index
        largest_index = i
    elif l[i] > seclargest:
        seclargest = l[i]
        seclargest_index = i

print(f"largest element is {largest} at index {largest_index}")
print(f"second largest element is {seclargest} at index {seclargest_index}")
'''
'''
l = [6,1,32,54,34,64,3,2]
smallest = l[0]
secsmallest = l[0]
smallest_index = 0
secsmallest_index = 0

for i in range(1,len(l)):
    if l[i] < smallest:
        secsmallest = smallest
        smallest = l[i]
        secsmallest_index = smallest_index
        smallest_index = i
    elif l[i] < secsmallest:
        secsmallest = l[i]
        secsmallest_index = i    

print(f"smallest element is {smallest} at index {smallest_index}")
print(f"second smallest element is {secsmallest} at index {secsmallest_index}")
'''
'''
l = [1,3,5,6,8,23,12,3,6,8,3]
result = []
for i in l:
    if i  not in result:
        result.append(i)

print(result)   
     '''
'''
for i in l:
    found = False

    for j in result:
        if i == j:
            found = True
            break
    if found == False:
        result.append(i)
print(result)     
'''
'''
# check if list is sorted or not
l = [1,2,3,4,5,6,7]

for i in range(len(l)-1):
    if l[i] > l[i+1]:
        print("list is not sorted")
        break
else:
    print("list is sorted")    
'''
#paillndrome 
'''
l = [2,3,15,15,3,2]
for i in range(len(l)):
    if l[i] != l[len(l)-1-i]:
        print("list is not paillndrome")
        break
else:
    print("list is paillndrome")    
'''
'''
n = int(input("give the size"))
l = []
sum = 0
for i in range(n):
    a = int(input("give the element"))
    sum += a
    l.append(a)

print(l, sum)    
'''
'''
lst = list(map(int,input("enter the element: ").split()))
print(lst)

# map(data type input)
# split(seprate all the values and digit)
# list (convert the value in the form of list data structure)
'''
"""
sabse pehle inputs accept -> har input split hoga -> input will be
type casted in the form of int -> we sorted all the int value inside a list
"""
'''
# cheak list is sorted or not
l = [4,8,12,26,65,87,94]

for i in range(len(l)-1):
    if l[i] > l[i+1]:
        print('list is not sorted')
        break
else:
    print('list is sorted')   
    '''
'''
# check list is pallindrome or not 
l = [2,3,15,15,3,2]

for i in range(len(l)):
    if l[i] != l[len(l)-1-i]:
        print("list is not a pallindrome")
        break
else:
    print("list is pallindrome")    

       '''
'''
l = [1,2,3,4,5,8,7]

for i in range(len(l)):
    if l[i] > l[i+1]:
        print('list is not sorted')
        break
else :
    print("list is sorted")        

'''
'''
l = [2,3,15,15,3,2]
for i in range(len(l)):
    if l[i] != l[len(l)-1-i]:
        print('list is not palindrome')
        break
else:
    print("list is palindrome")

'''
'''
n =int(input("num batao "))
sum = 0
mul = 1
while n > 0:
    digit = n%10
    sum += digit
    mul *= digit
    n = n//10

if mul == sum :
    print("it is a spy number")
else:
    print("not a spy number")        
'''
'''
n= int(input("num batao "))
i = 1
while i<=n:

    print(i)
    i += 1
'''
'''
# Find the greatest element and print its index too.
l = [2, 96, 69, 77, 145, 20]
max = l[0]
index = 0
for i in range(len(l)):
  if l[i] > max :
    max = l[i]
    index = i

print(f"max element is {max} at index {index}")

'''
'''
n = int(input("give the size of the list :- "))
l = []

for i in range(n):
    a = int(input("tell the element :- "))
    l.append(a)

print(l)

max = l[0]
for i in l:
    if i > max:
        max = i

print(f" the biggest num in this list is {max}")        

'''
'''
n = int(input("tell the number of element"))
l = []
for i in range(n):
    s = int(input("tell element :- "))
    l.append(s)

print(l)

min = l[0]
for i in l:
    if i < min:
        min = i

print(f"the smallest element in the list is {min}")        
'''
'''
n = int(input("tell the num of element :- "))
l = []
for i in range(n):
    s = int(input("tell element :- "))
    l.append(s)

sum = 0
for i in l:
    sum += i

print(f"sum of all the element is {sum}" )    
        
'''
'''
n = int(input("tell the number of element :- "))
l = []

for i in range(n):
    s = int(input("tell element :- "))
    l.append(s)

print(l)

count = 0
for i in l:
    if i % 2 == 0:
        print(i)
'''
'''
n = int(input("tell the number of element :- "))
l =[]

for i in range(n):
    s = int(input(" tell the element :- "))
    l.append(s)

print(l)

for i in l:
    if i % 2 != 0:
        print(i)
      
'''
'''
n = int(input("tell the number of element :- "))
l = []

for i in range(n):
    s= int(input("tell element :- "))
    l.append(s)

print(l)

d = len(l)-1
for i in range(len(l)//2):
    l[i],l[d] = l[d],l[i]
    d -= 1

print(l)    
'''
'''
n = int(input("tell the number of element :- "))
l = []

for i in range(n):
    s= int(input("tell element :- "))
    l.append(s)
    

print(l)


for i in l:
    if i not in l:
        print(i)
'''
'''
l = [1,2,3,4,5] # op = k = 2 [4,5,1,2,3]
k = 2
for i in range(k): # i = 0,1
    last = l[-1] # last value 5
    for j in range(len(l)-1,0,-1): # j -> 4,3,2,1
        l[j] = l[j-1]
    l[0] = last
print(l)       
'''
'''
# assign all the 0s at the end of the list
l = [1,0,4,0,12]
j = 0
for i in range(len(l)):
    if l[i] != 0:
        l[i],l[j] = l[j],l[i]
        j = j+1
print(l)        

'''
'''
l = [1,2,3,4,5]
k = 2 
for i in range(k):
    last = l[-1]
    for j in range(len(l)-1,0,-1):
        l[j] = l[j-1]
    l[0] = last
print(l)  
'''
'''
l = [1,0,4,0,12]
j = 0
for i in range(len(l)):
    if l[i] != 0:
        l[i],l[j] = l[j],l[i]
        j = j+1
print(l)    
'''
    