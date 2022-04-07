###############################################################################
#######################  Dictionaries ##########################################
###############################################################################
#son una de las herramientas mas usadas por la gente que programa en python
print('\n')
print('################### DICTONARIES ##############################')
print('\n')

#dado un diccionario x es posible armar una lista con los keys, los valores, o ambas cosas
#para armar una lista de los key tenemos dos opciones:
            #usamos la funcion list()
            #o usamos la funcion xxx.keys()
#para armar una lista de values usamos la funcion xxx.values()
#y si queremos keys y values usamos la funcion xxx.items()

counts={}
nombres=['juan', 'pedro','juan','maga','julia','julia','julian','fermin']
for nombre in nombres:
    counts[nombre]=counts.get(nombre,0)+1

print('Diccionario:', counts)
print(list(counts))
print(counts.keys())
print(counts.values())
new_list=counts.items()
print(new_list)
