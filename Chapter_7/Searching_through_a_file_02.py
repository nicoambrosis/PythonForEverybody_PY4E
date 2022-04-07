fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()  #esta linea elimina el \n de cada linea del archivo
    if not 'uct.ac.za'in line:
        continue
    print(line)
