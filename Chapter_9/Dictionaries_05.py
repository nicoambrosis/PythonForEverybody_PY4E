###############################################################################
#######################  Dictionaries ##########################################
###############################################################################
#son una de las herramientas mas usadas por la gente que programa en python
print('\n')
print('################################# Dictionaries #################################')
print('\n')


prueba=dict() #hay otra forma de crear un dccionario: prueba={}. Ambas formas son equivalentes, crean un dccionario vacio.
prueba['campeonatos']='9'
prueba['descensos']=2 #notar es mas sencillo agregar un elemnto a un diccionario que hacerlo a una lista (appen.xxx)
print(prueba)
print(prueba['campeonatos'])
prueba['campeonatos']=prueba['campeonatos']+'1' #esta es una linea de codigo que nos va a servir para contar
#cuantas veces se repite un valor (un numero o una palabra) en un texto (o un archivo!!)
print(prueba)
print(prueba['campeonatos'])
