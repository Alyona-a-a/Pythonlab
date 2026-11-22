import numpy as np

np.random.seed(42)

students = [
    "Иванов", "Петров", "Сидорова", "Смирнова", "Кузнецов",
    "Попов", "Васильева", "Соколов", "Михайлова", "Новиков",
    "Фёдорова", "Морозов", "Волкова", "Алексеев", "Лебедева",
    "Семёнов", "Егорова", "Павлов", "Козлова", "Степанов",
    "Николаева", "Орлова"
]
subjects = ["Математический анализ", "Оптика", "Программирование на Python", "Базы данных", "Английский"]

grades = np.random.randint(1, 11, size=(22, 5))

avg_students = grades.mean(axis=1)
avg_subjects = grades.mean(axis=0)

best_val = avg_students.max()
worst_val = avg_students.min()

easy_idx = avg_subjects.argmax()
hard_idx = avg_subjects.argmin()

scholarships = []
for i in range(22):
    score = avg_students[i]
    if score < 4.0:
        pay = 0.0
    elif score < 5.0:
        pay = 240.0
    elif score < 6.0:
        pay = 290.0
    elif score < 8.0:
        pay = 310.0
    else:
        pay = 350.0
    scholarships.append(pay)

total_pay = sum(scholarships)

out = []
out.append("СРЕДНИЙ БАЛЛ СТУДЕНТОВ")
for i in range(22):
    out.append(f"{students[i]}: {avg_students[i]:.2f}, стипендия: {scholarships[i]:.2f} BYN")

out.append("")
out.append(f"Итого на стипендии: {total_pay:.2f} BYN")

out.append("")
out.append(f"Лучший средний балл: {best_val:.2f}")
for i in range(22):
    if avg_students[i] == best_val:
        out.append("  лучший: " + students[i])

out.append(f"Худший средний балл: {worst_val:.2f}")
for i in range(22):
    if avg_students[i] == worst_val:
        out.append("  худший: " + students[i])

out.append("")
out.append("СРЕДНИЙ БАЛЛ ПО ПРЕДМЕТАМ")
for j in range(5):
    out.append(f"{subjects[j]}: {avg_subjects[j]:.2f}")

out.append("")
out.append(f"Самый простой предмет: {subjects[easy_idx]} ({avg_subjects[easy_idx]:.2f})")
out.append(f"Самый сложный предмет: {subjects[hard_idx]} ({avg_subjects[hard_idx]:.2f})")

text = "\n".join(out)
print(text)

with open("grades_report.txt", "w", encoding="utf-8") as f:
    f.write(text)