"""
Program for password security audit and generating recommendation reports.

Module for security audit designed for clients of Niebezpiecznik, a Polish leader in cybersecurity.
Password complexity requirements:
1. The password must contain at least one lowercase letter, one uppercase letter, and one special character.
2. The password cannot contain spaces.
3. The password must have a minimum length of 8 characters.

Usage instructions:
1. Run the program.
2. Provide the password you want to check.
3. The program will verify if the password meets the security requirements.
4. If the password is incorrect, a recommendation report will be generated.
5. If the password is secure, a confirmation message will be displayed.

"""

import string

def is_password_secure(password: str) -> bool:
    """
    Check if the given password meets the security requirements.

    Args:
        password (str): The password to be checked.

    Returns:
        bool: True if the password is secure, False otherwise.
    """
    length_too_short = len(password) < 8
    contains_space = any(char.isspace() for char in password)
    special_char = set(string.punctuation)
    no_special_char = not any(char in special_char for char in password)
    no_lower_char = not any(char.islower() for char in password)
    no_upper_char = not any(char.isupper() for char in password)

    return not any([length_too_short, contains_space, no_special_char, no_lower_char, no_upper_char])

def main():
    """
    Main function for password security audit and generating recommendation reports.
    """
    password = input("Enter your password: ")

    if is_password_secure(password):
        print("Your password is secure.")
    else:
        print("Your password is not secure. Please follow the rules below:")
        if len(password) < 8:
            print("Your password must have a minimum length of 8 characters.")
        if any(char.isspace() for char in password):
            print("Your password cannot contain spaces.")
        special_char = set(string.punctuation)
        if not any(char in special_char for char in password):
            print("Your password must contain at least one special character.")
        if not any(char.islower() for char in password):
            print("Your password must contain at least one lowercase letter.")
        if not any(char.isupper() for char in password):
            print("Your password must contain at least one uppercase letter.")

if __name__ == "__main__":
    main()
