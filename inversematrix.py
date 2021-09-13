#Edilberto Sergio Valle Ortiz
####3####
key = [[ 6,24, 1],
       [13,16,10],
       [20,17,15]]

#Se crea una matriz  3X3 inversa vacia
inversematrix = [[0,0,0],[0,0,0],[0,0,0]]

#Se calcula la determinante de la matriz llave
det=key[0][0]*(key[1][1]*key[2][2]-key[2][1]*key[1][2])-key[0][1]*(key[1][0]*key[2][2]-key[2][0]*key[1][2])+key[0][2]*(key[1][0]*key[2][1]-key[2][0]*key[1][1])

#Con el siguiente algoritmo se calcula el inverso multiplicativo
n = 26
a = det%n
inverso = 0
contador = 0
while contador < n:
    #Cuando un valor multiplicado por a mod n es igual a 1,
    #entonces el el inverso multiplicativo buscado
        if((a*contador)%n==1):
            inverso = contador            
            break
        contador = contador+1

#Se calcula la adjunta de key y es multilpicada por el inverso obtenido,
#y al resultado se le calcula el modulo con el alfabeto
inversematrix[0][0] = (key[1][1]*key[2][2]-key[2][1]*key[1][2])*inverso%n
inversematrix[1][0] =((key[1][0]*key[2][2]-key[2][0]*key[1][2])*(-1))*inverso%n
inversematrix[2][0] = (key[1][0]*key[2][1]-key[2][0]*key[1][1])*inverso%n
inversematrix[0][1] =((key[0][1]*key[2][2]-key[2][1]*key[0][2])*(-1))*inverso%n
inversematrix[1][1] = (key[0][0]*key[2][2]-key[2][0]*key[0][2])*inverso%n
inversematrix[2][1] =((key[0][0]*key[2][1]-key[2][0]*key[0][1])*(-1))*inverso%n
inversematrix[0][2] = (key[0][1]*key[1][2]-key[1][1]*key[0][2])*inverso%n
inversematrix[1][2] =((key[0][0]*key[1][2]-key[1][0]*key[0][2])*(-1))*inverso%n
inversematrix[2][2] = (key[0][0]*key[1][1]-key[1][0]*key[0][1])*inverso%n

####4####

#Se imprime la matriz llave
for fila in key:
    print(fila)

print("     *")

#Se prime la matriz inversa
for fila in inversematrix:
    print(fila)

#Se crea una matriz identidad vacia
identityMatrix = [[0,0,0],[0,0,0],[0,0,0]]

#Se aplica la multiplicacion de ambas matrices
#El algoritmo aplica para multiplicacion de
#matrices NXN
for i in range(len(key)):   
   for j in range(len(inversematrix[0])):       
       for k in range(len(inversematrix)):
           identityMatrix[i][j] += key[i][k] * inversematrix[k][j]

print("       =")
#Se imprime el resultado de la multiplicacion
for fila in identityMatrix:
    print(fila)    
print("    mod "+str(n))

#Ahora se saca el modulo n a cada casilla
for i in range(len(inversematrix)):
    for j in range(len(inversematrix)):
         identityMatrix[i][j]= identityMatrix[i][j]%n
    
print("       =")
#Se imprime la matriz identidad resultante
for fila in identityMatrix:
    print(fila)