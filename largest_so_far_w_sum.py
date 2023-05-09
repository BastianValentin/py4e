largest_so_far = -1
print('Before:', largest_so_far)
sum = 0
for the_num in [3, 6, 70, 100, 150, 275, 1740, 1000, 50, 101]:
    sum = sum + the_num
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After:', largest_so_far)
print('Numeric summarized value:', sum)
