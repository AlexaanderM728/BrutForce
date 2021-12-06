import random

character = "abcdefghijklmnoprstuwxyz"
character_list = list(character)
password = input("enter u pasword: ")
guess = ""
while(guess != password):
    guess = random.choices(character_list, k=len(password))
    print(guess)
    guess = "".join(guess)
    print(guess)
print("u pass: " + guess)