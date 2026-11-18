stroka1 = input("Введите первый набор чисел через пробел: ")
parts1 = stroka1.split()
set1 = []
for p in parts1:
    if "." in p:
        set1.append(float(p))
    else:
        set1.append(int(p))
set1 = set(set1)

stroka2 = input("Введите второй набор чисел через пробел: ")
parts2 = stroka2.split()
set2 = []
for p in parts2:
    if "." in p:
        set2.append(float(p))
    else:
        set2.append(int(p))
set2 = set(set2)

print("Первый набор:", set1)
print("Второй набор:", set2)

both = set1.intersection(set2)
print("1. В обоих наборах:", both)

only_first = set1.difference(set2)
only_second = set2.difference(set1)
print("2. Только в первом:", only_first)
print("   Только во втором:", only_second)

exclude_both = set1.symmetric_difference(set2)
print("3. Все, кроме общих:", exclude_both)