###############################################################################
#######################  Dictionaries ##########################################
###############################################################################
#son una de las herramientas mas usadas por la gente que programa en python
print('\n')
print('################################# Dictionaries #################################')
print('\n')


counts={}
nombres=['juan', 'pedro','juan','maga','julia','julia','julian','fermin']
for nombre in nombres:
    counts[nombre]=counts.get(nombre,0)+1
print(counts)

for key in counts:
    print(key)
