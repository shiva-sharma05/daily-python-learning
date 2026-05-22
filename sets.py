# sets are unordered
# semi-mutable (can add ,but cannot change or removed)
# unique element (no duplicate)
# hetergeneous (can contain diffrent data type) 

#s = {1,2,3,4,5}

#print(type(s))

# method in sets
""" 
1 add()
2 update()
3 remove ()
4 discard ()
5 pop ()
6 clear ()
 """

# 1 add
s = {10,1,2,3,5,4,3,2}
s.add(6)

# update 
s.update([7,8,9]) 

# remove
# s.remove(1)

#discard
#s.discard(10)

# pop
s.pop()

# clear
"""s.clear()
print(s)"""

"""
a = {1,2,3,4}
b = {2,3,4,6}
print(f"Intersection : {a.intersection(b)}")
print(f"union : {a.union(b)}")
print(f"diffrence : {a.difference(b)}")
print(f"symmetric_diffrence : {a.symmetric_difference(b)}")
"""

fs = {10,20,30,40,50}

fs = frozenset(fs)
fs.add(60)
fs.remove(10)

print(fs)

