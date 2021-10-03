def permutar(c):
    codigo = bin(ord(c))

    completo = ""
    if len(codigo[2:])!=8:
        completo += "0"*(8-len(codigo[2:]))
    completo += codigo[2:]

    permutacion = [2,4,1,6,3,0,7,5]
    nuevoOrden  = [0,0,0,0,0,0,0,0]
    cont = 0

    for c in completo:
        nuevoOrden[permutacion[cont]] = c
        cont+=1
    
    salida = "0b"
    for b in nuevoOrden:
        salida+=b    
    print(salida)

permutar("<")