eh = input('Enter hours')

try:
    h = float(eh)
except Exception as e:
    print('Please enter a numeric number. Remember the working hours must be above 0.')

er = input('enter rate')
try:
    r = float(er)
except Exception as e:
    print('Please enter a numeric number')
if h > 37:
    regpay = h * r
    otp = (h - 37) * (r * 0.5)
    payment = regpay + otp
else:
    payment = h * r
    pass

print('Pay:',payment)
