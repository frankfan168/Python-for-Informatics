# -*- coding: utf-8 -*
"""
Exercise 9.3 Write a program to read through a mail log, 
build a histogram using a dictionary to count how many messages 
have come from each email address, and print the dictionary.
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
    if len(words) < 2 or words[0] != 'From':
        continue
    word = words[1]
    sdict[word] = sdict.get(word, 0) + 1
print sdict