#!usr/bin/python
# -*- coding: utf-8 -*
"""
Exercise 4.1 Run the program on your system and see what numbers you get. Run the program more than once and see what numbers you get.
The random function is only one of many functions that handle random numbers. The function randint takes the parameters low and high, and returns an integer between low and high (including both).
>>> random.randint(5, 10) 
5
>>> random.randint(5, 10) 
9
"""

import random

"""
for i in range(10):
    x = random.random()
    print x
"""

print random.randint(5, 10)

t = [1, 2, 3]
print random.choice(t)