# coding: utf-8

print("***WELCOME TO OUR PASSWORD GENERATOR!***\n")

import time
from functions import *

while True:

    password_length = get_password_length()
    user_choices = get_password_criteria()
    
    for i in range(3):
        print("Generating password...")
        time.sleep(0.5)
        
    characters_range = get_characters_range(user_choices)
    password = generate_password(password_length, characters_range, user_choices)
    
    print("\nYour password is : {}".format(password))
    
    security_level, guess_time_sec = get_password_strength(password_length,characters_range)
    print("Security level: {}".format(security_level))
    print("A brute-force attack could guess your password in {} seconds.\n".format(guess_time_sec))

    user_input = input("Would you like to generate another password? (y/n)")
    if (user_input.lower() != "y") and (user_input.lower() != "n"):
        print("Please enter 'y' for 'yes', or 'n' for 'no'.")
    elif user_input.lower() == "n":
        break

print("Thank you for using our password generator. See you soon!")