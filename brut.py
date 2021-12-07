import random
import main
from Crypto.Cipher import DES

def compare_key(key):
    character = "abcdefghijklmnoprstuwxyz"
    character_list = list(character)
    key_decoded = key.decode('UTF-8')
    """
    character_list is an array containing letters from a-z. This is needed to be able to draw letters at a later stage.
    Since the key from main is not a string, we decode it according to UTF-8
    """
    while(True):
        """
            In this loop, each time the guess variable is compared to the decoded key. 
            Guess is a variable that stores the random string 
            from the character_list array with the length of characters
            that is equal to the number of characters of the decoded key
            If key_decoded is equal to generated value (guess) the loop break and function return this value
        """
        guess = random.choices(character_list, k=len(key_decoded))
        guess = "".join(guess)
        """
             We print guess to show that the program actually doing something
        """
        print(guess)
        if(key_decoded == guess):
            break

    return guess

"""
  guessed_key is a variable that holds the value returned by the function compare_key
  then according to this variable we will decode the message from main.py
"""
guessed_key = compare_key(main.key)
des = DES.new(guessed_key, DES.MODE_ECB)
mess = des.decrypt(main.msg)
print("Your message is: " + mess)
