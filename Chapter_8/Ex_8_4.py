list=[0,1,2,3]
print(list)

def chop():
    for i in list:
        list.pop(0)
        list.pop(-1)
        return list[i]
#hay algun problema con la resolucion de esta funcion. No se como hacer para que me devuelva una lista. Me trabe aca y no se como seguir... 
chop()



#pop() Vs remove(): cuando usamos la funcion pop(x) el argumento de la funcion es la posicion de la lista que queremos eliminar. Esta funcion admite
#utiliza el argumento '-1' para refereirnos a la lista contanto de atras hacia adelante. '-1' es el ultimo elemento de la lista.
#cuando usamos la funcion remove(x) el argumento es el nombre del elemento que queremos eliminar
