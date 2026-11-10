class Student:
    def __init__(self, id_stud, imya, specialnost, kurs, semestr):
        self.id = id_stud
        self.imya = imya
        self.specialnost = specialnost
        self.kurs = kurs
        self.semestr = semestr
        self.discipliny = {}
        self.fayli_vedomostey = []

    def dobavit_disciplinu(self, discipline, ocenka=None):
        self.discipliny[discipline] = ocenka

    def ubrat_disciplinu(self, discipline):
        if discipline in self.discipliny:
            del self.discipliny[discipline]

    def poluchit_ocenku(self, discipline):
        return self.discipliny.get(discipline)

    def postaviti_ocenku(self, discipline, ocenka):
        if discipline in self.discipliny:
            self.discipliny[discipline] = ocenka

class Discipline:
    def __init__(self, nazv, kafedra, specialnost, kurs, semestr):
        self.nazv = nazv
        self.kafedra = kafedra
        self.specialnost = specialnost
        self.kurs = kurs
        self.semestr = semestr

    def __str__(self):
        return self.nazv

    def __repr__(self):
        return self.nazv

SPECIALNOSTI_SOKR = {
    "пи": "Прикладная информатика",
    "кб": "Кибербезопасность",
    "рф": "Радиофизика и информационные технологии",
}

BASA_DISCIPLIN = [
    ("Математический анализ", "Кафедра высшей математики и математической физики", "Радиофизика и информационные технологии", 1, 1),
    ("Аналитическая геометрия и линейная алгебра", "Кафедра высшей математики и математической физики", "Радиофизика и информационные технологии", 1, 1),
    ("Программирование на С++", "Кафедра информатики и компьютерных систем", "Радиофизика и информационные технологии", 1, 1),
    
    ("Программирование в С++", "Кафедра информатики и компьютерных систем", "Радиофизика и информационные технологии", 1, 2),
    ("Электричество и магнетизм", "Кафедра физики и аэрокосмических технологий", "Радиофизика и информационные технологии", 1, 2),
    ("Аналитическая геометрия и линейная алгебра", "Кафедра высшей математики и математической физики", "Радиофизика и информационные технологии", 1, 2),
    
    ("Теория вероятностей и математическая статистика", "Кафедра системного анализа и компьютерного моделирования", "Радиофизика и информационные технологии", 2, 1),
    ("Оптика", "Кафедра физики и аэрокосмических технологий", "Радиофизика и информационные технологии", 2, 1),
    ("Дифференнциальные уравнения", "Кафедра высшей математики и математической физики", "Радиофизика и информационные технологии", 2, 1),
    
    ("Философия", "Другой факультет", "Радиофизика и информационные технологии", 2, 2),
    ("Интегральная электроника", "Кафедра интеллектуальных систем", "Радиофизика и информационные технологии", 2, 2),
    ("Базы данных", "Кафедра системного анализа и компьютерного моделирования", "Радиофизика и информационные технологии", 2, 2),
    
    ("Архитектура компьютеров", "Кафедра информатики и компьютерных систем", "Радиофизика и информационные технологии", 3, 1),
    ("Компьютерные сети", "Кафедра телекоммуникаций и информационных технологий", "Радиофизика и информационные технологии", 3, 1),
    ("Термодинамика и статистическая физика", "Кафедра физики и аэрокосмических технологий", "Радиофизика и информационные технологии", 3, 1),
    
    ("Статистическая радиофизика и теория информации", "Кафедра радиофизики и цифровых медиатехнологий", "Радиофизика и информационные технологии", 3, 2),
    ("Основы телеуправления и навигации", "Кафедра физики и аэрокосмических технологий", "Радиофизика и информационные технологии", 3, 2),
    ("Цифровая обработка сигналов и вейвлет-анализ", "Кафедра физики и аэрокосмических технологий", "Радиофизика и информационные технологии", 3, 2),
    
    ("Квантовая радиофизика и оптоэлектроника", "Кафедра квантовой радиофизики и оптоэлектроники", "Радиофизика и информационные технологии", 4, 1),
    ("Статистическая теория радиотехнических систем", "Кафедра физики и аэрокосмических технологий", "Радиофизика и информационные технологии", 4, 1),
    ("Геоинформационные системы и технологии", "Кафедра физики и аэрокосмических технологий", "Радиофизика и информационные технологии", 4, 1),
    
    ("Математический анализ", "Кафедра высшей математики и математической физики", "Прикладная информатика", 1, 1),
    ("Линейная алгебра и аналитическая геометрия", "Кафедра высшей математики и математической физики", "Прикладная информатика", 1, 1),
    ("Основы программирования C++", "Кафедра информатики и компьютерных систем", "Прикладная информатика", 1, 1),
    
    ("Программирование на С++", "Кафедра информатики и компьютерных систем", "Прикладная информатика", 1, 2),
    ("Аналитическая геометрия и линейная алгебра", "Кафедра высшей математики и математической физики", "Прикладная информатика", 1, 2),
    ("Математический анализ(МАК/МАД)", "Кафедра высшей математики и математической физики", "Прикладная информатика", 1, 2),
    
    ("Теория вероятностей и математическая статистика", "Кафедра системного анализа и компьютерного моделирования ", "Прикладная информатика", 2, 1),
    ("Численные методы", "Кафедра информатики и компьютерных систем", "Прикладная информатика", 2, 1),
    ("Оптика", "Кафедра физики и аэрокосмических технологий", "Прикладная информатика", 2, 1),
    
    ("Интегральная электроника", "Кафедра интеллектуальных систем", "Прикладная информатика", 2, 2),
    ("Искусственный интеллект и методы машинного обучения", "Кафедра интеллектуальных систем", "Прикладная информатика", 2, 2),
    ("Архитектура компьютера", "Кафедра информатики и компьютерных систем", "Прикладная информатика", 2, 2),
    
    ("Операционные системы", "Кафедра телекоммуникаций и информационных технологий", "Прикладная информатика", 3, 1),
    ("Термодинамика и статистическая физика", "Кафедра физики и аэрокосмических технологий", "Прикладная информатика", 3, 1),
    ("Технологии программирования", "Кафедра телекоммуникаций и информационных технологий", "Прикладная информатика", 3, 1),
    
    ("Цифровая обработка сигналов", "Кафедра физики и аэрокосмических технологий", "Прикладная информатика", 3, 2),
    ("Безопасность информационных систем", "Кафедра телекоммуникаций и информационных технологий", "Прикладная информатика", 3, 2),
    ("Интеллектуальный анализ данных", "Кафедра системного анализа и компьютерного моделирования", "Прикладная информатика", 3, 2),
    
    ("Анализ биомедицинских изображений", "Кафедра системного анализа и компьютерного моделирования", "Прикладная информатика", 4, 1),
    ("Мультиагентные системы", "Кафедра интеллектуальных систем", "Прикладная информатика", 4, 1),
    ("Анализ больших данных", "Кафедра системного анализа и компьютерного моделирования", "Прикладная информатика", 4, 1),
    
    ("Математический анализ", "Кафедра высшей математики и математической физики", "Кибербезопасность", 1, 1),
    ("Аналитическая геометрия и линейная алгебра", "Кафедра высшей математики и математической физики", "Кибербезопасность", 1, 1),
    ("Программирование на C++", "Кафедра информатики и компьютерных систем", "Кибербезопасность", 1, 1),
    
    ("Электричество и магнетизм", "Кафедра физики и аэрокосмических технологий", "Кибербезопасность", 1, 2),
    ("Алгоритмы и структуры данных", "Кафедра интеллектуальных систем", "Кибербезопасность", 1, 2),
    ("Математический анализ", "Кафедра высшей математики и математической физики", "Кибербезопасность", 1, 2),
    
    ("Дифференциальные уравнения", "Кафедра высшей математики и математической физики", "Кибербезопасность", 2, 1),
    ("Базы данных", "Кафедра системного анализа и компьютерного моделирования", "Кибербезопасность", 2, 1),
    ("Оптика", "Кафедра физики и аэрокосмических технологий", "Кибербезопасность", 2, 1),
    
    ("Архитектура компьютеров", "Кафедра информатики и компьютерных систем", "Кибербезопасность", 2, 2),
    ("Квантовая физика", "Кафедра физики и аэрокосмических технологий", "Кибербезопасность", 2, 2),
    ("Программирование на Java", "Кафедра системного анализа и компьютерного моделирования", "Кибербезопасность", 2, 2),
    
    ("Термодинамика и статистическая физика", "Кафедра физики и аэрокосмических технологий", "Кибербезопасность", 3, 1),
    ("Основы кибербезопасности", "Кафедра телекоммуникаций и информационных технологий", "Кибербезопасность", 3, 1),
    ("Операционные системы", "кафедра телекоммуникаций и информационных технологий", "Кибербезопасность", 3, 1),
    
    ("Прикладная электродинамика", "Кафедра радиофизики и цифровых медиатехнологий", "Кибербезопасность", 3, 2),
    ("Интеллектуальный анализ данных", "Кафедра системного анализа и компьютерного моделирования", "Кибербезопасность", 3, 2),
    ("Методы оптимизации и исследование операций", "Кафедра телекоммуникаций и информационных технологий", "Кибербезопасность", 3, 2),
    
    ("Криптографический инжиниринг", "Кафедра системного анализа и компьютерного моделирования", "Кибербезопасность", 4, 1),
    ("Квантовая радиофизика и оптоэлектроника", "Кафедра квантовой радиофизики и оптоэлектроники", "Кибербезопасность", 4, 1),
    ("Распределённые вычислительные системы и (облачные) технологии", "кафедра телекоммуникаций и информационных технологий", "Кибербезопасность", 4, 1)
]

class Facult:
    def __init__(self, nazv):
        self.nazv = nazv
        self.studenty = []
        self.discipliny = []
        self._zagruzit_discipliny()
    
    def _zagruzit_discipliny(self):
        for nazv, kafedra, specialnost, kurs, semestr in BASA_DISCIPLIN:
            self.discipliny.append(Discipline(nazv, kafedra, specialnost, kurs, semestr))

    def nayti_studenta(self, id_stud):
        for s in self.studenty:
            if s.id == id_stud:
                return s
        return None

    def nayti_disciplinu_po_nazv(self, nazv):
        nazv_lower = nazv.lower()
        for d in self.discipliny:
            if d.nazv.lower() == nazv_lower:
                return d
        return None

    def poluchit_discipliny_dlya_semestra(self, specialnost, kurs, semestr):
        return [d for d in self.discipliny 
                if d.specialnost.lower() == specialnost.lower() and d.kurs == kurs and d.semestr == semestr]

    def poluchit_vse_predyduschie_discipliny(self, specialnost, kurs, semestr):
        result = []
        for d in self.discipliny:
            if d.specialnost.lower() != specialnost.lower():
                continue
            if d.kurs < kurs or (d.kurs == kurs and d.semestr < semestr):
                result.append(d)
        return result

    def opredelit_specialnost(self, specialnost):
        klyuch = specialnost.lower().strip()
        if klyuch in SPECIALNOSTI_SOKR:
            return SPECIALNOSTI_SOKR[klyuch]
        for d in self.discipliny:
            if d.specialnost.lower() == klyuch:
                return d.specialnost
        return None

    def spisok_specialnostey(self):
        return sorted(set(d.specialnost for d in self.discipliny))

    def zachislit(self, id_stud, imya, specialnost, kurs, semestr):
        realnaya_spec = self.opredelit_specialnost(specialnost)
        if not realnaya_spec:
            print(f"Специальность '{specialnost}' не найдена.")
            print("Доступные специальности:")
            for spec in self.spisok_specialnostey():
                print(f"  - {spec}")
            print("Сокращения: ПИ, КБ, РФ")
            return
        if not (1 <= kurs <= 4 and 1 <= semestr <= 2):
            print("Курс должен быть 1-4, семестр 1-2")
            return
        if self.nayti_studenta(id_stud):
            print(f"Студент с ID {id_stud} уже существует")
            return
        
        student = Student(id_stud, imya, realnaya_spec, kurs, semestr)
        
        if kurs > 1 or semestr > 1:
            predyduschie = self.poluchit_vse_predyduschie_discipliny(realnaya_spec, kurs, semestr)
            print(f"\nВнимание! Студент зачисляется на {kurs} курс {semestr} семестр.")
            print(f"Найдено {len(predyduschie)} дисциплин из предыдущих семестров.")
            print("Автоматически проставляем минимальные проходные оценки (4 балла) за предыдущие дисциплины.")
            
            for d in predyduschie:
                student.dobavit_disciplinu(d, 4)
            
            print(f"Проставлено оценок за предыдущие дисциплины: {len(predyduschie)}")
        
        discipliny_semestra = self.poluchit_discipliny_dlya_semestra(realnaya_spec, kurs, semestr)
        for d in discipliny_semestra:
            student.dobavit_disciplinu(d, None)
        
        self.studenty.append(student)
        print(f"\nСтудент {imya} зачислен на {kurs} курс, {semestr} семестр, специальность {realnaya_spec}")
        print(f"Дисциплин текущего семестра: {len(discipliny_semestra)}")
        print(f"Всего дисциплин в списке: {len(student.discipliny)}")

    def otchislit(self, id_stud):
        student = self.nayti_studenta(id_stud)
        if student:
            for filename in student.fayli_vedomostey:
                try:
                    with open(filename, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                    new_lines = []
                    propuskat = False
                    for line in lines:
                        if line.strip() == "":
                            if propuskat:
                                propuskat = False
                                continue
                            if new_lines and new_lines[-1].strip() == "":
                                new_lines.pop()
                            continue
                        if f"Студент: {student.imya}" in line:
                            propuskat = True
                            continue
                        if not propuskat:
                            new_lines.append(line)
                    with open(filename, "w", encoding="utf-8") as f:
                        f.writelines(new_lines)
                    print(f"Запись удалена из файла '{filename}'")
                except FileNotFoundError:
                    pass
            self.studenty.remove(student)
            print(f"Студент {student.imya} (ID: {student.id}) отчислен")
        else:
            print("Студент не найден")
    def dobavit_na_disciplinu(self, id_stud, nazv_disc):
        disc = self.nayti_disciplinu_po_nazv(nazv_disc)
        if not disc:
            print("Дисциплина не найдена")
            return
        student = self.nayti_studenta(id_stud)
        if not student:
            print("Студент не найден")
            return
        if student.specialnost.lower() != disc.specialnost.lower():
            print("Дисциплина не для этой специальности")
            return
        if disc in student.discipliny:
            print("Студент уже записан на эту дисциплину")
        else:
            student.dobavit_disciplinu(disc, None)
            print(f"Студент {student.imya} добавлен на дисциплину {disc.nazv}")

    def ubrat_s_discipliny(self, id_stud, nazv_disc):
        student = self.nayti_studenta(id_stud)
        if not student:
            print("Студент не найден")
            return
        disc = self.nayti_disciplinu_po_nazv(nazv_disc)
        if not disc:
            print("Дисциплина не найдена")
            return
        if disc not in student.discipliny:
            print("Студент не записан на эту дисциплину")
        else:
            student.ubrat_disciplinu(disc)
            print(f"Студент удален с дисциплины {disc.nazv}")

    def postavit_ocenku(self, id_stud, nazv_disc, ocenka):
        if not (1 <= ocenka <= 10):
            print("Некорректная оценка (1-10)")
            return
        student = self.nayti_studenta(id_stud)
        if not student:
            print("Студент не найден")
            return
        disc = self.nayti_disciplinu_po_nazv(nazv_disc)
        if not disc:
            print("Дисциплина не найдена")
            return
        if disc not in student.discipliny:
            print("Студент не записан на эту дисциплину")
        else:
            student.postaviti_ocenku(disc, ocenka)
            print(f"Оценка {ocenka} выставлена студенту {student.imya}")

    def perevesti(self, id_stud):
        student = self.nayti_studenta(id_stud)
        if not student:
            print("Студент не найден")
            return
        for ocenka in student.discipliny.values():
            if ocenka is None or ocenka < 4:
                print("Не все дисциплины сданы успешно (есть несданные или оценка ниже 4)")
                return
        student.semestr += 1
        if student.semestr > 2:
            student.semestr = 1
            student.kurs += 1
        if student.kurs > 4:
            print("Студент уже на последнем курсе и завершил обучение")
            return
        student.discipliny = {}
        discipliny_novogo_semestra = self.poluchit_discipliny_dlya_semestra(student.specialnost, student.kurs, student.semestr)
        for d in discipliny_novogo_semestra:
            student.dobavit_disciplinu(d, None)
        print(f"Студент {student.imya} переведен на {student.kurs} курс, {student.semestr} семестр")
        print(f"Добавлено новых дисциплин: {len(discipliny_novogo_semestra)}")
    def sohranit_vedomost(self, id_stud, filename):
        student = self.nayti_studenta(id_stud)
        if not student:
            print("Студент не найден")
            return
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"Студент: {student.imya}\n")
            f.write(f"Специальность: {student.specialnost}\n")
            f.write(f"Курс: {student.kurs}, Семестр: {student.semestr}\n")
            f.write("Дисциплины:\n")
            summ, count = 0, 0
            for discipline, ocenka in student.discipliny.items():
                kafedra = discipline.kafedra
                ocenka_str = str(ocenka) if ocenka is not None else "не сдана"
                f.write(f"  {discipline.nazv} ({kafedra}): {ocenka_str}\n")
                if ocenka is not None:
                    summ += ocenka
                    count += 1
            if count > 0:
                f.write(f"Средний балл: {summ/count:.2f}\n")
        if filename not in student.fayli_vedomostey:
            student.fayli_vedomostey.append(filename)
        print(f"Ведомость сохранена в {filename}")

facult = Facult("РФиКТ БГУ")
while True:
    print("МЕНЮ УПРАВЛЕНИЯ ФАКУЛЬТЕТОМ")
    print("1. Зачислить студента")
    print("2. Отчислить студента")
    print("3. Добавить студента на дисциплину")
    print("4. Удалить студента с дисциплины")
    print("5. Выставить оценку")
    print("6. Перевести на следующий семестр")
    print("7. Сохранить ведомость в файл")
    print("0. Выход")
    
    choice = input("Выбор: ")
    
    if choice == "0":
        break
    elif choice == "1":
        id_stud = input("ID студента: ")
        imya = input("Имя: ")
        specialnost = input("Специальность (ПИ, КБ, РФ): ")
        try:
            kurs = int(input("Курс (1-4): "))
            semestr = int(input("Семестр (1-2): "))
            facult.zachislit(id_stud, imya, specialnost, kurs, semestr)
        except ValueError:
            print("Ошибка: курс и семестр должны быть целыми числами")
    elif choice == "2":
        id_stud = input("ID студента: ")
        facult.otchislit(id_stud)
    elif choice == "3":
        id_stud = input("ID студента: ")
        nazv_disc = input("Название дисциплины: ")
        facult.dobavit_na_disciplinu(id_stud, nazv_disc)
    elif choice == "4":
        id_stud = input("ID студента: ")
        nazv_disc = input("Название дисциплины: ")
        facult.ubrat_s_discipliny(id_stud, nazv_disc)
    elif choice == "5":
        id_stud = input("ID студента: ")
        nazv_disc = input("Название дисциплины: ")
        try:
            ocenka = int(input("Оценка (1-10): "))
            facult.postavit_ocenku(id_stud, nazv_disc, ocenka)
        except ValueError:
            print("Ошибка: оценка должна быть целым числом")
    elif choice == "6":
        id_stud = input("ID студента: ")
        facult.perevesti(id_stud)
    elif choice == "7":
        id_stud = input("ID студента: ")
        filename = input("Имя файла: ")
        facult.sohranit_vedomost(id_stud, filename)
    else:
        print("Неверный выбор, попробуйте снова.")
   