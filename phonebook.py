import sys
#Create initial phonebook
def initial_phonebook():
    rows,cols=int(input("Please enter initial number of contacts")),5
    phone_book=[]

    for i in range(rows):
        print("\n  Enter contact  details"  % (i+1))
        temp=[]

        for j in range(cols):
            if j==0:
                temp.append(str(input("Enter name:")))
                if temp[j]==" ":
                    sys.exit("Name is mandatory!")
                
            if j==1:
                temp.append(int(input("Enter number:")))

            if j==2:
                temp.append(str(input("Enter email:")))
                if temp[j]==" ":
                   temp[j]=None
            
            if j==3:
                 temp.append(str(input("Enter DOB:")))
                 if temp[j]==" ":
                   temp[j]=None
            
            if j==4:
                 temp.append(str(input("Enter Category:")))
                 if temp[j]==" ":
                   temp[j]=None

        phone_book.append(temp)  

#Menu
def Menu():
    print("\n 1.ADD")
    print("2.Remove")
    print("3.Delete all")
    print("4.Display All")
    print("5.Exit")
    return int(input("Enter Choice"))

def add(pb):
    temp=[]
    print('Enter new contact details')

    temp.append(input("Enter name:"))
    temp.append(int(input("Enter number:")))

    email=input("Enter email:")
    temp.append(email if email else None)

    dob=input("Enter DOB:")
    temp.append(dob if dob else None)

    category=input("Enter category:")
    temp.append(category if category else None)

    pb.append(temp)
    print("Contact added succesfully")
    return pb
    
def remove(pb):
    name=input("Enter name to remove:")

    for contact in pb:
        if contact[0]==name:
            pb.remove(contact)
            print("Contact removed successfully")
            return pb
        print("Contact not found")
        return pb
    
def display(pb):
    if not pb:
        print("List is empty")
    else:
        for i in range(len(pb)):
            print(pb[i])

print("Welcome to phone book")
pb=initial_phonebook()
while True:
    ch=Menu()
    if ch==1:
        pb=add(pb)
    elif ch==2:
        pb=remove(pb)

    elif ch==4:
        display(pb)

    elif ch==5:
        print("Goodbye")
        break