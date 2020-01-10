# coding: utf-8

def get_password_length():
    
    """Function asking the user to input the desired password length."""
    
    check = False
    while check == False:
        password_length = input("Please enter the desired password length (from 1 to 20):")
        try:
            password_length = int(password_length)
        except:
            print("Your input should be an integer.\n")
            continue
        if password_length<=0 or password_length>20:
            print("Your input should be an integer between 1 and 20 (included).\n") 
            continue
        check = True        
    return password_length
   

def get_password_criteria():
    
    """Function collecting user password criteria."""
    
    user_choices = dict()
    type_list = ["Uppercase","Lowercase","Numbers","Symbols"]
    print("Please select password character types:")
    for asked_type in type_list:
        check = False
        while check == False:
            chosen_type = input("- {} (y/n):".format(asked_type))
            if (chosen_type.lower() != "y") and (chosen_type.lower() != "n"):
                print("Please enter 'y' for 'yes', or 'n' for 'no'.")
            elif chosen_type.lower() == "y":
                user_choices[asked_type]=True
                check = True
            else:
                user_choices[asked_type]=False
                check = True
    return user_choices


def get_security_level(password_length,user_choices):
    
    """Function calculating the security level (WEAK, AVERAGE or STRONG)
    from the password length and selected character types."""
    
    total_score = password_length*sum(list(user_choices.values()))
    if total_score < 30:
        security_level = "WEAK"
    elif total_score < 40:
        security_level = "AVERAGE"
    else:
        security_level = "STRONG"
    return security_level


def generate_password(password_length, user_choices):
    
    """Function generating a random password based on the criteria selected by the user."""
    
    import string
    import random
    
    #Generating the characters range from which the password will be drawn
    characters_dict =\
    {"Lowercase" :[letter for letter in string.ascii_lowercase],\
     "Uppercase" :[letter for letter in string.ascii_uppercase],\
     "Numbers":[digit for digit in string.digits],\
     "Symbols":[punctuation for punctuation in string.punctuation]}
    characters_range = list()
    for key in characters_dict:
        if user_choices[key]==True:
            characters_range+=characters_dict[key]
    
    #Generating random password
    password = "".join(random.choices(characters_range, k=password_length))
    
    return password
