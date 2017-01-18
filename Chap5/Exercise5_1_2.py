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


def counting():
    count = 0
    total = 0
    list = []

    while True:  
        number = raw_input('Enter a number: ')
        if number == 'done':
            print int(total), count, max(list), min(list)
            break
        try:
            number = float(number)
            count += 1
            total += number    
            list.append(number)

        except:
            print 'Invalid input'

counting()