doxod = int(input("Введите сумму,которую вы получаете: "))
rasxhome = int(input("Введите сумму,которую вы отдаёте за квартиру: "))
rasxeat = int(input("Введите сумму,которую вы отдаёте за питание: "))
rasxtransport = int(input("Введите сумму,которую вы тратите на проезд: "))
rasxrazvl = int(input("Введите сумму,которую вы тратите на развлечения: "))
summa = rasxhome + rasxeat + rasxtransport + rasxrazvl
summa1 = rasxeat + rasxtransport + rasxrazvl
summa2 =  rasxtransport + rasxrazvl

if rasxhome >= summa1:
    print("Оплата жилья самая дорогая,поищите жильё дешевле или зарабатывайте больше!,получайте средний балл выше и степа больше будет")

if rasxeat > summa2:
    print("Молодец,кушать полезно")
else:
    print("Пересмотрите свои расходы на гулянки и проезд")

if doxod < summa:
    print("Вам необходимо уменьшить расходы, так ак дохода меньше")
elif doxod == summa:
    print("Ваш доход равен вашим расходам, но лууучше уменьшить расходы и создать подушку безопасности")
elif doxod < summa:
    print("Ваши доходы превышают рассходы, откладывайте на крупные покупки или в заначку!")