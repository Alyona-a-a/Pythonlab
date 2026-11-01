price = int(input("Введите сумму в рублях (целое число): "))
count100 = price // 100
price = price % 100
count50 = price // 50
price = price % 50
count10 = price // 10
price = price % 10
count5 = price // 5
price = price % 5
count2 = price // 2
price = price % 2
count1 = price 

print(f"{count100}")
print(f"{count50}")
print(f"{count10}")
print(f"{count5}")
print(f"{count2}")
print(f"{count1}")