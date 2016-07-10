# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 19:21:55 2016

@author: waytoalpit
"""

#!/usr/bin/python3

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])


dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School" # Add new entry


print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])


del dict['Name'] # remove entry with key 'Name'
#dict.clear()     # remove all entries in dict
#del dict         # delete entire dictionary

#print ("dict['Age']: ", dict['Age'])
#print ("dict['School']: ", dict['School'])

# type of variables
print (type(dict))

# create a local copy, default- pass by reference
dict2 = dict.copy()
print ("New Dictionary : ",dict2)


seq = ('name', 'age', 'sex')
# list creates a new dictionary with keys from seq and values set to None

dict = dict.fromkeys(seq)
print ("New Dictionary : ", dict)

#creates a new dictionary with keys from seq and values set to 10
dict = dict.fromkeys(seq, 10)
print ("New Dictionary : ", dict)

#get value from key
print ("Value : ", dict.get('age'))

#check if dict contains a aprticular key
print ("Value : ", 'age' in dict)

#prints every key/value pair in the form of tuple
print ("Value : ", dict.items())


#list of available keys
print ("Keys : ", dict.keys())

#list of available values
print ("Values : ", dict.values())






