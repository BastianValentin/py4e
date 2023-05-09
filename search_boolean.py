found = False
print('Before:', found)
for value in [1, 50, 6, 500, 11, 9]:
    if value == 9:
        found = True
    print(value, found)

print('After:', found)
