class Student:
    def __init__(self, id_stud, imya, specialnost):
        self.id = id_stud
        self.imya = imya
        self.specialnost = specialnost
        self.semestr = 1
        self.discipliny = {}
        self.fayli_vedomostey = []

class Discipline:
    def __init__(self, nazv, kafedra, specialnost):
        self.nazv = nazv
        self.kafedra = kafedra
        self.specialnost = specialnost

SPECIALNOSTI_SOKR = {
    "пи": "Прикладная информатика",
    "кб": "Кибербезопасность",
    "рф": "Радиофизика и информационные технологии",
    "иэ": "Интеллектуальная электроника",
}

class Facult:
    def __init__(self, nazv):
        self.nazv = nazv
        self.studenty = []
        self.discipliny = []

    def nayti_studenta(self, id_stud):
        for s in self.studenty:
            if s.id == id_stud:
                return s
        return None

    def nayti_disciplinu(self, nazv):
        nazv_lower = nazv.lower()
        for d in self.discipliny:
            if d.nazv.lower() == nazv_lower:
                return d
        return None

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
