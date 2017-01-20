"""
Exercise 8.4 Download a copy of the file from www.py4inf.com/code/romeo.
txt
Write a program to open the file romeo.txt and read it line by line. For each line,
split the line into a list of words using the split function.
For each word, check to see if the word is already in a list. If the word is not in the
list, add it to the list.
When the program completes, sort and print the resulting words in alphabetical order.
"""

def function8_2():
    Slist = list()
    fname = raw_input('Enter File: ')
    fopen = open(fname)
    for line in fopen:
        words = line.split()
        for word in words:
            if word not in Slist:
                Slist.append(word)
    print sorted(Slist)

function8_2()
