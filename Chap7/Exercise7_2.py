
fname = raw_input('Enter the file name: ')

try:
    fopen = open(fname)
except:
    print 'Please enter a valid file name'
    exit()

sum = 0
count = 0
for line in fopen:
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    a = line.find(':')
    b = float(line[a+1:])
    sum += b
    count += 1

print 'Average spam confidence: ', sum/count


        