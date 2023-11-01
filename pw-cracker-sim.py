
from random import *
import os

user_passord = input("Skriv inn ditt passord (a-z): ")

password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w', 'x', 'y', 'z',]

password_guess = ""

while (password_guess != user_passord):
    password_guess = ""
    for letter in range(len(user_passord)):
        letter_guess = password[randint(0, 25)]
        password_guess = str(letter_guess) + str(password_guess) 
    print(password_guess)
    print("Knekker passord... Vennligst vent")
    os.system("cls")

print(f"Suksess! Ditt passord er: {password_guess}")