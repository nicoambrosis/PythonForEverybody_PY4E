#al principio colocamos los valores iniciales de las variables
num=0
tot=0.0
min=None
max=None
while True:
    x=input('Enter a number:')
    if x=='done':
        break
    try:
        x=float(x)
    except:
        print('Invalid Value')
        continue
    #print(x)
    num=num+1
    tot=tot+ x

#estas lineas son para encontrar el numero mas bajo de la lista
    if min is None:
        min=x
    elif x<min:
        min=x

#estas lineas son para encontrar el numero mas alto de la lista
    if max is None:
        max=x
    elif x>max:
        max=x


print('ALL DONE')
print(num,tot,'max is:',max)
print(num,tot,'min is:',min)










# total count average
