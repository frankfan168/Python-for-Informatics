#!usr/bin/python
# -*- coding: utf-8 -*
"""
Exercise 4.6 Rewrite your pay computation with time-and-a-half for overtime and 
create a function called computepay which takes two parameters (hours and rate).
Enter Hours: 45 Enter Rate: 10 Pay: 475.0
"""

import sys

try: 
    hours = float(raw_input('Enter Hours: '))
    rate = float(raw_input('Enter Rate: '))

    
except:
    print 'Please enter a number'
    sys.exit()
    


def total_pay(hours, rate):
    if hours > 40: 
        pay = (hours - 40) * rate * 1.5 + 40 * rate
    else:
        pay = hours * rate
    return pay


print 'Pay: ', total_pay(hours, rate)

