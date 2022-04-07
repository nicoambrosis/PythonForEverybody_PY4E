###############################################################################
#######################  Dictionaries ##########################################
###############################################################################
#son una de las herramientas mas usadas por la gente que programa en python
#con las herramientas que habiamos aprendido hasta ahora podrimos contar cuantas
#veces un elemnto estaba dentro de una lista, pero no podiamos contar cuantas veces
#estaba cada uno de los elementos. Utilizando diccionarios si podemos hacer eso!

print('\n')
print('################################# Dictionaries #################################')
print('\n')

counts=dict()
nombres=['juan', 'pedro','juan','maga','julia','julia']
for nombre in nombres:
    counts[nombre]=counts.get(nombre,0)+1 #esto significa "si la key no esta en el diccionario se le asigna un valor de 0, pero si esta se le suma"
    #"1 al valor que tenia antes"
print(counts)

#esta funcion se usa normalmente para realizar histogramas
