#Buscador de permutaciones y llaves
import itertools
#HNAOEYDMIINCUAEQRCEUQLUOOECNAULREALFICDCXAYD
ct = "HNAO"
lugares = []
for i in range(len(ct)):
    pos = str(i+1)
    pos += ct[i]
    lugares.append(pos)

permutations = list(itertools.permutations(lugares))

ct = "EYDM"
lugares = []
for i in range(len(ct)):
    pos = str(i+1)
    pos += ct[i]
    lugares.append(pos)

permutations2 = list(itertools.permutations(lugares))

c = 0
llave = 0
for n in range(len(permutations)):
    fila = ""
    fila2 = ""
    fila = permutations[n]
    fila2 = permutations2[n]    
    c += 1
    cadena = ""   
    cadena2 = ""
    posicion = ""     
    for i in range(len(fila)):
        cadena += fila[i][1]
        cadena2 += fila2[i][1]
        posicion += fila[i][0]    
    print("("+str(c)+")")
    cadena = cadena+cadena2
    print(cadena)
    print(posicion)    
    print("-"*len(fila))

