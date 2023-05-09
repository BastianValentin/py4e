counts = dict()
names = ['Brian', 'Ole', 'Alex', 'Conny', 'Ole']

for name in names:
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)
