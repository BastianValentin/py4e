largest_so_far = -1
print('Before:', largest_so_far)
count = 0
for the_num in [3, 6, 70, 100, 150, 275, 1740, 1000, 50, 101]:
    count = count + 1
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After:', largest_so_far)
print('Number of data:', count)
