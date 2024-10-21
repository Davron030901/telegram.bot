# x = 10
# print(type(x))
#
# matn = "salom"
# print(type(matn))
#
# def salom_ber():
#     print("Assalom alaykum")
#
# print(type(salom_ber))

class Talaba:
    """Talaba nomli klass yaratamiz"""

    def __init__(self, ism, familiya, tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1

    def set_bosqich(self, bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = bosqich

    def update_bosqich(self):
        """Talabanining bosqichini 1taga ko'paytirish"""
        self.bosqich += 1

    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "

    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism

    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya

    def get_fullname(self):
        """Talabaning ism-familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"

    def get_age(self, yil):
        """Talabaning yoshini qaytaradi"""
        return yil - self.tyil


class Fan():
    """Fan nomli klass"""

    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_student(self, talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_name(self):
        """Fan nomi"""
        return self.nomi

    def get_students(self):
        """Fanga yozilgan talabalar haqida ma'lumot"""
        return [x.get_info() for x in self.talabalar]

    def get_students_num(self):
        """Fanga yozilgan talabalar soni"""
        return self.talabalar_soni
matematika = Fan("Oliy Matematika")
talaba1 = Talaba("Alijon","Valiyev",2000)
talaba2 = Talaba("Hasan","Alimov",2001)
talaba3 = Talaba("Akrom","Boriyev",2001)

matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)

print(matematika.talabalar_soni)
print(matematika.get_students())

# print(talaba1.ism)
# print(talaba1.familiya)
# talaba2 = Talaba("Olim","Olimov",1995)
# talaba3 = Talaba("Husan","Akbarov",2004)
# talaba4 = Talaba("Hasan","Akbarov",2004)
# print(talaba2.ism)
# print(talaba4.familiya)
# talaba1 = Talaba("Alijon","Valiyev",2000)
# print(talaba1.get_age(2021))
# talaba1 = Talaba("Alijon","Valiyev",2000)
# print(talaba1.get_fullname())
#
# talaba1 = Talaba("Alijon","Valiyev",2000)
# talaba1.set_bosqich(3)
# print(talaba1.get_info())
#
# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# print(talaba1.get_info())

m=dir(Talaba)
print(m)
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

print(see_methods(Talaba))
print(talaba1.__dict__)
print(see_methods(talaba1))