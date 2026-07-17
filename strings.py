#formatted strings
first = 'John'
last = 'Smith'
msg = f'{first} [{last}] likes to cook'                                                                                                                             
print(msg)
print(len(msg))

#strings methods
Course = 'Learning Python'
#to use string methods we make use of the .(dot) operator
#the len() method is used todisplay the number of items in a list.
print(len(Course))

"""to change the case of a string to either lowercase or uppercase and vice versa
we use the .upper() and .lower() functions"""
print(Course.upper())
print(Course.lower())

"""the .find() function is used to return the index/position of the first 
occurrence of the defined character.The method is case sensitive"""
print(Course.find('P'))

#replace() method 
"""The replace() method is used to replace a certain word or character with another"""
print(Course.replace('Python' , 'Java'))
print(Course.replace('P','J'))
