class Parrot:
    species='bird'

    def __init__(self,name,age):
        self.name=name
        self.age=age

bluey=Parrot("Bluey",10)
 

print(bluey.name,'is',bluey.age,"years") 


#code 2 

class student:
    stream='coding'

    def __init__(self,roll,address):
        self.roll=roll
        self.address=address
 
student1= student(405,'Shantinagar,Dhaka')
print("Student's roll no is",student1.roll," Student's address is",student1.address)