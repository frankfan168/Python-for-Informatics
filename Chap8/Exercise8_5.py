

def function():
    count = 0
    fname = raw_input('Enter a file name: ')
    fopen = open(fname)
    for line in fopen:
        line = line.rstrip()
        if not line.startswith('From '):
            continue
        words = line.split()
        if len(words) == 0 or len(words) < 2:
            continue
        print words[1]
        count += 1
    print 'There were %d lines in the file with From as the first word' %count

function()
        