from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
import base64

leer = open("5mb.txt","r")
lectura = leer.readlines()

linea = ""
for l in lectura:
    linea+=l
leer.close()

llave = open("key.txt","w")

while True:
    try:
        key = DES3.adjust_key_parity(get_random_bytes(24))        
        base64_bytes = base64.b64encode(key)
        base64_message = base64_bytes.decode('ascii')         
        llave.write(str(key))        
        llave.close()
        
        break
    except ValueError:
        pass

leerKey = open("key.txt","r")
keyObtenida = leerKey.readline()
leerKey.close()
cipher = DES3.new(key, DES3.MODE_CFB)
plaintext = bytes(linea,'utf-8')
msg = cipher.iv + cipher.encrypt(plaintext)

crearDES = open("5mb.des","w")
base64_bytes = base64.b64encode(msg)
base64_message = base64_bytes.decode('ascii')   
crearDES.write(base64_message)
crearDES.close()