from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = b'rfghuioftedgydrf'
cipher = AES.new(key, AES.MODE_CBC)

#plaintext = b'Pvto el que lo lea'
pFile = open("Plaintext_IN","rb")
plaintext = pFile.read()
pFile.close

ciphertext = cipher.encrypt(pad(plaintext,AES.block_size))

cFile = open("Cipher","wb")
cFile.write(cipher.iv)
cFile.write(ciphertext)
cFile.close()