while True:
    vozrast = int(input("Введите ваш возраст (0 для выхода): "))
    if vozrast == 0:
        break
    doxod = float(input("Введите ваш ежемесячный доход: "))
    kredit = float(input("Какую сумму кредита хотите взять: "))
    srok = int(input("На какой срок хотите оформить кредит (месяцы): "))
    history = int(input("Кредитная история (1-отличная, 2-хорошая, 3-удовлетворительная, 4-плохая): "))
    poruch = int(input("Есть ли поручители? (1-да, 2-нет): "))
    zalog = int(input("Есть ли залог? (1-да, 2-нет): "))
    platezh = kredit / srok
    ratio = platezh / doxod
    risks = {"Низкий": "Шанс одобрения большой", "Средний": "Шанс средний", "Высокий": "Шанс низкий", "Критический": "Шанс очень низкий"}
    if ratio < 0.3:
        risk = "Низкий"
    elif ratio < 0.5:
        risk = "Средний"
    elif ratio < 0.7:
        risk = "Высокий"
    else:
        risk = "Критический"
    print(risks[risk])
    stavka = 20
    odobrenie = "Одобрено"
    if history == 4:
        stavka += 5
        odobrenie = "Отклонено"
    elif history == 3:
        stavka += 3
    if poruch == 1:
        stavka -= 2
    if zalog == 1:
        stavka -= 3
    if vozrast < 21 or vozrast > 65:
        odobrenie = "Отклонено"
    print("Категория риска:", risk)
    print("Итоговая ставка:", stavka, "%")
    print("Решение банка:", odobrenie)