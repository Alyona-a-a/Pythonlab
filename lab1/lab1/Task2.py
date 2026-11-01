parol = input("Введите пароль: ")
dlina = len(parol)
if dlina < 16:
    print("Слабый пароль!")
else:
    has_letters = any(c.isalpha() for c in parol)
    has_digit = any(c.isdigit() for c in parol)

    if not has_letters:
        print("Слабый пароль, нужны буквы")
    elif not has_digit:
        print("Слабый пароль, нужны цифры")
    else:
        print("Пароль надежный")


