def xorFuncion(entrada,iv,alphabet):
    cadena = ""
    for i in range(0,len(entrada)):
        cadena += alphabet[(alphabet.index(entrada[i])^alphabet.index(iv[i]))%len(alphabet)]
    return cadena

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
entrada = "str"
iv = "kkk"

print(xorFuncion(entrada,iv,alphabet))