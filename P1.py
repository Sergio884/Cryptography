"""
Escuela Superior de Computo
Criptografía
Práctica Uno - 13/Sep/2021

Integrantes:
Juan Lopéz Gutierrez (Punto dos)
Elias Muñoz Primero (Punto uno y dos)
Edilberto Sergio Valle Ortiz (Punto tres y cuatro)

Descripcion:
A través de este documento, se da solucion a cuatro planteamientos solicitados en la clase.
Punto 1: Escribir una función que implemente el algoritmo extendido de euclides.
Punto 2: Escribir una función que genere dado un entero 'n' una matriz 3x3 valida para el cifrado Hill.
Punto 3: Escribir una función que regrese la matriz inversa dada una que sea 3x3.
Punto 4: Escribir una función que deje probar el hecho de que la matriz 3x3 multiplicada por su inversa da a la matriz identidad.
⣿⣿⣿⠟⠛⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢋⣩⣉⢻⣿⣿ 
⣿⣿⣿⡀⣿⣿⣿⣶⣕⣈⠹⠿⠿⠿⠿⠟⠛⣛⢋⣰⠣⣿⣿⣿ 
⣿⣿⣿⡀⣿⣿⣿⣧⢻⣿⣶⣷⣿⣿⣿⣿⣿⣿⠿⠶⡝⠀⣿⣿ 
⣿⣿⣿⣷⠘⣿⣿⣿⢏⣿⣿⣋⣀⣈⣻⣿⣿⣷⣤⣤⣿⡐⢿⣿ 
⣿⣿⣿⣿⣆⢩⣝⣫⣾⣿⣿⣿⣿⡟⠿⠿⠦⠀⠸⠿⣻⣿⡄⢻ 
⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⠇⣼ 
⣿⣿⣿⣿⣿⣿⡄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣰⣿ 
⣿⣿⣿⣿⣿⣿⠇⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⣿⣿ 
⣿⣿⣿⣿⣿⠏⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿ 
⣿⣿⣿⣿⠟⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿ 
⣿⣿⣿⠋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⣿⣿ 
⣿⣿⠋⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿
"""
import random
from math import gcd

# Punto uno
# Nota: debudo a que la variable 'r' siempre da cero, se obto por implementar la funcion gcd de python en el punto dos
def EjercicioUno(a,n):
	u=a;v=n;x1=1;x2=0
	while u!=0:
		q=(v//u);r=(v-q*u);x=(x2-q*x1);
		v=u;u=r;x2=x1;x1=x;	
	print(" x1: {} y n: {} \n Resultado: {}".format(x1,n,x1%n))
	return(x1%n)

# Punto dos
def EjercicioDos(n):
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
			number = random.randint(0,n)
			Matrix[f][c] = number

def determinante(Matrix):
	det=Matrix[0][0]*(Matrix[1][1]*Matrix[2][2]-Matrix[2][1]*Matrix[1][2])-Matrix[0][1]*(Matrix[1][0]*Matrix[2][2]-Matrix[2][0]*Matrix[1][2])+Matrix[0][2]*(Matrix[1][0]*Matrix[2][1]-Matrix[2][0]*Matrix[1][1])
	return det



# Punto tres
def EjercicioTres(key,n):
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
def EjercicioCuatro(key,inversematrix):
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


#a = int(input("a > "))
#n = int(input("n > "))
#EjercicioUno(a,n)
n = int(input("Tam Alfabeto > "))
key = EjercicioDos(n)
inversa = EjercicioTres(key,n)
EjercicioCuatro(key,inversa)