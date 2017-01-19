count = 0
total = 0

fname = raw_input('Enter a file name: ')
try:
    fopen = open(fname)
    for line in fopen:
        line = line.rstrip()
        if not line.startswith('X-DSPAM-Confidence:'):
            continue
        start = line.find(':')
        list = float(line[start+2 : ])
        count += 1
        total += list
    print 'Average spam confidence:', total/count
             
        
except:
    print 'Please enter a valid file name'