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


def xorFuncion(entrada,iv,alphabet):
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
    ct = ""
    newPt = arreglarCadena(pt,alphabet)
    bloquesPt = dividirCadena(newPt,segmento)

    for i in range(len(bloquesPt)):
        xor = xorFuncion(bloquesPt[i],iv,alphabet)
        vc = encryption(xor,k,alphabet)
        ct += vc
        iv = vc        

    return ct

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
read500 = open("500.txt","r")
pt = read500.readline()
read500.close()
iv = "bba"
k = (1,2,3)

create500CT = open("500CT.txt","w")
print(cbc(pt,iv,3,k,alphabet))
create500CT.write(cbc(pt,iv,3,k,alphabet))
create500CT.close()