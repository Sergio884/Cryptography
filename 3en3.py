cadena = "abdddhaj"
separadores = []

if len(cadena)%3!=0:
    cadena += " "*(3-len(cadena)%3)

for i in range(int(len(cadena)/3)):    
    separadores.append(cadena[(i*3):((i+1)*3)])
    
print(separadores)