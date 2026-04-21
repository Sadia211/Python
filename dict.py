my_dict={1:'apple',2:'orange'}
print(my_dict)
 
student={'name':'Jack', 'class':7}
print(student)
print(student.get('name'))

#Update a value
student['class']=8
print(student)

#add a value
student['phone']=999294
print(student)

#remove a particular element
student.pop('class')
print(student)