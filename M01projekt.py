# Napisz dla BBC program sprawdzający złożoność artykułów i wpisów, dzięki czemu pracę dziennikarzy będzie można sparametryzować i automatycznie ustalić, czy piszą teksty proste i łatwe w zrozumieniu. Policz jaka jest średnia długość słów i wyświetl rezultat.


TRESHOLD = 4
CHARS = ',.?!()/'

# def clear_text(text: str) -> str:
#     for char in text: # to jest zbedne
#         if char in CHARS:
#             text = text.replace(char, '')
#     return text
# jeszcze raz ta funkcja:
def clear_text(text: str) -> str:
    for char in CHARS:
        text = text.replace(char, '')
    return text

def check_av_len(text: str) -> float:
    try:
        chars = len(text)
        words = len(text.split())
        average_len = chars/words-1
    except ZeroDivisionError:
        average_len = 0
    return average_len

def check_scientific(average_len: float) -> None:
    if average_len >= 4:
        print(f'this text is scientific. average word length: {average_len}')
    else:
        print(f'this text is not scientific. average word length: {average_len}')

if __name__ == '__main__':

    text = input('podaj text: ')
    text = clear_text(text)
    average_len = check_av_len(text)
    print(average_len)
    check_scientific(average_len)