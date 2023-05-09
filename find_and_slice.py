str = 'X-DSPAM-Confidence: 0.8475'
acolon = str.find(':')
print(acolon)
piece = str[acolon+1:]
print(piece)
value = float(piece)
print(value)
