#variables,input and type conversion
## exercise 1
name=input('What is your name? ')
age=input('What is your age? ')
nextAge = int(age)+1
print(f"Hello [{name}] next year you'll be [{nextAge}]")

## exercise 2
temperatureCelcius = input('What is the current temperature? ')
temperatureFahr = int(temperatureCelcius)*(9/5) + 32
print(f'The temperature is {temperatureFahr} Fahrenheits')

