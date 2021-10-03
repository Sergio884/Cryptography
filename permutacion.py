import itertools
#HNAO EYDM IINC UAEQ RCEUQLUOOECNAULREALFICDCXAYD
ct = "ESCOM"
lugares = []
for i in range(len(ct)):
    pos = str(i+1)
    pos += ct[i]
    lugares.append(pos)

permutations = list(itertools.permutations(lugares))

c = 0
llave = 0
for fila in permutations:    
    c += 1
    cadena = ""   
    posicion = ""     
    for i in range(len(fila)):
        cadena += fila[i][1]
        posicion += fila[i][0]    
    if(c==llave and llave!=0):
        print("("+str(c)+")")
        print(cadena)
        print(posicion)    
        print("-"*len(fila))
    elif(llave==0):
        print("("+str(c)+")")
        print(cadena)
        print(posicion)    
        print("-"*len(fila))

