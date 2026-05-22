# tuples 
'''
1 tuples are orderd (indexing)
2 can have duplicacy 
3 are hetrogenous 
4 are immutable 
'''

t = () # empty tuples 
t = (1,2,3,4,5) 
'''
index loop
for i in range(len(t)):
    print(i,t[i])

direct loop 
for i in l:
    print(i)    
'''
'''
# for value and index both
for index , value in enumerate(t):
    print(index,value)
'''
# methods in tuples 
'''
1 count()
2 index()
'''
t = (1,2,2,2,2,3,3,3,4,5)
print(t.count(2))
print(t.count(3))

print(t.index(2)) # frist occourence of 2

print(3 in t)

# tuple unpacking and packing
t = (1,2,3,4,5)
# a,b,c,d,e, = t unpacking

a = 1,2 # this is packing

# star expression (*)
t = (1,2,3,4,5)
'''
a,*b= t
print(a)
print(b)
'''
a,*b,c = t
print(a)
print(b)
print(c)

t1 = (1,2,3)
t2 = (4,5,6)
print(t1+t2)

 
