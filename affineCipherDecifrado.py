#Affine Cipher Extendido

alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def deciphersaffineCipher(n,ci,a,b):
    c = alfabeto.index(ci)
    contador = 1
    inverso = 0
    while contador < n:
        if((a*contador)%n==1):
            inverso = contador            
            break
        contador = contador+1                    
    posicion = inverso*(c-b)%n

    return alfabeto[posicion]


#print(affineCipher(26,"f",5,8))

a = 26
i = 15
j = 2

ct = "KFKXYREVY LSKM"            
cadena = ""
for c in ct:
    if c!=" ":
        cadena += deciphersaffineCipher(a,c,i,j)
    else:
        cadena += " "        
print(cadena)

