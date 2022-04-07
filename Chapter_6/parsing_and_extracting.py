data='nambrosis@biol.unlp.edu.ar mail from NMA'
atpos=data.find('@')
print(atpos)
spos=data.find(' ',atpos) #el primer miembro del parentesis indica el elemento a buscar, el segundo elemento indica elluga donde se INICIA la busqueda
print(spos)
mail=data[atpos+1:spos] #recordar que la ultima posicion no esta incluida 
print(mail)
