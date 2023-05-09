filename = input('Enter filename: ')
if len(filename) < 1 : filename = 'clown.txt'
fhand = open(filename)
#print(fhand)

di = dict()
for lin in fhand:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    # print(wds)
    for w in wds:
        #idiom: retrieve/create/ update counter
        di[w] = di.get(w,0) + 1

        #print(w)

print('Dictionary:',di)

#x = di.items()
#x_sorted = sorted(di.items())
#print("x: ", x, "x sorted:", x_sorted)

tmp = list()
for k, v in di.items():
    print(k, v)
    newtup = (v,k)
    tmp.append(newtup)

print('Flipped tmp:', tmp)

tmp = sorted(tmp, reverse=True)

print('Sorted temp:', tmp[:5])

for v, k in tmp[:5]:
    print(k,v)

#Counter:
#bigcount = None
#bigword = None
#for w,count in di.items():
#    if bigcount is None or count > bigcount:
#        bigword = w
#        bigcount = count
#
#print(bigword, bigcount)
