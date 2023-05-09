fhan = open('mbox-short.txt')

d = dict()
for line in fhan:
    line = line.rstrip()
    print('Line:', line)
