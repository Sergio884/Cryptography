from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key = b'rfghuioftedgydrf'
cFile = open("Cipher","rb")
iv = cFile.read(len(key))
ciphertext = cFile.read()
cFile.close()

cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
print(plaintext)

pFile = open("Plaintext_OUT.txt","wb")
pFile.write(plaintext)
pFile.close()