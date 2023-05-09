ci = input('Degree Celsius to Fahrenheit. Celsius to convert:')
not_a_number = 'Att!: C is not a numeric number. Please enter a number.'

try:
    c = float(ci)
except:
    c = not_a_number

if c == not_a_number:
    print(not_a_number)
else:
    f = c * 1.8 + 32
    print('Fahrenheit:',f)
    pass


#if c >= 0 or c <= 0:
#    f = c * 1.8 + 32
#    print('Fahrenheit:',f)
#    pass

#else:
#    print(not_a_number)
