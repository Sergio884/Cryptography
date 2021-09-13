n = 26
a = 3
inverso = 0
contador = 0
while contador < n:
        if((a*contador)%n==1):
            inverso = contador            
            break
        contador = contador+1

if(inverso==0):
    print("No existe")
else:
    print(inverso)

#  3n  + 6

# (8)