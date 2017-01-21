#!usr/bin/python
# -*- coding: utf-8 -*
"""
题目：输入某年某月某日，判断这一天是这一年的第几天？
"""

year = int(raw_input('Please enter year:\n'))
month = int(raw_input('Please enter month\n'))
day = int(raw_input('Please enter day\n'))

m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum = 0
total = 0
for x in range(1, 12):
    if month == 1:
        sum = 0
        break
    if month > m[x-1]:
        sum += d[x]
        #print sum

if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) and month > 2:
    total = sum + day + 1
else:
    total = sum + day
print 'This is the %d day of the year.' %total




