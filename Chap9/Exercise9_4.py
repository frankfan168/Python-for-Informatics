sdict = dict()
fname = raw_input('Enter a file name:')
try:
    fopen = open(fname)
except:
    print 'Please enter a valid file name'

for line in fopen:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0 or len(words) < 3 or words[0] != 'From': 
        continue
    s = words[1]
    sdict[s] = sdict.get(s, 0) + 1

biggest = 0
for key in sdict:
    if sdict[key] > biggest:
        biggest = sdict[key]
        bigword = key
print bigword, sdict[bigword]
