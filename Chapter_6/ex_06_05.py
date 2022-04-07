str='X-DSPAM-Confidence: 0.8475'
xx=str.find(' ')
print(xx)
number=str[xx+1:]
value=float(number)
print(value)
