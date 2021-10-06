def arreglarCadena(cadena,alphabet):    
    newCadena = ""
    for i in cadena.lower():
        if alphabet.count(i)==1:
            newCadena+=i
    return newCadena


def dividirCadena(cadena,segmento):
    separadores = []
    if len(cadena)%segmento!=0:
        cadena += "x"*(segmento-len(cadena)%segmento)

    for i in range(int(len(cadena)/segmento)):    
        separadores.append(cadena[(i*segmento):((i+1)*segmento)])        
    return separadores


def xorF(entrada,iv,alphabet):
    cadena = ""
    for i in range(0,len(entrada)):
        cadena += alphabet[((ord(entrada[i])^ord(iv[i]))%len(alphabet))]
    return cadena

def encryption(pt,k,alphabet):    
    ct = ""
    cont = 0
    for c in pt:
        ct += alphabet[(alphabet.index(c)+(k[cont%len(k)]))%len(alphabet)]            
        cont += 1        
    return (ct)

def cbc(pt,iv,segmento,k,alphabet):
    newPt = arreglarCadena(pt,alphabet)
    bloquesPt = dividirCadena(newPt,segmento)
    xor = xorF(bloquesPt[0],iv,alphabet)
    vc = encryption(xor,k,alphabet)

    print(vc)

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
pt = "e b*Z ddh aje fe"
iv = "bba"
k = (1,2,3)


cbc(pt,iv,3,k,alphabet)