###############################################################################
#######################  Dictionaries ##########################################
###############################################################################
#son una de las herramientas mas usadas por la gente que programa en python
print('\n')
print('################### DICTONARIES ##############################')
print('\n')


file=open('words.txt') #recordar que para que esta linea de codigo funcione, el archivo al que llamamos
#tiene que estar en la misma carpeta en la que esta este programa


counts={}
for line in file: #me parece super elegante llamar file al archivo abierto y no 'handle'
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
#for word,count in counts.items():
#    if count>1:
#        print(word,count)

#hasta aca el programa nos permitio armar un histograma con el numero de veces que aprece una palabra en un arhivo de texto


#ahora vamos a buscar la palabra que aparece mas veces
mas_repetido=0
palabra=0
for word,count in counts.items():
    if mas_repetido is 0 or count>mas_repetido:
        mas_repetido=count
        palabra=word
print(palabra,mas_repetido)
############################################################
