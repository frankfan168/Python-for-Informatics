#!usr/bin/python
# -*- coding: utf-8 -*
"""
Exercise8.1 Writeafunctioncalledchopthattakesalistandmodifiesit,remov- ing the first and last elements, and returns None.
Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
"""

"""
t = [1, 2 , 3]

def chop(t):
    del t[0]
    del t[-1]
    
print chop(t)
print t
"""

t = [1, 2, 3, 4]

def middle(t):
    return t[1 : -1]

print middle(t)