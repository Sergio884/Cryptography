#Affine Cipher Extendido

alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def affineCipher(n,m,a,b):
    x = alfabeto.index(m)
    newIndex = x*a+b
    nuevaPosicion = newIndex % n    
    return alfabeto[nuevaPosicion]

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
ct = "V URNE NAQ V SBETRG V FRR NAQ V ERZRZORE V QB NAQ V HAQREFGNAQ"
for i in range(1,a):    
    for j in range(1,a):             
        cadena = ""
        for c in ct:
            if c!=" ":
                cadena += deciphersaffineCipher(a,c,i,j)
            else:
                cadena += " "
        
        if(cadena.count("A")+cadena.count(" "))!=len(cadena):
            print("---------------------")
            print(str(i)+" ,"+str(j))        
            print(cadena)


