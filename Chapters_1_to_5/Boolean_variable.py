found='false'
print('Before:', found)
for value in [9,41,12,3,74,15]:
    if value==3:
        a='true'
    elif value!=3: #en lugar de la "funcion elif + !=" tambien se podria usar "else" 
        a='false'
    print(value,a)
