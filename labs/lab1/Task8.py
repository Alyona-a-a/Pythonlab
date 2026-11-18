GREEN = "\033[32m"
RESET = "\033[0m"
import random
print("Игра: Угадай число от 1 до 100")
rand = random.randint(1, 100)
chislo = 0  
while chislo != rand:
    chislo = int(input("Введите ваше число: "))
    if chislo > rand:
        print("Ваше число больше")
    elif chislo < rand:
        print("Ваше число меньше")
print(f"{GREEN}Вы угадали!{RESET}")