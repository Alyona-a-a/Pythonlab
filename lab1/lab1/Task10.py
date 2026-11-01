summa = float(input("Введите сумму покупки: "))
age = int(input("Введите возраст: "))
is_birthday = int(input("Сегодня у вас день рождения? (1-да,2-нет): ").strip().lower())
is_vip = int(input("Есть VIP-карта? 1-да,2-нет): ").strip().lower())
if is_vip == 1:
    discount = 15
else:
    if summa > 1000:
        discount = 10
    else:
        discount = 0
if age >= 63:
    discount += 5
if is_birthday == 1:
    discount += 5
if discount > 25:
    discount = 25
final_summa = summa - (summa * discount / 100)
print("Ваша скидка:", discount, "%")
print("Итоговая сумма:", final_summa)