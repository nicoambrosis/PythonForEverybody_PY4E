###############################################################################
#######################  Dictionaries ##########################################
###############################################################################
#este programa fue escrito para ordenar que cantidad de mail llego cada dia a partir del archivo mbox-short.txt####

file=open('mbox-short.txt')

counts={}

for line in file:
    #line=line.rstrip() #todavia no tengo muy claro en que momento hay que usar esta funcion y en que momento no
    if line.startswith('From '): #este codigo identifica a aquellas lineas que empiezan con 'From'
        line=line.split()       #este codigo arma una lista con los str de la linea
        mail=line[1]             #esta linea de codigo es fundamental para definir cuales van a ser los elementos de
        #print(day)                        #de las listas que queremos meter en el diccionario de dias
        counts[mail]=counts.get(mail,0)+1
print(counts)

for mail,value in counts.items():
    print('You have recived',value,'mails from >>>>>>',mail,'\n')

############################################################
#ahora vamos a buscar la palabra que aparece mas veces
mas_repetido=-1
remitente=None
for mail,value in counts.items():
#    print(word,count)
    if value > mas_repetido:
        mas_repetido=value
        remitente=mail
print('remitente mas frecuente >>>', remitente,'>>>',mas_repetido, "veces")
