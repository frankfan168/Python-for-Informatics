sdict = dict()
fname = raw_input('Enter a file name:')
try:
    fopen = open(fname)
except:
    print 'Please enter a valid file name'

for line in fopen:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    words = line.split()
    if len(words) == 0 or len(words) < 3: 
        continue
    s = words[2]
    sdict[s] = sdict.get(s, 0) + 1
print sdict
        