"""
Exercise 6.3 Encapsulate this code in a function named count, 
and generalize it so that it accepts the string and the letter as arguments.
"""

string = raw_input('Please Enter a String: ')

def counts(string, target):   #take string and letter both as argument in a function.
    count = 0
    for letter in string:
        if letter == target:
            count += 1
    return count

print counts(string, 'a')