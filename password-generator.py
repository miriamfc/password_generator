# coding: utf-8

print("***WELCOME TO OUR PASSWORD GENERATOR!***\n")

import time
continue_generator = True

while continue_generator == True:

    password_length = get_password_length()
    user_choices = get_password_criteria()

    print("Given the chosen criteria, the security level of your password will be: {}\n"\
          .format(get_security_level(password_length,user_choices)))
    
    for i in range(3):
        time.sleep(1)
        print("Generating password...")
    
    password = generate_password(password_length, user_choices)
    print("\nYour password is : {}".format(password))

    user_input = input("Would you like to generate another password? (y/n)")
    if (user_input.lower() != "y") and (user_input.lower() != "n"):
        print("Please enter 'y' for 'yes', or 'n' for 'no'.")
    elif user_input.lower() == "n":
        continue_generator = False

print("Thank you for using our password generator. See you soon!")
