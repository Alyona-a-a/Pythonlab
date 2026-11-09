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

BASA_DISCIPLIN = []

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
                        if line.strip().startswith("=" * 20):
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

   