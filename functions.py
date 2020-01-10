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

def set_characters_range(user_choices):
    
    """Function returning a list of candidate characters
    for the generate_password function."""
    
    import string
    characters_dict =        {"Lowercase" :[letter for letter in string.ascii_lowercase],         "Uppercase" :[letter for letter in string.ascii_uppercase],         "Numbers":[digit for digit in string.digits],         "Symbols":[punctuation for punctuation in string.punctuation]}
    characters_range = list()
    for key in characters_dict:
        if user_choices[key]==True:
            characters_range+=characters_dict[key]
    return characters_range

def create_choice_item(user_input,type_asked,choices_dict):
    if user_input.lower() == "yes":
        choices_dict[type_asked]=True
    else:
        choices_dict[type_asked]=False

def refine_choice():
    
    choices = dict()
    
    check=False
    
    while check == False:    
        uppercase = input("Would you like to use uppercase letters (ABC...)? Type yes or no")
        if uppercase.lower() != "yes" and uppercase.lower() != "no":
            print("Please use only two words, 'yes' or 'no'. Numbers and\or other words not accepted.")
        else:
            create_choice_item(uppercase,"Uppercase",choices)
            check = True
            
    
    check=False
    
    while check == False:
        lowercase = input("Now, would you like to use lowercase letters (abc...)? Type yes or no")
        if lowercase.lower() != "yes" and lowercase.lower() != "no":
            print("Please use only two words, 'yes' or 'no'. Numbers and\or other words not accepted.")
        else:
            create_choice_item(lowercase,"Lowercase",choices)
            check = True
            
    
    check=False
    
    while check == False:
        numbers = input("Now, would you like to use numbers (123...)? Type yes or no")
        if numbers.lower() != "yes" and numbers.lower() != "no":
            print("Please use only two words, 'yes' or 'no'. Numbers and\or other words not accepted.")
        else:
            create_choice_item(numbers,"Numbers",choices)
            check = True
    
    
    check = False
    
    while check == False:
        symbols = input("Now, would you like to use special symbols (!$#...)? Type yes or no")
        if symbols.lower() != "yes" and symbols.lower() != "no":
            print("Please use only two words, 'yes' or 'no'. Numbers and\or other words not accepted.")
        else:
            create_choice_item(symbols,"Symbols",choices)
            check = True
    
    return choices 

def generate_password(characters_range, password_length):
    
    import random
    
    characters_range=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    final_password = "".join(random.choices(characters_range, k=password_length))
    print(final_password)

"""def check_password(final_password):
    
    for i in final_password:
        
check1 = "1234567890-="
check2 = "qwertyuiop[]"
check3 = "asdfghjkl;'\'"
check4 = "zxcvbnm,./"
"""

