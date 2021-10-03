z = 26
r = ""
fila = ""
for i in range(1,z):    
    if(i<10):
        fila = fila+" "+str(i)+" "
    else:
        fila = fila+str(i)+" "

    
print(" * "+fila)


for i in range(1,z):    
    fila=""
    for j in range(1,z):              
        if(((i*j)%z)==1 ):
            r = r+"("+str(i)+"*"+str(j)+") mod "+str(z)+" = 1  \n"
        if(((i*j)%z)<10):
            fila = fila+" "+str((i*j)%z)+" "
        else:
            fila = fila+str((i*j)%z)+" "

    if(i<10):
        print(" "+str(i)+"|"+fila)
    else:
        print(str(i)+"|"+fila)    

print(r)