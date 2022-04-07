print('lets see')
rawstr = input('enter a number: ')
try :
    ival = int(rawstr)
except:
    ival = -1
if ival > 0 :
    print('nice work')
else :
    print('sorry, not a number')
print('good catch nick!')
