counts = dict()
names = ['Brian', 'Ole', 'Alex', 'Conny', 'Ole']

for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
