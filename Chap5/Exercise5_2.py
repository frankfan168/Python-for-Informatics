#!usr/bin/python
# -*- coding: utf-8 -*

"""
Exercise 5.2 Write another program that prompts for a list of numbers 
as above and at the end prints out both the maximum and minimum of the numbers instead of the average.
"""

count = 0
sum = 0
list = []

while True:
    number = raw_input('Enter a number: ')
    if number == 'done':
        break
    else:
    
        try:
            number = float(number)
            count = count + 1
            sum = sum + number
            list.append(number)
        except:
            print 'Invalid input'

print int(sum), count, max(list), min(list)