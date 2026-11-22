tip = int(input("1-Длина 2-Ток 3-Давление 4-Время 5-Масса 6-Температура 7-Скорость 8-Объём 9-Энергия 10-Плотность: "))
izm = input("Из какой единицы: ")
nado = input("В какую единицу: ")
val = float(input("Значение: "))
result = None
if tip == 1:
    names, coefs = ["мм", "см", "м", "км"], [0.001, 0.01, 1, 1000]
elif tip == 2:
    names, coefs = ["ма", "а", "ка"], [0.001, 1, 1000]
elif tip == 3:
    names, coefs = ["па", "кпа", "бар", "атм"], [1, 1000, 100000, 101325]
elif tip == 4:
    names, coefs = ["с", "мин", "ч", "сут"], [1, 60, 3600, 86400]
elif tip == 5:
    names, coefs = ["г", "кг", "т"], [0.001, 1, 1000]
elif tip == 7:
    names, coefs = ["м/с", "км/ч", "миль/ч"], [1, 0.277778, 0.44704]
elif tip == 8:
    names, coefs = ["мл", "л", "м3"], [0.000001, 0.001, 1]
elif tip == 9:
    names, coefs = ["дж", "кдж", "кал", "ккал"], [1, 1000, 4.184, 4184]
elif tip == 10:
    names, coefs = ["кг/м3", "г/см3"], [1, 1000]
if tip == 6:
    if izm == "c": c = val
    if izm == "f": c = (val - 32) * 5 / 9
    if izm == "k": c = val - 273
    if nado == "c": result = c
    if nado == "f": result = c * 9 / 5 + 32
    if nado == "k": result = c + 273
elif tip != 6:
    if izm in names and nado in names:
        i_izm = names.index(izm)
        i_nado = names.index(nado)
        result = val * coefs[i_izm] / coefs[i_nado]
if result is not None:
    print("Ответ:", round(result, 4), nado)
else:
    print("Ошибка ввода")