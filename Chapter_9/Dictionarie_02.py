###############################################################################
#######################  Dictionaries ##########################################
###############################################################################
#son una de las herramientas mas usadas por la gente que programa en python
print('\n')
print('################################# Dictionaries #################################')
print('\n')

counts={}
nombres=['juan', 'pedro','juan','maga','julia','julia']
for nombre in nombres:
    if nombre not in counts:
        counts[nombre]=1
    else: #esto significa "si el nombre ya esta en la lista, hace lo siguiente..."
        counts[nombre]=counts[nombre]+1 #esto significa "al valor que tiene asignado ese nombre, agregale 1"
print(counts)

#esta es una manera complicada de contar cuantas veces aparece un elemento en una lista.
#una forma mucho mejor es utilizando la funcion .get(). ver Dictionaries_03.py
