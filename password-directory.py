# coding: utf-8

import os
from functions import get_saved_passwords

print("*** WELCOME TO OUR PASSWORD DIRECTORY ***")

if os.path.exists("saved-passwords")==False:
    print("\nNo passwords have been saved so far. Please use our password generator first.")  
else:
    #Load previous passwords as a dictionnary {website:(username,password)}
    saved_passwords = get_saved_passwords()

    while True:

        #Display the list of available websites
        print("\nList of websites:")
        for key in saved_passwords:
            print("- {}".format(key))

        #Ask user for searched website, and displays associated username and password
        while True:
            website = input("\nPlease enter the website you're looking for:")
            try:
                saved_passwords[website]
            except KeyError:
                print("No password has been saved for {}. Please enter a new one.".format(website))
                continue
            print("- Username:",saved_passwords[website][0])
            print("- Password:",saved_passwords[website][1])
            break

        #Ask user for next steps: search for a new password, or leave our program
        selection = input("\nWould you like to look for another password? (y/n)")
        if selection.lower() != "y" and selection.lower() != "n":
            print("Please enter 'y' for 'yes', or 'n' for 'no'.")
        elif selection.lower() == "n":
            print("Thank you for using our password directory. See you soon!")
            break