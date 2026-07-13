#Python fundamentals
"""Task one: Write a program for a hospital where we check in 
a patient named John Smith.He is 20 years old and is a new patient"""

name = "John Smith"
age = 20
isPatientNew = True 
print(name)
print(age)
print(isPatientNew)

"""Task two: Write a program to ask two questions,person's name and favorite 
color and then print a message like "Mosh likes blue" """

name = input("What is your name? ")
color = input("What is your favorite color? ")
print(name + " likes " + color )

"""Type conversion task:Write a program that asks the year we are born in then it will 
calculate our age and print it on the terminal"""

birth_year = input('What year were you born in? ')
current_year = input('What is the current year? ')
age=int(current_year) - int(birth_year)
print(age)

"""Task three:Ask a user their weight(in pounds),convert it to kilograms and print 
on the terminal"""

weight_in_pounds= input("What is your weight in pounds? ")
weight_in_kilorgrams = int(weight_in_pounds) * 0.45
print(weight_in_kilorgrams)

"""Exercise:Define a variable called name and assign it a value called Jennifer then
Print(name[1:-1]) and determine what will be displayed"""
name = 'Jennifer'
print(name[1:-1])

