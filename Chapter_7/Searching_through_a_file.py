#fhand=open('mbox-short.txt')
#for line in fhand:
#    line=line.rstrip() #esta linea elimina el \n de cada linea del archivo
#    if line.startswith('From:'):
#        print(line)
#el print statemente agruega siempre una new line al final por lo tanto  el resultado de correr este programa
#va a ser una serie de lines separadas por lineas


#la forma anterior no es la mejor manera de escribir esta funcion.
#la mejor manera de hacerlo es utilizando la funcion "continue"


fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()  #esta linea elimina el \n de cada linea del archivo
    if not line.startswith('From:'):
        continue
    print(line)
