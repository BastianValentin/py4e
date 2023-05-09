fname = input('Enter filename: ')
if len(fname) < 1 : fname = 'r_and_j_short.txt'
try:
    fhand = open(fname)
except Exception as e:
    print('File cannot be opened', fname)
    exit()

count = dict()
for line in fhand:
    words = line.split()
    #print('words: ', words)
    for word in words:
            if word not in count:
                count[word] = 1
            else:
                count[word] = count[word] + 1


print(count)

lst = list(count.keys())
print(lst)
lst.sort()
for xkey in count:
    print(xkey, count[xkey])
