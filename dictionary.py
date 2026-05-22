'''
d1 = {1:10,2:20,3:30}
d2 = {3:40,5:50,6:60}

for i in d2:
     if i in d1.keys():
          d1[i] = d1[i] + d2[i]
     else:     
          d1[i] = d2[i]

print(d1)

l = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6]
d= {}

for i in l:
   if i in d.keys():
     d[i] = d[i] + 1
   else:
       d[i] = i

print(d)         
'''
'''
d1 = {1:10,2:20,3:30}
d2 = {4:40,5:50,6:60}

for i in d2:
    d1 [i] = d2 [i]

print(d1)    
    '''
"""
l = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6]
d = {}

for i in l:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

print(f"frequency of element : {d} ") 

"""
'''
d1 = {1:10,2:20,3:30}
d2 = {3:30,5:50,6:60}

for i in d2:
    if i in d1.keys():
        d1[i] = d1[i] + d2[i]
    else:
        d1[i] = d2[i]

print(d1)    

'''

nums = [1,3,2,1,3,2,2]
d = {}

for i in nums:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

pair = 0
leftover = 0
for i in d.values():
    pair += i//2
    leftover += i%2 

print(f"pair are {pair} and left over is {leftover}")