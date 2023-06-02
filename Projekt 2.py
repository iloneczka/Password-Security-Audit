# Jesteś konsultantem działającym dla Niebezpiecznika - polskiego lidera cyberbezpieczeństwa. Napisz program, który będzie dokonywał audytu bezpieczeństwa u klientów Niebezpiecznika - jesteś odpowiedzialny za moduł sprawdzający złożoność haseł i generujący raport z rekomendacjami. 
#
# 1. Poproś użytkownika o hasło, a następnie sprawdź, czy spełnia ono reguły bezpieczeństwa.
# 2. Hasło powinno mieć minimum jedną małą literę, jedną wielką literę i jeden znak specjalny.
# 3. Hasło nie może zawierać spacji!  (wewnętrzny wymóg klienta wynikający z ograniczeń ich systemu teleinformatycznego)
# 4. Hasło musi mieć minimum 8 znaków.
# 5. Jeśli hasło jest niepoprawne, wyświetl raport w punktach co należy zmienić.

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
