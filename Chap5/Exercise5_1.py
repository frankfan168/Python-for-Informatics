#!usr/bin/python
# -*- coding: utf-8 -*

"""
Exercise 5.1 Write a program which repeatedly reads numbers until the user en- ters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
Enter a number: 4
Enter a number: 5
Enter a number: bad data Invalid input
Enter a number: 7
Enter a number: done
16 3 5.33333333333
"""

count = 0
sum = 0

while True:
    number = raw_input('Enter a number: ')
    if number == 'done':
        break
    else:
    
        try:
            number = float(number)
            count = count + 1
            sum = sum + number
        except:
            print 'Invalid input'

print int(sum), count, sum/count




    