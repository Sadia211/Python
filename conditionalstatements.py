
#even odd

number = int(input("Enter Number to Check"))
print("Number to be checked :", number)

if number>0:
  print("This is a positive number")

elif number<0:
  print("This is a negative number")

else:
  print("This is neutral")








  #odd even
  number = int(input("Enter Number to check"))
print("Number to be checked :", number)

if number%2==0 :
  print("This is an even number")

else:
  print("This is an odd number")







# lists
lst = ['Apple', 'Guava', 'Mango', 'Banana', 'Kiwi']

print("Length of list:", len(lst))
print("First Element:", lst[0])
print("Last Element:", lst[-1])

lst.append('Papaya')
print("Updated List :", lst)

lst.remove('Guava')
print("Updated List :", lst)

lst.sort()
print("Sorted List:", lst)

lst.pop(1)
print("Updated List :", lst)

lst.reverse()
print("Reversed List :", lst)


