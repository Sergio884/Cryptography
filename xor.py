def xor(entrada,iv,alphabet):
    cadena = ""
    for i in range(0,len(entrada)):
        cadena += alphabet[((ord(entrada[i])^ord(iv[i]))%len(alphabet))]
    return cadena

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
entrada = "SAN"
iv = "BBB"

print(xor(entrada,iv,alphabet))