#!usr/bin/python
# -*- coding: utf-8 -*
"""
Exercise7.3 Sometimeswhenprogrammersgetboredorwanttohaveabitoffun, they add a harmless Easter Egg to their program (en.wikipedia.org/wiki/ Easter_egg_(media)). Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name “na na boo boo”. The program should behave normally for all other files which exist and don’t exist. Here is a sample execution of the program:
python egg.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt
python egg.py
Enter the file name: missing.tyxt File cannot be opened: missing.tyxt
python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!
We are not encouraging you to put Easter Eggs in your programs—this is just an exercise.
"""

fname = raw_input('Enter the file name: ')

if fname == 'na na boo boo':
    print "A NA BOO BOO TO YOU - You have been punk'd!"
    exit()

try:
    fopen = open(fname)
except:
    print 'File cannot be opened: ', fname
    exit()

count = 0
for line in fopen:
    line = line.rstrip()
    if not line.startswith('Subject'):
       continue
    count += 1

print 'There were', count, 'subject lines in', fname
    