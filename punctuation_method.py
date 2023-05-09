import string

fname = input('Enter filename: ')
if len(fname) < 1 : fname = 'r_and_j_short_punctuation.txt'
try:
    fhand = open(fname)
except Exception as e:
    print('File cannot be opened', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)

lst = list(counts.keys())
for xkey in counts:
    print('key: ', xkey, 'Value: ', counts[xkey])
