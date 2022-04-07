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
        day=line[2]             #esta linea de codigo es fundamental para definir cuales van a ser los elementos de
                                #de las listas que queremos meter en el diccionario de dias
        counts[day]=counts.get(day,0)+1
print(counts)

for key,value in counts.items():
    print(key,value)
