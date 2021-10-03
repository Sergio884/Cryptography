import random
from math import gcd



# Punto dos
def crearLlave(n):
	Matrix = [[0,0,0],[0,0,0],[0,0,0]]	
	GeneraMatriz(Matrix,n)
	det = determinante(Matrix)
	while (det==0 or gcd(det%n,n)!=1):
		GeneraMatriz(Matrix,n)
		det = determinante(Matrix)	
	return Matrix

def GeneraMatriz(Matrix,n):
	for f in range(len(Matrix)):
		for c in range(len(Matrix)):
			number = random.randint(0,n-1)
			Matrix[f][c] = number

def determinante(Matrix):
	det=Matrix[0][0]*(Matrix[1][1]*Matrix[2][2]-Matrix[2][1]*Matrix[1][2])-Matrix[0][1]*(Matrix[1][0]*Matrix[2][2]-Matrix[2][0]*Matrix[1][2])+Matrix[0][2]*(Matrix[1][0]*Matrix[2][1]-Matrix[2][0]*Matrix[1][1])
	return det

def guardarLlave(key,n):
    alfabeto = obtenerAlfabeto(n)
    nombre = ""
    nombre = str(input("Nombre del archivo por crear: "))
    archivo = open(nombre+".txt","w")

    llaveCreada = ""
    for fila in key:
        for elemento in fila:
            llaveCreada += alfabeto[elemento]

    archivo.write(llaveCreada)
    archivo.close()


def buscarLlave(n):
    alfabeto = obtenerAlfabeto(n)    
    busqueda = ""
    busqueda = str(input("Nombre del archivo por buscar: "))
    llaveArchivo = open(busqueda+".txt","r")
    llaveCadena = llaveArchivo.readline()
    llaveArchivo.close()

    keyArchivo = [[ 0,0, 0],
                [0,0,0],
                [0,0,0]]

    contador = 0
    for i in range(0,3):    
        for j in range(0,3):                
            keyArchivo[i][j] = alfabeto.index(llaveCadena[contador])
            contador += 1

    return(keyArchivo)

# Punto tres
def obtenerMatrizInversa(key,n):
	#Se crea una matriz  3X3 inversa vacia
	inversematrix = [[0,0,0],[0,0,0],[0,0,0]]
	#Se calcula la determinante de la matriz llave
	det=key[0][0]*(key[1][1]*key[2][2]-key[2][1]*key[1][2])-key[0][1]*(key[1][0]*key[2][2]-key[2][0]*key[1][2])+key[0][2]*(key[1][0]*key[2][1]-key[2][0]*key[1][1])
	#Con el siguiente algoritmo se calcula el inverso multiplicativo	
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
	return(inversematrix)

# Punto cuatro
def comprobarMatrizIdentidad(key,inversematrix):
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
    
#En esta función se obtiene el alfabeto con el que se está trabajando
#Se es uno igual a 26, entonces se trata del alfabeto ingles
#Si es igual a 27 es el alfabeto español
#y si es igual a 30, es el alfabeto aleman
def obtenerAlfabeto(n):
    alfabeto = []
    if n == 26:
        alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    elif n == 27:
        alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    elif n == 30:
        alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","ä","ö","ü","ß"]
    return(alfabeto)

n = int(input("Tamaño del Alfabeto : "))

keyGenerada = crearLlave(n)
guardarLlave(keyGenerada,n)
key = buscarLlave(n)
inversa = obtenerMatrizInversa(key,n)
comprobarMatrizIdentidad(key,inversa)