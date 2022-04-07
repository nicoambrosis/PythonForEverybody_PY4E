num=0
tot=0.0
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

print('ALL DONE')
print(num,tot,tot/num)










# total count average
