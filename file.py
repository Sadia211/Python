#open file in read mode
file=open('sample.txt')
print(file.read())
file.close()

#open file in write mode
file=open('sample.txt','w')
file.write("File in write mode")
file.close()

#open file in append mode
file=open('sample.txt','a')
file.write("\n Adding an extra line.")
file.close()

file=open("sample.txt","r")
lines=file.readlines()
print(len(lines))