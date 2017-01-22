#!usr/bin/python
# -*- coding: utf-8 -*
"""
Exercise 9.2 Write a program that categorizes each mail message by which day 
of the week the commit was done. To do this look for lines that start with “From”, 
then look for the third word and keep a running count of each of the days of the week. 
At the end of the program print out the contents of your dictionary (order does not matter).
"""

sdict = dict()
fname = raw_input('Enter a file name:')
try:
    fopen = open(fname)
except:
    print 'Please enter a valid file name'
for line in fopen:
    line = line.strip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    word = words[2]
    sdict[word] = sdict.get(word, 0) + 1
print sdict