produkts = [
    {"name": "Хлеб", "price": 5.0, "prodano": 14},
    {"name": "Масло", "price": 4.0, "prodano": 7},
    {"name": "Чай", "price": 4.50, "prodano": 5}
]

print("Выручка по каждому товару:")
for produkt in produkts:
    summa = produkt['price'] * produkt['prodano']
    print(produkt['name'], ":", summa)

maxsumma = 0
best_product = ""

for produkt in produkts:
    summa = produkt['price'] * produkt['prodano']
    if summa > maxsumma:
        maxsumma = summa
        best_product = produkt['name']

print("Самый прибыльный товар:", best_product, "Общая сумма:", maxsumma)

unique_names = set()
for produkt in produkts:
    unique_names.add(produkt['name'])
print("Количество уникальных наименований:", len(unique_names))