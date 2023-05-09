smallest_so_far = None
print('Before: ', smallest_so_far)
for value in [3, 6, 70, 100, 150, 275, 1740, 1000, 50, 101]:
    if smallest_so_far is None:
        smallest_so_far = value
    elif value < smallest_so_far :
        smallest_so_far = value
        print(smallest_so_far, value)
print('After: ', smallest_so_far)
