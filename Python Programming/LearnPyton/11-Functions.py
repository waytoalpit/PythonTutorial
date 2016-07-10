# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 22:02:53 2016

@author: waytoalpit
"""

#!/usr/bin/python3

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return

# Now you can call printme function- Required arguments
printme('Required arguments')


# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function- Keyword arguments
printinfo( age=50, name="miki" )


# Function definition is here
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function- Defult arguments
printinfo( name="miki" )


def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return

# Now you can call printinfo function- Variable-length arguments
printinfo( 10 )
printinfo( 70, 60, 50 )


# multiple return feature
# Function definition is here
def swap( arg1, arg2 ):
   # swap and return
   temp= arg1
   arg1= arg2
   arg2= temp
   return arg1, arg2

# Now you can call swap function
a, b = swap( 10, 20 )
print ("swapped values : ", a, b )