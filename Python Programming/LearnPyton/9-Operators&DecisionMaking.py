# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 22:12:58 2016

@author: waytoalpit
"""
#!/usr/bin/python3

a = 3
b = 8
list = [1, 2, 3, 4, 5 ]

if ( a in list ):
   print ("Line 1 - a is available in the given list")
else:
   print ("Line 1 - a is not available in the given list")

if ( b not in list ):
   print ("Line 2 - b is not available in the given list")
else:
   print ("Line 2 - b is available in the given list")
   

b=3
if ( a is b ):
   print ("Line 2 - a and b have same identity")
else:
   print ("Line 2 - a and b do not have same identity")
   
b=8
if ( a is not b ):
   print ("Line 5 - a and b do not have same identity")
else:
   print ("Line 5 - a and b have same identity")
   
   
# many more....