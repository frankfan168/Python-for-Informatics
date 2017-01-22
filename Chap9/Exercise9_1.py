#!usr/bin/python
# -*- coding: utf-8 -*
"""
Exercise9.1 Writeaprogramthatreadsthewordsinwords.txtandstoresthem as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.
"""

store = dict()                 #void dict must be put before def
                               #if you put inside def, store will always be void
def function():               
    count = 0                  #count=0 must be put inside def, or it will always be 0
    fopen = open('words.txt')
    for line in fopen:
        line = line.rstrip()
        words = line.split()
        for word in words:
            store[word] = count
            count += 1
    return store

function()
print store
fname = raw_input('Enter a word:')
print fname in store

    