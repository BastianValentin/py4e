fhan = open('mbox-short.txt')

for line in fhan:
    line = line.rstrip()
    #print('Line: ',line)
#Another way to make aguardian of blank lines
    #if line == '' :
        #print('Skip blank')
        #continue
    wds = line.split()
    #print('Word: ', wds)
    # Guardian pattern to protect the code from blewing up!
    if len(wds) < 3:
        continue
    if wds[0] != 'From':
        #print('Ignore')
        continue

    print(wds[2])
