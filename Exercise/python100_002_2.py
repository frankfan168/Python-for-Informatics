#!usr/bin/python
# -*- coding: utf-8 -*

i = int(raw_input('Please enter revenue:'))
r = 0
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
for x in range(0, 6):
    if i > arr[x]:
        r += (i - arr[x]) * rat[x]
        i = arr[x]
print r
