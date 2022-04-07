# a=samlleste value
#estas lineas de codigo nos permite poner al primer valor de la lista como el mas chico hasta el momento en que se empieza a contar la lista
#sin necesidad de asumir un valor al azar que podria llevarnos a cometer algun error.
a=None  #esta es una manera de decir "'a' no vale ningun valor"
for i in [9,41,12,3,74,15]:
    if a is None:
        a=i
    elif i<a:
        a=i
    #print(a,i)
print(a)
