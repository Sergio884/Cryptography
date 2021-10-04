cadena = "1234567890"
separadores = []

newCadena = cadena
if len(cadena)%3!=0:
    newCadena += " "*(3-len(cadena)%3)

for i in range(int(len(newCadena)/3)):    
    separadores.append(newCadena[(i*3):((i+1)*3)])
    
print(separadores)