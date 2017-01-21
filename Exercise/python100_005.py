#!usr/bin/python
# -*- coding: utf-8 -*
"""
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
"""

l = list()
for i in range(0, 3):
    try:
        m = int(raw_input('Please enter a number:'))
    except:
        print 'Please enter a valid number'
        exit()    
    l.append(m)
l.sort()
print l

