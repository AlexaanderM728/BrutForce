# Zuzanna Borkowska (s21243) Aleksander Mazurek (s15230)
import random
from Crypto.Cipher import DES
from multiprocessing import Process
"""
    msg is varaible that stores encrypted message
"""
msg = b"M\xe9\x07M\x0c\x1f3\xa0\x88L\x08\xde\x9c[\xac\x97;\xe3\xac\x02z\xde\xc7'\xcdx+\xfc\x9b\x0fcr \xed\x0fX\xab\xe7\xed\xba}\xefP\x90-\x92\xb9\xe4+\xc5\xc0\xc4\xc1\x01\xd1oZ\x1eD*\xc6\xf6Ze\xe1\xc8i\xec\x94\xa9\xf0~\xa3\xf1\r]6M\x97\xc8\x80\xce\x1a\x0f\xc9Ky\xd0\x07c=YL\xc1\xff\xb99b\x08\xda\xce\x93\x05\xfc\xe3\x8c\x11\xf7w\xce\xec$\xceu\xb8\xbf\xd5xI\x97\xe1\xe4\xfaK\x11\xb2z\xaaP,Q\xe7\xb7<\xef7\xff\x862\xd0dz^\xb5\r\x89\x8a\xd2d\x8d\xc8\xe7q\xe7\x1e89\x9aN9\x11\xdaHX\xb6\xb0\xe2\x8b^Z\xd3\x87P\xe7;\x87\xd1z^\xa3!\x12g*f\xb1Fe\xdd\x1a\xeb\xde\xc3\x8d\xfd\x99\x7f\xb7\xc4\xdd\x94\xf6\xdd\xd71\x9b\x0e\x04:\x18-\xee}\x0f\xa8#\x15ff\x9a\x9d\xfb\x8fl"

def guess_key():
    character = "abcdefghijklmnoprstuwxyz"
    character_list = list(character)
    """
       character_list is an array containing letters from a-z. This is needed to be able to draw letters at a later stage.
    """
    while(True):
        """
           In this loop, each time a number between 4 and 12 is drawn to represent the length of the key. 
           It is stored in the variable rand_number. Then a string from the character_list array with length
           according to rand_number is stored in the guess variable.
        """
        rand_number = random.randint(4,12)
        guess = random.choices(character_list,k=rand_number)
        guess = "".join(guess)
        """
        Based on the drawn key (guess variable) an attempt is made to decrypt the message stored in the msg variable. 
        The key in the DES.new function is also encoded according to ascii. If the attempt is successful the message is printed to the console and the loop stops.
        Otherwise a message about a wrong key is printed. 
        """
        try:
            des = DES.new(guess.encode('ascii'), DES.MODE_ECB)
            mess = des.decrypt(msg)
            print(mess.decode('UTF-8'))
        except:
            print("Wrong key to encode message")
"""
mulirporccesing guess_key function
"""
def main():
    p1 = Process(target=guess_key())
    p1.start()

    p2 = Process(target=guess_key())
    p2.start()

    p3 = Process(target=guess_key())
    p3.start()

    p1.join()
    p2.join()
    p3.join()


"""start brute-force"""
if __name__ == '__main__':
    main()
