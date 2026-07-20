## If statements 
is_hot = False
is_cold = True
if is_hot:
    print("It is a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It is a cold day")
    print("wear warm clothes")
else:
    print("It is a lovely day")
print("Enjoy your day")

#example
buyingPrice = 1000000
is_credit_good = False
is_credit_bad = True

if is_credit_good:
    print("You have good credit")
    down_payment = 0.1*buyingPrice
    print("The down payment is $",down_payment)
elif is_credit_bad:
    print("You have bad credit")
    down_payment = 0.2*buyingPrice
    print("The down payment is $",down_payment)
else:
    print("no credit record")

##logical operators - used in situations where we have multiple conditions
"""Logical operators in python include:
i)and - used when both of the conditions are true
ii)or - used when either one of the conditions or both of the conditions are true
iii)not -inverts any boolean value given.Converts True to False and vice versa
"""
#and operator
"""if an applicant has high income and good credit then they are
eligible for a loan
"""
has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for loan")
#or operator
"""
If an applicant has  a good income or has good values then they
are eligible for loan"""
has_good_income = True
has_good_values = False
if has_good_income or has_good_values:
    print("Eligible for loan")
#not 
"""If an applicant has a good car and does not have a criminal
record then they are eligible for a loan
"""
has_good_car = True
has_criminal_record = False

if has_good_car and not has_criminal_record:
    print("Eligible for loan")


