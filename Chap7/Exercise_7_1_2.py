fname = raw_input('Enter a file name: ')
try:
    fopen = open(fname)
    for line in fopen:
        line = line.rstrip().upper()
        print line
        
except:
    'Please enter a valid file name'