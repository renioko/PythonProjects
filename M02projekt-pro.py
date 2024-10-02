# Jesteś konsultantem działającym dla Niebezpiecznika - polskiego lidera cyberbezpieczeństwa. Napisz program, który będzie dokonywał audytu bezpieczeństwa u klientów Niebezpiecznika - jesteś odpowiedzialny za moduł sprawdzający złożoność haseł i generujący raport z rekomendacjami. 
#
# 1. Poproś użytkownika o hasło, a następnie sprawdź, czy spełnia ono reguły bezpieczeństwa.
# 2. Hasło powinno mieć minimum jedną małą literę, jedną wielką literę i jeden znak specjalny.
# 3. Hasło nie może zawierać spacji!  (wewnętrzny wymóg klienta wynikający z ograniczeń ich systemu teleinformatycznego)
# 4. Hasło musi mieć minimum 8 znaków.
# 5. Jeśli hasło jest niepoprawne, wyświetl raport w punktach co należy zmienić.

class PasswordCheck:
    def __init__(self, check_method) -> None:
        self.check_method = check_method

    def check_password(self, text) -> bool:
        return any(self.check_method(char) for char in text)
    
    @staticmethod
    def is_special_char(char: str) -> bool:
        return not char.isalnum()
    

def check_length_no_spaces(text: str) -> bool:
    text = text.replace(' ', '_')
    num_char = len(text)
    if num_char >= 8:
        safe_len = True
    else: 
        safe_len = False
    return safe_len

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

# Inicjalizacja obiektów w głównym bloku programu
    check_upper = PasswordCheck(str.isupper)
    check_lower = PasswordCheck(str.islower)
    check_special_char = PasswordCheck(PasswordCheck.is_special_char)

# Główna logika programu
    text = input('podaj hasło: ')
    safe_len = check_length_no_spaces(text)
    safe_upper = check_upper.check_password(text)
    safe_lower = check_lower.check_password(text)
    safe_special_char = check_special_char.check_password(text)

# wyświetlanie raportu
    print_raport(safe_len, safe_upper, safe_lower, safe_special_char)