# PythonForEverybody_PY4E
Python exersices I've when I was starting with python. PY4E from [Chuck Severance](https://www.youtube.com/watch?v=UjeNA_JtXME&list=PLlRFEj9H3Oj7Bp8-DfGpfAfDBiblRfl5p)

---
[ex_02_03.py](https://github.com/nicoambrosis/PythonForEverybody_PY4E/blob/main/Chapters_1_to_5/ex_02_03.py)
```python

print('PY4E')
xh=input('enter hours: ')
xr=input('enter rate: ')
xp=float(xh)*float(xr)
print('pay:',xp)

```
---
[not a number error.py](https://github.com/nicoambrosis/PythonForEverybody_PY4E/blob/main/Chapters_1_to_5/not%20a%20number%20error.py)
```python
print('lets see')
rawstr = input('enter a number: ')
if rawstr > 0 :
    print('nice work')
else :
    print('sorry, not a number')
print('good catch nick!')

```
---
[Nice_Excercise.py](https://github.com/nicoambrosis/PythonForEverybody_PY4E/blob/main/Chapter_9/Nice_Excercise.py)
```python
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
```

---
[Ex_8_4.py](https://github.com/nicoambrosis/PythonForEverybody_PY4E/blob/main/Chapter_8/Ex_8_4.py)
```python
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

```

---
[Searching_through_a_file.py](https://github.com/nicoambrosis/PythonForEverybody_PY4E/blob/main/Chapter_7/Searching_through_a_file.py)
```python

#fhand=open('mbox-short.txt')
#for line in fhand:
#    line=line.rstrip() #esta linea elimina el \n de cada linea del archivo
#    if line.startswith('From:'):
#        print(line)
#el print statemente agruega siempre una new line al final por lo tanto  el resultado de correr este programa
#va a ser una serie de lines separadas por lineas


#la forma anterior no es la mejor manera de escribir esta funcion.
#la mejor manera de hacerlo es utilizando la funcion "continue"


fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()  #esta linea elimina el \n de cada linea del archivo
    if not line.startswith('From:'):
        continue
    print(line)
```
    

