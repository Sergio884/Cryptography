def xorAscii(entrada,iv):
    cadena = ""
    for i in range(0,len(entrada)):
        cadena += chr(ord(entrada[i])^ord(iv[i]))
    return cadena

def xorAlfabeto(entrada,iv,alfabeto):
    cadena = ""
    for i in range(0,len(entrada)):
        cadena += alfabeto[(alfabeto.index(entrada[i])^alfabeto.index(iv[i]))]
    return cadena

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
entrada = "san"
iv = "bbb"

print(xorAscii(entrada,iv))
print(xorAlfabeto(entrada,iv,alphabet))