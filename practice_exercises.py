""""variables,input and type conversion"
## exercise 1
name=input('What is your name? ')
age=input('What is your age? ')
nextAge = int(age)+1
print(f"Hello [{name}] next year you'll be [{nextAge}]")

## exercise 2
temperatureCelcius = input('What is the current temperature? ')
temperatureFahr = int(temperatureCelcius)*(9/5) + 32
print(f'The temperature is {temperatureFahr} Fahrenheits')

"Strings , Formatted Strings and String Methods"
## exercise 3 
full_name = input('What is your Full name? ')
print(full_name.lower())
print(full_name.upper())
print(full_name[::-1])"""

## exercise 4
sentence = input('Write any random sentence of your choice : ')
sentence_characters = len(sentence)
print(f'this sentence has {sentence_characters} characters')
if sentence[0] == sentence[0].upper():
    print('the first letter is in capital')
else:
    print('the first letter is in lowercase')
