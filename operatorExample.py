
# importing operator module 
import operator
  
# taking input
a = int(input("insert a number: "))
b = int(input("insert another number: "))
  

# using add() to add two numbers
print ("The addition of numbers is :",end="");
print (operator.add(a, b))
  
# using sub() to subtract two numbers
print ("The difference of numbers is :",end="");
print (operator.sub(a, b))
  
# using mul() to multiply two numbers
print ("The product of numbers is :",end="");
print (operator.mul(a, b))

# using truediv() to divide two numbers
print ("The true division of numbers is : ",end="");
print (operator.truediv(a,b))

# using floordiv() to divide two numbers
print ("The floor division of numbers is : ",end="");
print (operator.floordiv(a,b))

# using pow() to exponentiate two numbers
print ("The exponentiation of numbers is : ",end="");
print (operator.pow(a,b))

# using mod() to take modulus of two numbers
print ("The modulus of numbers is : ",end="");
print (operator.mod(a,b))
