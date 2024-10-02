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
class PasswordCheck:
    def __init__(self, check_method) -> None:
        self.check_method = check_method

    def check_password(self, text) -> bool:
        return any(self.check_method(char) for char in text)
    
    def is_special_char(char: str) -> bool:
        return not char.isalnum()
    # w init jest przekazana metoda sprawdzania, poniewaz to jest glowny cel istnienia tej klasy - przekazanie metody sprawdzenia tekstu

    # w zdefiniowanej funkcji przekazuje tekst do sprawdzenia i okreslam, co ma sie z nim dziac. 
    # wywoluje na nim wybrana metode (self.check_method). 
    # funkcja any() sprawdza czy chociaz jeden z char spełnia warunek metody

    #♻️ okreslam klase ➡️ klasa przyjmuje metode ➡️ przypisuje to do zmiennej z wybraną metodą ➡️ ♻️(teraz wypełnia sie funkcja ponizej, a to przypisanie jest selfem) ➡️ na zmiennej (która zawiera clase z przekazana metodą) wywołuje zdefiniowaną funkcje 'check_password' i przekazuje jej text

    # 💡metoda, którą przekazuje klasie to jest sama nazwa metody, bez nawiasów - one by oznaczały wywołanie. jednoczesnie odnosi sie ona do str a nie do self - bo nie chodzi o metode dot. konkretnej instancji odbieranej przez klase, tylko o metode przypisana do str //self.isupper po prostu nie zadziała//

    # w przypadku password check:
    # tez okreslam clase, która przyjmuje metode, ale teraz metoda to jest klasa, na której wywołuje funkcje 


# tutaj okreslam dokladnie jakie to maja byc metody:
check_upper = PasswordCheck(str.isupper)
check_lower = PasswordCheck(str.islower)
check_special_char = PasswordCheck(PasswordCheck.is_special_char)

#bez nawiasów bo przekazuje metode, a nie wykonuje jej od razu


def check_length_no_spaces(text: str) -> bool:
    text = text.replace(' ', '_')
    num_char = len(text)
    if num_char >= 8:
        safe_len = True
    else: 
        safe_len = False
        # print('Twoje hasło jest za krótkie')
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

    text = input('podaj hasło: ')
    safe_len = check_length_no_spaces(text)
    safe_upper = check_upper.check_password(text)
    safe_lower = check_lower.check_password(text)
    safe_special_char = check_special_char.check_password(text)
    print_raport(safe_len, safe_upper, safe_lower, safe_special_char)



# WYJASNIENIA CHATAGPT:
# 💫
# W konstruktorze __init__ klasy przekazywana jest funkcja check_method, a nie tekst, ponieważ celem klasy PasswordCheck jest umożliwienie elastycznego sprawdzania różnych warunków dotyczących tekstu (np. czy zawiera duże litery, małe litery itd.). Dzięki przekazaniu metody (funkcji) do sprawdzenia, klasa staje się bardziej uniwersalna.
# Zamiast tworzyć osobną funkcję dla każdego przypadku, w konstruktorze możesz podać metodę, która będzie sprawdzać określony warunek, np. str.isupper() dla sprawdzenia wielkich liter lub str.islower() dla małych liter. To eliminuje konieczność pisania kilku prawie identycznych funkcji.

# 💫Dlaczego używamy str.isupper a nie self.isupper?
# Używamy str.isupper dlatego, że isupper to metoda wbudowana w klasę str (string). Ta metoda nie należy do instancji obiektu (np. self w kontekście klasy, którą zdefiniowaliśmy), ale do klasy str. Dlatego przekazujemy funkcję str.isupper, ponieważ chcemy, aby nasza klasa używała tej wbudowanej metody do sprawdzania każdego znaku w stringu.

# Przykład:

# str.isupper: To odniesienie do samej metody. Dzięki temu możemy przekazać ją jako argument i wywołać później, gdy będzie potrzebna. Jest to obiekt metody, który możesz później wywołać.

# self odnosi się do instancji danej klasy, ale w tym przypadku nie potrzebujemy się do niej odwoływać, ponieważ chcemy użyć metody z klasy str, a nie własnej klasy PasswordCheck.

# Dlaczego str.isupper bez nawiasów?
# To kluczowy aspekt. Gdy piszemy str.isupper (bez nawiasów), przekazujemy samą funkcję, jako referencję do metody, bez jej wykonywania. Dzięki temu możemy później wykonać tę funkcję dla każdego znaku tekstu.

# Gdybyśmy napisali str.isupper() (z nawiasami), funkcja zostałaby natychmiast wykonana, ale to nie jest naszym celem. My chcemy przekazać samą metodę jako obiekt, aby później można było ją wywołać na każdym znaku w tekście.

# Jak działa str.isupper?
# str.isupper: To odwołanie do metody, które przekazujemy dalej.
# Później w naszej funkcji check, wywołujemy tę metodę dla każdego znaku, np. self.check_method(char), gdzie self.check_method to właśnie przekazana funkcja str.isupper.
# Dzięki temu wyrażenie any(self.check_method(char) for char in text) sprawdza, czy jakikolwiek znak w text spełnia warunek metody str.isupper (czy jest wielką literą).

# Podsumowanie
# str.isupper: To odniesienie do wbudowanej metody, którą przekazujemy do klasy PasswordCheck.
# Bez nawiasów: Przekazujemy metodę jako obiekt, który możemy później wywołać dla każdego znaku, zamiast natychmiast ją wykonywać.
# Zastosowanie: Używamy str.isupper zamiast str.isupper() ponieważ chcemy operować na metodzie jako obiekcie, a nie wywoływać ją od razu.


##############
# def check_length_no_spaces(text: str) -> bool:
#     text = text.replace(' ', '_')
#     num_char = len(text)
#     if num_char >= 8:
#         safe_len = True
#     else: 
#         safe_len = False
#         # print('Twoje hasło jest za krótkie')
#     return safe_len

# def check_upper(text:str) -> bool:
#     counter = 0
#     for char in text:
#         if char.upper():
#             counter += 1
#     if counter > 0:
#         upper = True
#     else:
#         upper = False
#     return upper

# def check_lower(text: str) -> bool:
#     counter = 0
#     for char in text:
#         if char.lower():
#             counter += 1
#     if counter > 0:
#         lower = True
#     else: 
#         lower = False
#     return lower
# # 💡 mozna to zliczanie zastapic funkcja any() 🔥

# def check_special_char(text: str) -> bool:
#     counter = 0
#     for char in text:
#         if not char.isalnum():
#             counter += 1

#     if counter > 0:
#         special_char = True
#     else: 
#         special_char = False
#     return special_char

# # TRZEBA UZYC KLASY!!

# if __name__ == '__main__':

#     text = input('podaj hasło: ')
#     check_length_no_spaces(text)
#     # safe_upper = PasswordCheck(text, upper)
