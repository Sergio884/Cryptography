n = 127
auxN = n
llaves = True
resto = n
valores = []
i = 2
while auxN>1:    
    if(auxN % i == 0):
        auxN = auxN/i
        valores.append(i)        
    else:
        i = i+1
print(valores)

anterior = 0
resultado  = 1
for valor in valores:
    if (valores.count(valor)>1 and  anterior!=valor):
        resultado = resultado * valor**valores.count(valor)-valor**(valores.count(valor)-1)
        anterior = valor        
    elif (anterior!=valor):
        resultado = resultado * (valor-1) 

if llaves:
    print(resultado)
    print("Llaves Posibles: "+str((resultado*n)))
else:
    print(resultado)