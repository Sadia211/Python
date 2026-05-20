file1=open("f1.txt",'r')
file2=open("f2.txt",'w')

count=0
for line in file1.readlines():
    if not(line.startswith('Coding')):
        print(line)
        file2.write(line)
        count=count+1
print("Total lines copied:",count)
file1.close()
file2.close()