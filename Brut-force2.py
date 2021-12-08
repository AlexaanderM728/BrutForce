"""
authors: Aleksander Mazurek , Zuzanna Borkowska
"""
import random
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import sys
BLOCK_SIZE = 32
"""
    msg is varaible that stores encrypted message
"""
text = b"M\xe9\x07M\x0c\x1f3\xa0\x88L\x08\xde\x9c[\xac\x97;\xe3\xac\x02z\xde\xc7'\xcdx+\xfc\x9b\x0fcr \xed\x0fX\xab\xe7\xed\xba}\xefP\x90-\x92\xb9\xe4+\xc5\xc0\xc4\xc1\x01\xd1oZ\x1eD*\xc6\xf6Ze\xe1\xc8i\xec\x94\xa9\xf0~\xa3\xf1\r]6M\x97\xc8\x80\xce\x1a\x0f\xc9Ky\xd0\x07c=YL\xc1\xff\xb99b\x08\xda\xce\x93\x05\xfc\xe3\x8c\x11\xf7w\xce\xec$\xceu\xb8\xbf\xd5xI\x97\xe1\xe4\xfaK\x11\xb2z\xaaP,Q\xe7\xb7<\xef7\xff\x862\xd0dz^\xb5\r\x89\x8a\xd2d\x8d\xc8\xe7q\xe7\x1e89\x9aN9\x11\xdaHX\xb6\xb0\xe2\x8b^Z\xd3\x87P\xe7;\x87\xd1z^\xa3!\x12g*f\xb1Fe\xdd\x1a\xeb\xde\xc3\x8d\xfd\x99\x7f\xb7\xc4\xdd\x94\xf6\xdd\xd71\x9b\x0e\x04:\x18-\xee}\x0f\xa8#\x15ff\x9a\x9d\xfb\x8fl"
"""def stop is guess_key loop stop condition"""
def stop(key, text):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("FOUND!")
    print(key, ':', text)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!")
    sys.exit(0)

def guess_key():
    character = "abcdefghijklmnoprstuwxyz"
    character_list = list(character)
    """
       character_list is an array containing letters from a-z. This is needed to be able to draw letters at a later stage.
    """
    while True:
        """
           In this loop, each time a number between 4 and 12 is drawn to represent the length of the key. 
           It is stored in the variable rand_number. Then a string from the character_list array with length
           according to rand_number is stored in the guess variable.
        """
        rand_number = random.randint(4,12)
        guess = random.choices(character_list,k=rand_number)
        guess = "".join(guess)
        key = guess

        try:
            """
            the key is used to encrypt an encrypted message. Then the encrypted message is decrypted again.  
            compares the new encrypted message with the attacked message.  If the key is correct, we will get the same hard-coded message as the attacked message.
            it is enough to use the found key and decrypt it twice with the DES algorithm
            """
            des = DES.new(key, DES.MODE_ECB)
            print("=============================")
            print('KEY:    ', key)
            print("SECRET MESSAGE")
            msg = des.encrypt(pad(text, BLOCK_SIZE))
            print("msg:    ", msg)
            dmsg = des.decrypt(msg)
            print("dmsg:   ", dmsg)
            print("Orginal message")
            print("text:   ", text)
            crack = des.decrypt(des.decrypt(msg))
            print("CRACK:  ", crack)
            print("=============================")
            """crack[:-32] cuts off empty bytes"""
            crack = crack[:-32]
            """ccrack is copy crack and convert to string"""
            ccrack = str(crack)
            """if loops are needed to check if the variable crack contains bytes elements"""
            if ccrack.find("\"" or "&" or "$") != -1:
                continue
            elif ccrack.find("xb" or "xa" or 'xe') != -1:
                continue
            else:
                stop(key, ccrack)
        except:
            print(key,":Wrong key to encode message")

"""start brute-force"""
guess_key()
