#############################################################################
#En este archivo utilizamos el Guardia pero de una manera ligeramente defirente
#El resultado es el mismo que en el caso anterior.
############################################################################

han=open('mbox-short.txt')

for line in han:
    line=line.rstrip()
    wds=line.split()
#############################################
#Guardian!!
    if len(wds)<3 or wds[0]!='From': #el orden de esta linea es muy imporante
        continue
##############################################
    print(wds[2])
