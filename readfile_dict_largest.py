import string

fname = input('Enter filename: ')
if len(fname) < 1 : fname = 'clown.txt'

try:
    fhand = open(fname)
except:
    print('Filename does not exist in current folder')
    exit()

d = dict()
for line in fhand:
    line = line.rstrip() # to clear the white space on the right hand side of the data.
    line = line.translate(line.maketrans('', '', string.punctuation)) #Removes punctuation tags.
    line = line.lower()
    words = line.split()
    #print('Words: ', words)

    for word in words:
        #print(word)
        d[word] = d.get(word, 0) + 1

#print('Dict:', d)

#We want o find the most common word in the text.
mcw = -1
theword = None
for k,v in d.items():
    #print(k,v)
    if v > mcw:
        mcw = v
        theword = k

print("Most common word: ", theword, mcw)
