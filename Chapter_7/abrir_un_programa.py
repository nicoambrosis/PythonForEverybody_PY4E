fname=input('Enter file name:')
try:
    fhand=open(fname)
except:
    print('File cannot be opened:', fname)
    quit()  #esta linea cierra el programa sin mandar error.
            #Porque si el programa sigue corriendo si abrir ningun archivo probablemente se caiga mas adelante

print('Good!')
