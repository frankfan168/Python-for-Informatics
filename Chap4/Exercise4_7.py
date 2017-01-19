#!usr/bin/python
# -*- coding: utf-8 -*
"""
Exercise 4.7 Rewrite the grade program from the previous chapter using a 
func- tion called computegrade that takes a score as its parameter and returns 
a grade as a string.
Score Grade >0.9 A >0.8 B >0.7 C >0.6 D <=0.6 F
Program Execution: 
Enter score: 0.95 A
Enter score: perfect Bad score
Enter score: 10.0 Bad score
Enter score: 0.75 C
Enter score: 0.5 F
Run the program repeatedly to test the various different values for input.
"""
def computegrade(score):
    if score >= 0 and score <= 1.0:
        if score > 0.9:
            grade = 'A'
        elif score > 0.8:
            grade = 'B'
        elif score > 0.7:
            grade = 'C'
        elif score > 0.6:
            grade = 'D'
        else:
            grade = 'F'
        print grade
    else:
        print 'Bad score'

while True:
    score = raw_input('Enter score: ')

    try:
        score = float(score)

    except:
        print 'Bad score'
        break
    
    computegrade(score) 
    


