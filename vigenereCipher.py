alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def encryption(pt,k,alphabet):    
    ct = ""
    cont = 0
    for c in pt:
        ''' Esto se hace para eliminar los espacios o ciertos caracteres 
        que no esten en  el alfabeto, y .lower() sirve para pasar a minuscula'''
        if  alphabet.count(c.lower())==1:
            '''Se le concatena a otra cadena el caracter valido'''
            ct += alphabet[(alphabet.index(c.lower())+(k[cont%len(k)]))%len(alphabet)]            
            cont += 1        
    return (ct.upper())

def decryption(ct,k,alphabet):
    pt = ""
    cont = 0
    for c in ct:
        ''' Esto se hace para eliminar los espacios o ciertos caracteres 
        que no esten en  el alfabeto, y .lower() sirve para pasar a minuscula'''
        if  alphabet.count(c.lower())==1:
            '''Se le concatena a otra cadena el caracter valido'''
            pt += alphabet[(alphabet.index(c.lower())-(k[cont%len(k)]))%len(alphabet)]            
            cont += 1        
    return (pt.upper())

pt = "Esta es una cadena de tres leones ambrientoz en buzka de sexo y vida en wichinton"
k = (1,2,3)

print(encryption(pt,k,alphabet))
print(decryption( encryption(pt,k,alphabet) ,k,alphabet))


