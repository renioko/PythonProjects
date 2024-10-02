# Jesteś konsultantem działającym dla Niebezpiecznika - polskiego lidera cyberbezpieczeństwa. Napisz program, który będzie dokonywał audytu bezpieczeństwa u klientów Niebezpiecznika - jesteś odpowiedzialny za moduł sprawdzający złożoność haseł i generujący raport z rekomendacjami. 
#
# 1. Poproś użytkownika o hasło, a następnie sprawdź, czy spełnia ono reguły bezpieczeństwa.
# 2. Hasło powinno mieć minimum jedną małą literę, jedną wielką literę i jeden znak specjalny.
# 3. Hasło nie może zawierać spacji!  (wewnętrzny wymóg klienta wynikający z ograniczeń ich systemu teleinformatycznego)
# 4. Hasło musi mieć minimum 8 znaków.
# 5. Jeśli hasło jest niepoprawne, wyświetl raport w punktach co należy zmienić.

# Hinty

# Używaj operatorów and oraz or do tworzenia bardziej złożonych warunków.
# counter = 0
# text = "ile liter lub cyfr ma ten napis? 1234"
# for char in text:
#     if char.isalpha() or char.isdigit():
#         counter = counter + 1
# print("Ten tekst ma", len(text), "znaków, w tym", counter, "liter i cyfr.")

# # Możesz także negować przy pomocy not.
# text = "ASdf"
# if not text.islower():
#     print("Nie wszystkie litery są małe!")
    
# # Możesz łączyć not, or oraz and:
# if text.isalpha() and not text.islower():
#     print("Same litery i co najmniej jedna wielka litera.")
    
# Do porównania typu "większy lub równy" służy >=
# x = 5
# print(x >= 5)  # ==> True

# TRZEBA UZYC KLASY!!


##############
def check_length_no_spaces(text: str) -> bool:
    text = text.replace(' ', '_')
    num_char = len(text)
    if num_char >= 8:
        safe_len = True
    else: 
        safe_len = False
        # print('Twoje hasło jest za krótkie')
    return safe_len

def check_upper(text:str) -> bool:
    counter = 0
    for char in text:
        if char.isupper():
            counter += 1
    if counter > 0:
        upper = True
    else:
        upper = False
    return upper

def check_lower(text: str) -> bool:
    counter = 0
    for char in text:
        if char.islower():
            counter += 1
    if counter > 0:
        lower = True
    else: 
        lower = False
    return lower

def check_special_char(text: str) -> bool:
    counter = 0
    for char in text:
        if not char.isalnum():
            counter += 1

    if counter > 0:
        special_char = True
    else: 
        special_char = False
    return special_char

# TRZEBA UZYC KLASY!!

def print_raport(safe_len, safe_upper, safe_lower, safe_special_char):
    if not safe_len:
        print('twoje hasło jest za krótkie')
    if not safe_lower:
        print('hasło musi zawierać małą literę')
    if not safe_upper:
        print('hasło musi zawierac wielką literę')
    if not safe_special_char:
        print('hasło musi zawierać znak specjalny')
    else:
        print('twoje hasło jest bezpieczne')

if __name__ == '__main__':

    text = input('podaj hasło: ')
    safe_len = check_length_no_spaces(text)
    safe_lower = check_lower(text)
    safe_upper = check_upper(text)
    safe_special_char = check_special_char(text)
    print_raport(safe_len, safe_upper, safe_lower, safe_special_char)



