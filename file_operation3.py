with open('codingal.txt','w') as file:
    file.write("Hi! I am penguin.")
file.close()

#split file into words
with open('codingal.txt','r') as file:
    data=file.readlines()
    for line in data:
        word=line.split()
        print(word)
file.close()   

updated=open('updated.txt',"w")
repeated=open('Repeated.txt','r')

duplicate=set()
for line in repeated:
    if line not in duplicate:
        updated.write(line)
        duplicate.add(line)
repeated.close()
updated.close()

import os
print('Checking if file exist or not')
os.remove("codingal.txt")

if os.path.exists("codingal.txt"):
   print('exist')
else:
    print("It does not exist")