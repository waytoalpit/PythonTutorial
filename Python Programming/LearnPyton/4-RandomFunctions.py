# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 17:47:08 2016

@author: waytoalpit
"""

#!/usr/bin/python3
import random

#returns a random item from a list, tuple, or string
print ("returns a random number from range(100) : ",random.choice(range(100)))
print ("returns random element from list [1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9]))
print ("returns random character from string 'Hello World' : ", random.choice('Hello World'))


#randomly selected element from range(start, stop, step)

# randomly select an odd number between 1-100 
print ("randrange(10,100, 1) : ", random.randrange(1, 100, 2))

# randomly select a number between 0-99 
print ("randrange(100) : ", random.randrange(100))


#returns a random float r, such that 0.0 <= r <= 1.0
print ("random() : ", random.random())


#returns reshuffled list.
list = [20, 16, 10, 5];
random.shuffle(list)
print ("Reshuffled list : ",  list)


#returns a floating point number r such that x <=r < y
print ("Random Float uniform(5, 10) : ",  random.uniform(5, 10))

