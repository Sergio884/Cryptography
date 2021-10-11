def convertBits(iv):
    iv+="s"
    letra = ""
    newIV=""
    cont = 0
    for l in iv:               
        if cont < 8:
            letra+=l
        else:            
            n = int(letra,2)            
            newIV+=chr(n)
            cont=0
            letra=""        
        cont+=1
    return newIV

iv = "01100001011000010110000101100010"
print(convertBits(iv))