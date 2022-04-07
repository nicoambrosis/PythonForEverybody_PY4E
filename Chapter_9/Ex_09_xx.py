###############################################################################
#######################  Dictionaries ##########################################
###############################################################################
#son una de las herramientas mas usadas por la gente que programa en python
print('################### DICTONARIES ##############################')
print('\n')

file_name=input('Enter file name:')
if len(file_name)<1:file_name='words02.txt'
file=open(file_name)

counts={}
for text in file:         #usar "text" en lugar de "line" me parece una forma mucho mas elegante de armar el codigo.
    text=text.rstrip()   #esta linea elimina los '\n', creo que es opcional
    #print(text)          #si la line de arriba no esta activada, cuando imprima el texto, lo ultimo que va a imprimir es un '\n'
                        # lo cual genera una linea vacia debajo del texto que se imprimio.
    words=text.split()   #con este codigo, para cada linea arma una lista diferente
    #print(words)
    for word in words:
        counts[word]=counts.get(word,0)+1

for key,value in counts.items():
    if value>1: print(key,value)

############################################################
#ahora vamos a buscar la palabra que aparece mas veces
mas_repetido=-1
palabra=None
for word,count in counts.items():
#    print(word,count)
    if count > mas_repetido:
        mas_repetido=count
        palabra=word
print('palabra mas usada>>>', palabra,'>>>',mas_repetido, "veces")
############################################################
