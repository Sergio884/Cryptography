''' Para eliminar simbolos o caracteres que no pertenecen al alfabeto '''
def arreglarCadena(cadena,alphabet):    
    newCadena = ""
    for i in cadena.lower():
        if alphabet.count(i)==1:
            newCadena+=i            
    return newCadena

'''Esta funcion sirve para dividir una cadena en segmentos de un tamanio determinado'''
def dividirCadena(cadena,segmento):
    separadores = []
    if len(cadena)%segmento!=0:
        '''Se concatena x al final en caso de que no se complete un segmento'''
        cadena += "x"*(segmento-len(cadena)%segmento)

    for i in range(int(len(cadena)/segmento)):    
        separadores.append(cadena[(i*segmento):((i+1)*segmento)])        
    return separadores


def xorFuncion(entrada,iv,alphabet):
    cadena = ""
    for i in range(0,len(entrada)):
        cadena += alphabet[(alphabet.index(entrada[i])^alphabet.index(iv[i]))%len(alphabet)]
    return cadena

def encryptionVigenere(pt,k,alphabet):    
    ct = ""
    cont = 0
    for c in pt:
        ct += alphabet[(alphabet.index(c)+(k[cont%len(k)]))%len(alphabet)]            
        cont += 1        
    return (ct)

def decryptionVigenere(ct,k,alphabet):    
    pt = ""
    cont = 0
    for c in ct:
        pt += alphabet[(alphabet.index(c)-(k[cont%len(k)]))%len(alphabet)]            
        cont += 1            
    return (pt)

def cbcCifrado(pt,iv,segmento,k,alphabet):
    ct = ""
    pt = arreglarCadena(pt,alphabet)    
    bloquesPt = dividirCadena(pt,segmento)        

    for i in range(len(bloquesPt)):
        xor = xorFuncion(bloquesPt[i],iv,alphabet)
        vc = encryptionVigenere(xor,k,alphabet)
        ct += vc
        iv = vc            
    return ct

def cbcDecifrado(ct,iv,segmento,k,alphabet):
    pt = ""    
    bloquesCt = dividirCadena(ct,segmento)    

    for i in range(len(bloquesCt)):        
        vc = decryptionVigenere(bloquesCt[i],k,alphabet)  
        xor = xorFuncion(vc,iv,alphabet)        
        pt += xor
        iv = bloquesCt[i]        

    return pt

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","{","<","¬","^",">","}"]

read500 = open("500.txt","r")
pt = read500.readline()
read500.close()
iv = "aaa"
k = (1,1,1)

create500CT = open("500CT.txt","w")
ct = cbcCifrado(pt,iv,len(iv),k,alphabet)
create500CT.write(ct)
create500CT.close()

getPt = cbcDecifrado(ct,iv,len(iv),k,alphabet)
print(getPt)
create500PT = open("500PT.txt","w")
create500PT.write(getPt)
create500PT.close()