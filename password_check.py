"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    
    length = len(password)
    if (length < MIN_LENGTH):
        print("Password must be atleast {} characters long!".format(MIN_LENGTH))
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if (char.isnumeric()):
            count_digit += 1
        elif (char.islower()):
            count_lower += 1
        elif (char.isupper()):
            count_upper += 1
        elif (char in SPECIAL_CHARACTERS):
            count_special += 1




    if(count_digit < 1 ):
        print("Must have a number in your password!")
        return False
    elif(count_lower < 1):
        print("Must have a lowercase character in your password!")
        return False
    elif(count_upper < 1):
        print("Must have an uppercase character in your password")
        return False

    # and return False if it's zero
    elif (count_special < 1):
        print("Must have a special character in your password")
        return False
    # if we get here (without returning False), then the password must be valid
    else:
        return True


main()