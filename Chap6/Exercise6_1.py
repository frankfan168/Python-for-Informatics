#!usr/bin/python
# -*- coding: utf-8 -*
"""
Exercise 6.1 Write a while loop that starts at the last character in 
the string and works its way backwards to the first character in the 
string, printing each letter on a separate line, except backwards.
"""

fruit = 'banana'

def backward(fruit):
    index = len(fruit)-1   # adjust for 0th index, if not -1, it will be out of range
    while index >= 0:
        letter = fruit[index]
        print letter
        index = index -1
        
backward(fruit)