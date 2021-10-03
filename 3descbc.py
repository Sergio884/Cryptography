from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import codecs

leer = open("5mb.txt","r")
lectura = leer.readlines()

linea = ""
for l in lectura:
    linea+=l
leer.close()

data = bytes(linea,"utf-8")
key = get_random_bytes(16)
keyCBC = open("keyCBC.txt","w")
keyCBC.write(str(key))
keyCBC.close()
readKey = open("KeyCBC.txt","r")
llave = readKey.readline()
readKey.close()


cipher = AES.new(key, AES.MODE_CBC)
ct_bytes = cipher.encrypt(pad(data, AES.block_size))
iv = b64encode(cipher.iv).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')

cbc = open("CBC.txt","w")
cbc.write("IV: "+str(iv)+"\n"+"CT: "+str(ct))
cbc.close()