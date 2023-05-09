
def computepay(hours, rate):
    # print("In computepay", hours, rate)
    if h > 37:
        regpay = hours * rate
        otp = (hours - 37) * (rate * 0.5)
        pay = regpay + otp
    else:
        pay = hours * rate
    # print("returning", pay)
    return pay
    pass

eh = input('Enter hours')
try:
    h <= 0
    pass
except Exception as e:
    print("Hours should be above 0")
try:
    h = float(eh)
except Exception as e:
    print('Please enter a numeric number. Remember the working hours must be above 0.')

er = input('enter rate')
try:
    r = float(er)
except Exception as e:
    print('Please enter a numeric number')

payment = computepay(h, r)


print('Pay:',payment)
