

Slist = list()
while True:
    number = raw_input('Enter a number: ')
    if number == 'done':
        break
    number = float(number)
    Slist.append(number)

print 'Maximum:', max(Slist)
print 'Minimum:', min(Slist)
    