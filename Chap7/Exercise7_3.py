

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
    