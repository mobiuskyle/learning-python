"variables,input and type conversion"
## exercise 1 - prints name and age
name=input('What is your name? ')
age=input('What is your age? ')
nextAge = int(age)+1
print(f"Hello [{name}] next year you'll be [{nextAge}]")

## exercise 2 - temperature converter program
temperatureCelcius = input('What is the current temperature? ')
temperatureFahr = int(temperatureCelcius)*(9/5) + 32
print(f'The temperature is {temperatureFahr} Fahrenheits')

"Strings , Formatted Strings and String Methods"
## exercise 3  - case converter program
full_name = input('What is your Full name? ')
print(full_name.lower())
print(full_name.upper())
print(full_name[::-1])

## exercise 4
sentence = input('Write any random sentence of your choice : ')
sentence_characters = len(sentence)
print(f'this sentence has {sentence_characters} characters')
if sentence[0] == sentence[0].upper():
    print('the first letter is in capital')
else:
    print('the first letter is in lowercase')

##exercise 5 -simple username generator
f_name = input('What is your First name? ')
l_name = input('What is your Last name? ')
print(f'your username could be [{f_name[0:3].lower()}{l_name.lower()} @gmail.com]')

##exercise 6 - palindrome checker
word = input('Enter any word to check if it is a palindrome : ')
print(word.lower())
print(word[::-1].lower())
if word.lower()== word[::-1].lower():
    print('It is a palindrome')
else:
    print('it is not a palindrome')

"Arithmetic,Operator Precedence and Math Function"
## exercise 7 - tip calculator
bill_amount = float(input('Enter the bill amount : '))
tip_percentage = float(input('Enter the tip percentage : '))
tip_amount = (bill_amount)*(tip_percentage/100)
total = bill_amount + tip_amount
print('Your total is : ',total)
print('Yout tip amount is : ',tip_amount)

## exercise 8 
first_number = float(input('Enter the first number : '))
second_number = float(input('Enter the second number : '))
third_number = float(input('Enter the third number : '))
average = (first_number+second_number+third_number)//3
print(f'the average of the three numbers is {average}')

## exercise 9 - checks if number is even or odd
number = int(input('enter number : '))
if number%2==0:
    print('Number is even')
else:
    print('Number is odd')

## exercise 10 - simple grade display program
score = int(input('Enter score : '))
if score>=0 and score<=100:
    if score>=90:
        print("You have a Grade A")
    elif score>=80 and score<=89:
        print("You have a Grade B ")
    elif score>=70 and score<=79:
        print("You have a Grade C ")
    else:
        print("You have a Grade F ")
else:
    print("Number is Invalid,should be within the range of 0-100")
## exercise 11 - login checker
fixed_username = 'mobiuskyle'
fixed_password = 'BLACKPINK'
username = input('enter username : ')
password = input('enter password : ')
if username==fixed_username and password==fixed_password:
    print('Access Granted')
else:
    print('Access denied')