filename = input('Enter filename: ')
if len(filename) < 1 : filename = 'words.txt'
fhand = open(filename)
#print(fhand)

di = dict()
for lin in fhand:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    # print(wds)
    for w in wds:
        di[w] = 1
        #print(w)

print(di)
q = 'the' in di
print(q)
