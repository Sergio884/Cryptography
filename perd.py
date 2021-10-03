#Decifrador de permutaciones
ct = "NSORPIDOGRNMAERSN-O-"
#51234
llave = [2,4,1,3]

texto = ""
paquete = ""
cont = 0
for letra in ct:
    paquete += letra
    cont += 1
    if cont==len(llave):
        for i in range(len(llave)):
            texto += paquete[llave[i]-1]        
        paquete=""
        cont = 0        
    
print(texto)
    




    

