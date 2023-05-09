num = 0
tot = 0.0
while True :
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    fval = float(sval)
    print(fval)
    pass

print('ALL DONE')
print(tot,num,tot/num)
