# coding: utf-8

import time
from functions import *

print("*** WELCOME TO OUR PASSWORD GENERATOR ***")

while True:

    #Get user criteria: password length and allowed character types
    password_length = get_password_length()
    user_choices = get_password_criteria()
    
    #Generate password
    for i in range(3):
        print("Generating password...")
        time.sleep(0.5)
        
    characters_range = generate_characters_range(user_choices)
    password = generate_password(password_length, characters_range, user_choices)
    
    #Display password
    print("\nYour password is : {}".format(password))
    
    #Display associated security level
    security_level, guess_time_sec = get_password_strength(password_length,characters_range)
    guess_time = Time(guess_time_sec)
    print("Security level: {}".format(security_level))
    print("A brute-force attack could guess your password in {}.\n".format(guess_time))

    #Save generated password
    while True:
        selection = input("Would you like to save this password? (y/n)")
        if selection.lower() == "y":
            print("Please give us more context about this password:")
            website = input("-Website:")
            username = input("-Username:")
            #Load previous passwords as a dictionnary {website:(username,password)}
            saved_passwords = get_saved_passwords()
            #Add new password to the loaded dictionnary, and rewrite the saved-passwords file accordingly
            save_password(saved_passwords, website, username, password)
            break
        if selection.lower() == "n":
            break
        else:
            print("Please enter 'y' for 'yes', or 'n' for 'no'.")

    #Ask user for next steps: generate a new password, or leave our program
    selection = input("\nWould you like to generate another password? (y/n)")
    if selection.lower() != "y" and selection.lower() != "n":
        print("Please enter 'y' for 'yes', or 'n' for 'no'.")
    elif selection.lower() == "n":
        print("Thank you for using our password generator. See you soon!")
        break
