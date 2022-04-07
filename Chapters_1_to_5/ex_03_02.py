print('Welcome to our new platform')
score=input('Enter Score: ')
try :
    sc=float(score)
except:
    print('Please Insert a number')
    score=input('Enter Score: ')
    sc=float(score)
if sc<0.0:
    print('Error, try again')
else:
    if sc>1.0:
        print('Error, try again')
    elif sc>=0.9:
        print('A')
    elif sc>=0.8:
        print('B')
    elif sc>=0.7:
        print('E')
    elif sc>=0.6:
        print('D')
    elif sc<0.6:
        print('F')
#seguramente existan formas mas sencillas de escribir este programa, pero lo importante es que de una forma u otra logre escribir el programa que queria!!
