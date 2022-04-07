def computepay(h,r):
    if h<=40:
        return(h*r)
    elif h>40:
        return((h-40)*r*1.5+40*r)

hrs = input("Enter Hours:")
h=float(hrs)
rate= input('Enter Rate: ')
r=float(rate)
print("Pay",computepay(h,r))

#ESTE ES EL SEGUNDO PROGRAMA QUE ESCRIBO POR MI PROPIA CUENTA!!!!!

#hrs= input('Hours: ')
#h=float(hrs)
#print((h-40)*10.5*1.5+40*10.5)


#rate= input('Enter Rate: ')
#r=float(rate)
#print(r)
