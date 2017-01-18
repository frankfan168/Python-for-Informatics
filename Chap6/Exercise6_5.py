#!usr/bin/python
# -*- coding: utf-8 -*

"""
Exercise 6.5 Take the following Python code that stores a string:‘
str = 'X-DSPAM-Confidence: 0.8475'
Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.
"""


str = 'X-DSPAM-Confidence: 0.8475'
x = str.find(':')
y = str[x+2:]
print float(y)


