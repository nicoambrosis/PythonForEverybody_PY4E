###############################################################################
#######################  Dictionaries ##########################################
###############################################################################
#son una de las herramientas mas usadas por la gente que programa en python
print('\n')
print('################### DICTONARIES ##############################')
print('\n')

#########
# opcion 1 #
counts=dict()
line=input('Enter a line of text:')

################
# opcion 2 # a mi me gusta mas la opcion de arriba, pero esta bueno saber que ambas tienen el mismo resultado
#print("Enter a line of text:")
#line=input('')


print(line)

words=line.split() #esta linea te permite crear una lista (que en este caso llama
#words que contiene como valores cada palabra de la oracion ingresada)
print(words)

for i in words:  #recordar que words es una lista, no un diccionario
    counts[i]=counts.get(i,0)+1 #con esta linea estamos incorporando los valores de la lista
    #words a un diccionario que se llama counts. Los valores de la lista se van a incorporar
    #como key, el numero de veces que esas key estan en la oracion va a ser el valor del par key-value

print("Counting...")
print("counts>>>", counts)

for key in counts:
    if counts[key]>1:   #incorporando esta linea dejamos de lado a aquellas palabras que solo aparecen una vez(es muy buena!!)
        print(key,counts[key])
