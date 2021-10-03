from Crypto.Cipher import DES

readFile = open("cadena.txt","r")
read = readFile.readline()
readFile.close()

key = b'-8B key-'
cipher = DES.new(key, DES.MODE_OFB)
plaintext = bytes(read,'utf-8')
msg = cipher.iv + cipher.encrypt(plaintext)
print(msg)