# coding: utf-8

def get_password_length():
    
    """Function asking the user to input the desired password length."""
    
    while True:
        password_length = input("\nStep 1 - Please enter the desired password length (from 1 to 20):")
        try:
            password_length = int(password_length)
        except:
            print("Your input should be an integer.\n")
            continue
        if password_length<=0 or password_length>20:
            print("Your input should be an integer between 1 and 20 (included).\n") 
            continue
        else:
            break
    return password_length
   
def get_password_criteria():
    
    """Function collecting user password criteria."""
    
    user_choices = dict()
    type_list = ["Uppercase","Lowercase","Numbers","Symbols"]
    print("Step 2 - Please select password character types:")
    for asked_type in type_list:
        while True:
            chosen_type = input("- {} (y/n):".format(asked_type))
            if (chosen_type.lower() != "y") and (chosen_type.lower() != "n"):
                print("Please enter 'y' for 'yes', or 'n' for 'no'.")
            elif chosen_type.lower() == "y":
                user_choices[asked_type]=True
                break
            else:
                user_choices[asked_type]=False
                break
    return user_choices

def get_characters_range(user_choices):
    
    """Function generating the characters range from which the password will be drawn."""
    
    import string

    characters_dict =\
        {"Lowercase" :[letter for letter in string.ascii_lowercase],\
        "Uppercase" :[letter for letter in string.ascii_uppercase],\
        "Numbers":[digit for digit in string.digits],\
        "Symbols":[punctuation for punctuation in string.punctuation]}
    characters_range = list()
    for key in characters_dict:
        if user_choices[key]==True:
            characters_range+=characters_dict[key]
    return characters_range

def generate_password(password_length, characters_range, user_choices):
    
    """Function generating a random password based on the criteria selected by the user."""
    
    import string
    import secrets

    while True:
        password = "".join(secrets.choice(characters_range) for i in range(password_length))
        #The secrets module is used for generating cryptographically strong random numbers.
        if sum(character.isupper() for character in password) >= user_choices["Uppercase"]\
            and sum(character.islower() for character in password) >= user_choices["Lowercase"]\
            and sum(character.isdigit() for character in password) >= user_choices["Numbers"]\
            and sum(character in string.punctuation for character in password) >= user_choices["Symbols"]:
            break
    return password

def get_password_strength(password_length,characters_range):
    
    """Function calculating password strength from the password length and the selected characters range."""
    
    from math import log
    
    max_attempts = len(characters_range)**password_length
    
    #Identify security level
    entropy = log(max_attempts,2)
    
    if entropy < 50:
        security_level = "VERY WEAK"
    elif entropy < 60:
        security_level = "WEAK"
    elif entropy < 70:
        security_level = "FAIR"
    elif entropy < 80:
        security_level = "STRONG"
    else:
        security_level = "VERY STRONG"
    
    #Identify the average time needed to guess the password
    attempts_per_sec = 10**10
    guess_time_sec = max_attempts/(attempts_per_sec*2)

    return security_level, guess_time_sec

def get_saved_passwords():

    """Function returning the dictionnary of previously saved passwords."""

    import os
    import pickle

    if os.path.exists("saved-passwords"):
        with open("saved-passwords","rb") as file:
            saved_passwords = pickle.Unpickler(file).load()
    else:
            saved_passwords = dict()
    return saved_passwords

def save_password(saved_passwords, website, username, password):

    """Function saving passwords in a "saved-passwords" file
    under the follwoing dictionary format : {website: (username,password)}."""

    import pickle

    saved_passwords[website] = (username, password)
    with open("saved-passwords","wb") as file:
        pickle.Pickler(file).dump(saved_passwords)