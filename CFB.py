'''Olivares Romero José Alejandro'''


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

'''Esta función recibe la cadena de la llave y devuelve una lista con el indice de cada caractér de la llave'''
def indexkey(key):
    a = 'abcdefghijklmnopqrstuvwxyz'
    k = [a.find(i) for i in key]
    return k

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
'''
Para el primer bloque
1. Ciframos al vector de inicialización.
2. Hacemos la operación xor entre los bloques del texto con el resultado del cifrado del vector de inicialización
3. El resultado del paso 2 será el vector de inicialización del siguiente bloque, a su vez será parte del texto cifrado.

Para el resto de los bloques
4. El vector de inicialización será el resultado de la operación xor del bloque de texto plano 
con el resultado del cifrado de Vigenere del bloque anterior.
'''
def cfbCifrado(pt,iv,segmento,k,alphabet):
    ct = ""
    pt = arreglarCadena(pt,alphabet)    
    bloquesPt = dividirCadena(pt,segmento)        

    for i in range(len(bloquesPt)):
        vc = encryptionVigenere(iv,k,alphabet)
        xor = xorFuncion(bloquesPt[i],vc,alphabet)
        ct += xor
        iv = xor            
    return ct

'''
Para el primer bloque
1. Ciframos por Vigenere al vector de inicialización.
2. Hacemos la operación xor entre los bloques del texto cifrado con el resultado del cifrado del vector de inicialización.
El resultado será un bloque de nuestro texto plano

Para el resto de los bloques
3. El bloque de texto anterior a la posición actual será el que entrará al cifrado de Vigenere.
Hacemos la operación xor entre el bloque del texto cifrado de la posicón actual con el resultado del cifrado de Vigenere.
El resultado será un bloque de nuestro texto plano

'''

def cfbDecifrado(ct,iv,segmento,k,alphabet):
    pt = ""    
    bloquesCt = dividirCadena(ct,segmento)    

    for i in range(len(bloquesCt)):        
        vc = encryptionVigenere(iv,k,alphabet)  
        xor = xorFuncion(vc,bloquesCt[i],alphabet)        
        pt += xor
        iv = bloquesCt[i]        

    return pt

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","{","<",">","}"]


read500 = open("500.txt","r")
pt = read500.readline()
read500.close()
iv = "aaa"
k = indexkey('hola')

create500CT = open("500CT.txt","w")
ct = cfbCifrado(pt,iv,len(iv),k,alphabet)
create500CT.write(ct)
create500CT.close()

getPt = cfbDecifrado(ct,iv,len(iv),k,alphabet)
print(getPt.upper())
create500PT = open("500PT.txt","w")
create500PT.write(getPt)
create500PT.close()