minutes_tr = 60
sms_soo = 30
internet_tr = 1024
minutes = int(input("Введите количество минут: "))
sms = int(input("Введите количество смс сообщений: "))
internet = int(input("Введите количество интернета: "))
if minutes > minutes_tr:
    minut = (minutes - minutes_tr) * 0.89
else:
    minut = 0
if sms > sms_soo:
    soo = (sms - sms_soo) * 0.59
else:
    soo = 0
if internet > internet_tr:
    inter = (internet - internet_tr) * 0.79
else:
    inter = 0
summa = 24.99 + minut + soo + inter
nalog = summa * 0.02
itogo = summa + nalog
print("Сумма тарифа основная: 24.99")
if minut > 0:
    print("Сумма за доп. минуты: ", round(minut, 2))
if soo > 0:
    print("Сумма за доп. сообщения: ", round(soo, 2))   
if inter > 0:
    print("Сумма за доп. интернет: ", round(inter, 2))
print("Налог (2%): ", round(nalog, 2))
print("Итоговая сумма: ",f"{itogo:.2f}")