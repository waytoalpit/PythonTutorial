# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 23:39:19 2016

@author: waytoalpit
"""

#!/usr/bin/python3

#impl of try, except, else and finally
try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
finally:
   print ("Error: can\'t find file or read data in finally block")


#pass arguments to an exception
# Define a function here.
def temp_convert(var):
   try:
      return int(var)
   except ValueError as Argument:
      print ("The argument does not contain numbers\n", Argument)

# Call above function here.
temp_convert("xyz")



#raise an exception
def functionName( level ):
    if level <1:
        raise Exception(level)
        # The code below to this would not be executed
        # if we raise the exception
    return level

try:
    l=functionName(-10)
    print ("level=",l)
except Exception as e:
    print ("error in level argument",e.args[0])
    
    

#User defined exceptions
class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg


try:
   raise Networkerror("Bad hostname")
except Networkerror as e:
   print (e.args)