stroka = input("Введите строку: ")
print("Перевёртыш: ",stroka[::-1])
stroka = stroka.lower().replace(" ", "")
if stroka == stroka[::-1]:
    print("Палиндром!")
else:
    print("Не палиндром")