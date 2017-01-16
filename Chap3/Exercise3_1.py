"""
Exercise 3.1 Rewrite your pay computation to give the employee 1.5 times the
hourly rate for hours worked above 40 hours.
"""

hours = float(raw_input('Enter Hours: '))
rate = float(raw_input('Enter Rate: '))
if hours >= 40:
    pay = (hours - 40) * rate * 1.5 + 40 * rate
    print 'Pay: %.1f' %pay

else:
    pay = hours * rate
    print 'Pay: %.1f' %pay