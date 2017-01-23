# -*- coding: utf-8 -*
"""
Exercise 9.4 Add code to the above program to figure out who has the most mes- sages in the file.
After all the data has been read and the dictionary has been created, look through the dictionary 
using a maximum loop (see Section 5.7.2) to find who has the most messages and print how many messages the person has.
"""
sdict = dict()
largest = None
fname = raw_input('Enter a file name:')
try:
    fopen = open(fname)
except:
    print 'Please enter a valid file name'
    exit()
for line in fopen:
    line = line.strip()
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    word = words[1]
    sdict[word] = sdict.get(word, 0) + 1
for key in sdict:
    if sdict[key] > largest:
        largest = sdict[key]
        bigword = key
        
print bigword, sdict[bigword]

