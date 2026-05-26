var choice=prompt("Welcome to Area Calculator.\n Please Enter your choice.\n1.Area of Rectangle \n2.Area of Triangle \n3.Area of circle.")

if(choice=='1'){
  var length=prompt('Enter the Length')
  var width=prompt("Enter the width")
  var result=length*width
  alert('The area is'+result)
}
if (choice=='2'){
  var height=prompt("Enter the height")
  var base=prompt("Enter the base")
  var area=height*(base)/2
  alert('The area is '+ area)
}