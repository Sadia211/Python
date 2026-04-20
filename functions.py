def greet(name):
    print("Hello " + name +".Good Morning")
greet('Penguin')
greet('Cody')


print('Finding absolute number')

def absolute_num(num):
    if num>=0:
        return num
    else:
        return -num
print ("Absolute value of the number is" ,absolute_num(89))
print ("Absolute value of the number is" ,absolute_num(-189))


print('Finding out palindromes')
def palindrome(word):
   if word==word[::-1]:
      return True
   else:
      return False


if palindrome('madam'):
 print('The word is palindrome')
else:
 print('The word is not palindrome')

   
