stroka = input("Введите числа через пробел: ")
parts = stroka.split()

numbers = []
for p in parts:
    if "." in p:
        numbers.append(float(p))
    else:
        numbers.append(int(p))

print("Ваш список чисел:", numbers)

unique = []
repeat = []

for num in numbers:
    if numbers.count(num) == 1 and num not in unique:
        unique.append(num)
    elif numbers.count(num) > 1 and num not in repeat:
        repeat.append(num)

print("Уникальные:", unique)
print("Повторяющиеся:", repeat)

chetn = []
nechetn = []

for num in numbers:
    if num % 2 == 0:
        chetn.append(num)
    else:
        nechetn.append(num)

print("Четные:", chetn)
print("Нечетные:", nechetn)

otric = []
for num in numbers:
    if num < 0:
        otric.append(num)
print("Отрицательные:", otric)

floats = []
for num in numbers:
    if type(num) == float:
        floats.append(num)
print("С точкой:", floats)

sum_5 = 0
for num in numbers:
    if num % 5 == 0:
        sum_5 += num
print("Сумма кратных 5:", sum_5)

maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print("Самое большое:", maximum)
print("Самое маленькое:", minimum)