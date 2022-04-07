#############################################################################
############################################################################

han=open('mbox-short.txt')

for line in han:
    line=line.rstrip()
    wds=line.split()
#Guardian. Las dos linea que vienen abajo se llama guardian pattern porque nos protegen de que el programa no se caiga si hay algo raro en el archivo
#------------------------------
    if len(wds)<3:
        continue
#--------------------------------
#otra forma de introducir un 'Guardian' seria...
        #if line='':
        #    continue
    if wds[0]!='From':
        continue
    print(wds[2])
