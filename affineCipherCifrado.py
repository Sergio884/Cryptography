#Affine Cipher Extendido

alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def affineCipher(n,m,a,b):
    x = alfabeto.index(m)
    newIndex = x*a+b
    nuevaPosicion = newIndex % n    
    return alfabeto[nuevaPosicion]


a = 35
i = 6
j = 25

ct = "AFFINE CIPHER"            
cadena = ""
for c in ct:
    if c!=" ":
        cadena += affineCipher(a,c,i,j)
    else:
        cadena += " "        
print(cadena)

