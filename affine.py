
alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def affineCipher(n,m,a,b):
    x = alfabeto.index(m)
    newIndex = x*a+b
    nuevaPosicion = newIndex % n    
    return alfabeto[nuevaPosicion]

def deciphersaffineCipher(n,ci,a,b):
    c = alfabeto.index(ci)
    contador = 1
    while contador < n:
        if((a*contador)%n==1):
            inverso = contador            
            break
        contador = contador+1                    
    posicion = inverso*(c-b)%n

    return alfabeto[posicion]


#print(affineCipher(26,"f",5,8))
print(deciphersaffineCipher(26,affineCipher(26,"s",0,0),0,0))

