# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 18:57:55 2016

@author: waytoalpit
"""

#!/usr/bin/python3

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]

print ("list1[0]: ", list1[0:2])
print ("list2[1:5]: ", list2[1:5])

list2[2]="updated value"
print ("list2[1:5]: ", list2[1:5])

del list2[2]
print ("list2[1:5]: ", list2[1:5])

print (len(list1))


list1, list2 = ['C++','Java', 'Python'], [456, 700, 200]
print ("Max value element : ", max(list1))
print ("Max value element : ", max(list2))

print ("min value element : ", min(list1))
print ("min value element : ", min(list2))


list1.append('C#')
print ("updated list : ", list1)

aList = [123, 'xyz', 'zara', 'abc', 123];
print ("Count for 123 : ", aList.count(123))


list1.reverse()
print ("list1 now : ", list1)
list2.reverse()
print ("list2 now : ", list2)

list1.sort()
print ("list1 now : ", list1)