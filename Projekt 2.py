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

lenght_too_short= False
contains_space = False
no_special_char= False
no_lower_char= False
no_upper_char= False

password= input("Podaj hasło: ")
special_char= string.punctuation 

if len(password) < 8:
    lenght_too_short = True
if any(char.isspace() for char in password):
    contains_space = True
if not any(char in special_char for char in password):
    no_special_char= True
if not any(char.islower() for char in password):
    no_lower_char= True
if not any(char.isupper()for char in password):
    no_upper_char= True


if any([lenght_too_short, contains_space, no_special_char, no_lower_char, no_upper_char]) == True:
    print("Twoje hasło nie jest wystarczająco bezpieczne. Dostosuj się do poniższych reguł:")
    if lenght_too_short == True:
        print("Twoje hasło musi składać się z minimum 8 znaków")  
    if contains_space == True:
        print("Twoje hasło nie może zawierać spacji")
    if no_special_char == True:
        print("Twoje hasło musi zawierać znak specjalny")
    if no_lower_char == True:
        print("Twoje hasło musi zawierać małą literę")
    if no_upper_char == True:
        print("Twoje hasło musi zawierać wielką literę")
else:
    print("Twoje hasło jest bezpieczne.") 
