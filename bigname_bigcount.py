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
        di[w] = di.get(w,0) + 1

        #print(w)

#print(di)

#Counter:
bigcount = None
bigword = None
for w,count in di.items():
    if bigcount is None or count > bigcount:
        bigword = w
        bigcount = count

print(bigword, bigcount)
