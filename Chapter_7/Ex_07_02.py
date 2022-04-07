filename=input('Enter file name:')
if filename=='na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    try:
        file=open(filename)
        count=0
        list=[]
        for line in file:
            if line.startswith('X-DSPAM-Confidence:'):
                line=line.rstrip() #esta linea es fundamental porque sino el resultado de imprimir este codigo va  a tner espacios entre cada linea
                count=count+1
                x=float(line[19:])
                list.append(x)      #mediante esta linea incorporamos cada uno de los valores a una lista. Esto nos permite despues seguir trabajand con ese grupo de datos
                print(x)
        print('n=', count)
        print(list)
        sum=sum(list)
        mean=sum/count
        print('Average Spam Confidence:',mean)
    except:
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>> File name cannot be found <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        quit()


#muy lindo programa!!!
