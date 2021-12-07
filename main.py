from Crypto.Util.Padding import pad
from Crypto.Cipher import DES
key = b'passpass'

BLOCK_SIZE = 32

text =b'ODGADNIJ MNIE UKRYTA WIADOMOSC'

des = DES.new(key, DES.MODE_ECB)
print("SECRET MESSAGE")
msg = des.encrypt(pad(text, BLOCK_SIZE))
print(msg)
print("Orginal message")
print(des.decrypt(msg))
