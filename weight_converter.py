"""Ask the user to input their weight in either kilograms or pounds and then \
will convert it to the other unit
1 pound = 0.45kg
"""
weight = input('What is your weight : ')
weight_measurement_type = input('is your weight in kg or pounds : ')
if weight_measurement_type == 'kg':
    weight_in_pounds = int(weight)/0.45
    print('Your weight in pounds is : ',weight_in_pounds)
elif weight_measurement_type == 'pounds':
    weight_in_kg = int(weight)*0.45
    print('Your weight in kg is : ',weight_in_kg)
else:
    print('value inputed is invalid')