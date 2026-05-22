# for creating list you have to use square bracket ( [] )
#l = [12,13,14,15,16]

# speical power
# 1 hetrogeneous nature
# it can store any kind of data type at once
# eg
#l = [12,"hello",12.67,True,print()]

# 2 ordered 
# every element in list has a designated position

# 3 muteable nature
# you can change anything inside the list at any point at time

# duplicates 
# you can store duplicates element inside the list

#a = [10,20,30,40,70]

#print(a)
#print(a[2],a[-1])

# updating a list

#a[-1] = 50
#print(a)

# delete 
# you can delete a single element and entire list

#del a[-1]
#print(a)

# creating loops on a list

# based on value

#for i in a:
 #   print(i)


# here you will access all the value    

# based on index

#for i in range(0,len(a)):
 #   print(a[i])

# this loop can assess your index as well as your value and it give more
# control over the list

# methods 
#a.append(50)
#l = []

#for i in range(10,51,10):
#    l.append(i)

#print(l)    

#l.insert(2,60)

#a = [2,3,4]
#a.clear()
#print[a]

#a = [10,20,30,10]

#saved = a.pop(1)
#a.remove(10)
#print(a)
'''
#Q1 
a = int(input("how many element you want : "))

l= []

for i in range(a):
    z = int(input("tell your number : "))
    l.append(z)
    l.sort()

print(l)    
'''
#a = eval(input("tell your string"))
#print(a)
'''
#Q2
a = [10,20,30,40,50]

#l =[]

#for i in range(len(a)-1,-1,-1):
 #   l.append(a[i])

#print(l)    

z = len(a)-1

for i in range(len(a)//2):
    a[i],a[z] = a[z],a[i]
    z = z-1

print(a)    
'''
'''
#Q3
a = [1,2,5,-4,-7,6,-5,6]
print("positive num are")
for i in a:
    if i >= 0:
        print(i)

print("negative num are")
for i in a:
    if i < 0:
        print(i)     
'''
'''
# bubble sort
a = [12,34,13,65,62,36,67]
for j in range(len(a)-1):
  for i in range(0,len(a)-1-j):
    if a[i] > a[i+1]:
        a[i],a[i+1] = a[i+1],a[i]

print(a)        
'''
'''
a = [12,56,38,98,54,59,32,67]

largest = a[0]
index = 0

for i in range(1,len(a)):
    if a[i] > largest:
        largest = a[i]
        index = i

print(largest,index)
'''
'''
l = [6,1,32,54,34,64,6,3,51]
largest = l[0]
s_largest = l[0]
seclargest_largest = 0
largest_index = 0
for i in range(1,len(l)):
    if l[i] > largest:
        s_largest = largest 
        largest = l[i]
        seclargest_largest = largest_index
        largest_index = i

    elif l[i] > s_largest:
        s_largest = l[i]    
        seclargest_largest = i

print(largest,largest_index)   
print(s_largest,seclargest_largest)  

'''
l = [6,1,32,54,34,64,3,2]

smallest = l[0]
secsmallest = l[0]
secsmallest_index = 0
smallest_index = 0

for i in range(1,len(l)):
    if l[i] < smallest:
        secsmallest = smallest
        secsmallest_index = smallest_index
        smallest = l[i]
        smallest_index = i
    elif l[i] < secsmallest:
        secsmallest = l[i]
        secsmallest_index = i

print(smallest,smallest_index)
print(secsmallest,secsmallest_index)
