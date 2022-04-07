#estas lineas de codigos nos permiten ingresar a un archivo, puntalizar una linea que contiene informacion interesante y extraer esa informacion

file_01=open('mbox-short.txt')
for line in file_01:
    line=line.rstrip() #recordar que esta linea elimina los new line (\n) de cada linea
    if not line.startswith('From '):continue
    words=line.split()
    print(words[2])
