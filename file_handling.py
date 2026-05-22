# file handling
'''
file = open('backup.py')
print(file.read())
file.close()
'''
'''
w - write mode (1. agar file created nhi hai toh create ho jayegi 2. agar purana data hai to overwrite ho jayega)
a- append mode 
r - read mode
x - create mode
'''

file = open('gangadhar.txt' , 'r')
# file.write('this content is adding using a (append) mode')
# file.close() 
# print(file.read())

for i in file:
    print(i)
file.close()    

# with statement
'''
with open('gangadhar.txt','r') as file:
    print(file.read())

with open('gangadhar.txt' , 'w') as file:
    file.write('content overwriten')
    print('done')

'''

from pathlib import path
p = path('shaktiman.txt')
if p.exists():
    print("file exists")
else:
    print('file does not exists')
