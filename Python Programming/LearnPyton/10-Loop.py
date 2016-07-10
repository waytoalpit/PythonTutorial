# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 23:09:38 2016

@author: waytoalpit
"""

#!/usr/bin/python3
import sys

list=[1,2,3,4]
it = iter(list) # this builds an iterator object

# for impl
for x in list:
   print (x, end=" ")

print('\n')
# while impl
while True:
   try:
      print (next(it))
   except StopIteration:
      sys.exit() #you have to import sys module for this
      
      
      
# use of break, continue and pass


