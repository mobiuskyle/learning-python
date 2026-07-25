"""Arithmetic Operations supported in Python include:
i)Addition
ii)Subtraction
iii)Multiplication
iv)Division
v)Modulus
vi)Exponential
vii)increment and decrement

"""
x=10
y=3
print(x+y) #Addition
print(x-y)#Subtraction
print(x*y)#Multiplication
print(x/y)#Division - returns the value as it is 
print(x//y)#Division - returns the whole value
print(x%y)#Modulus - returns the remainder
#x=x+3 can also be written as x+=3
x+=3 #increment
print(x)
#y=y-1 can also be written as y-=1
y-=1 #Decrement
print(y)
print(x**y)#exponential

"""Task
Ask the user for two values a and b then ,Add code to print three lines where:

i)The first line contains the sum of the two numbers.
ii)The second line contains the difference of the two numbers (first - second).
iii)The third line contains the product of the two numbers.
iv)the fourth line contains the division of the two numbers 
v)the fifth line contains the float division of the two numbers"""

a=int(input("What is the value of a :"))
b=float(input("What is the value of b :"))
sum=a+b
difference = a-b
product=a*b
division = a/b
floatDivision = a//b
print("the sum of a and b is : ",sum)
print("the difference of a and b is : ",difference)
print("the product af a and b is : ",product)
print("the division of a and b is : ",division)
print("the float division of a and b is : ",floatDivision)
