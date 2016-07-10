# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 00:55:18 2016

@author: waytoalpit
"""

#!/usr/bin/python3
import os

# Open a file
fo = open("foo.txt", "w")
fo.write( "Python is a great language.\nYeah its great!!\n")

# Close opend file
fo.close()


# Open a file
fo = open("foo.txt", "r+")
str = fo.read()
print ("Read String is : ", str)

# Close opened file
fo.close()


#rename/remove files 

# This would give location of the current directory
print (os.getcwd())

# create/delete/change directories