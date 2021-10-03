#Encriptador por permutaciones
ct = "GOD REWARDS FOOLS"
llave = [2,3,4,5,1]

texto = ""
paquete = ""
cont = 0
for letra in ct:
    if letra != " ":
        paquete += letra
        cont += 1    
    if cont==len(llave):        
        for i in range(len(llave)):
            texto += paquete[llave[i]-1]        
        paquete=""
        cont = 0        
    
print(texto)
    



