# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 16:50:50 2016

@author: waytoalpit
"""

#!/usr/bin/python3

str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str[:-1])     # prints string except last character
print (str[-2:-1])   # prints second last character 
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string


str = "this is string example....wow!!!"

#returns a copy of the string with only its first character capitalized.
print ("str.capitalize() : ", str.capitalize())

#padding the string with the character fillchar (default is a space)
print ("str.center(40, 'X') : ", str.center(40, 'X'))

#occurrences of substring sub in the range [start, end]
sub='exam'
print ("str.count('exam', 10, 40) : ", str.count(sub,10,40))

suffix='!!'
print (str.endswith(suffix, 0, 31))

print (str.find(sub))
print (str.index(sub))


s = "-"
seq = ("a", "b", "c") # This is sequence of strings.
print (s.join( seq ))


str="PYTHONPROGRAMMING"
print ("Max character: " + max(str))
print ("Min character: " + min(str))


#returns last index if found and -1 otherwise.
str1 = "this is really a string example....wow is!!!"
str2 = "is"
print (str1.rfind(str2))


#split, replace and many more...