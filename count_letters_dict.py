word = 'brontosaurus'
d = dict()
for c in word:
    if not c in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1

print(d)
