class Avto:
    __num_avto = 0
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narh):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1

    def __repr__(self):
        """Obyekt haqida ma'lumot"""
        return f"Avto: {self.rang} {self.make} {self.model}"
    # hammasi bilan
    def __str__(self):
        """Obyekt haqida ma'lumot"""
        return f"Avto: {self.rang} {self.make} {self.model}"
    # satr va prin bilan
    def __eq__(self, boshqa_avto):
        """Tenglik"""
        return self.narh == boshqa_avto.narh

    def __lt__(self, boshqa_avto):
        """Kichik"""
        return self.narh < boshqa_avto.narh

    def __le__(self, boshqa_avto):
        """Kichik yoki teng"""
        return self.narh <= boshqa_avto.narh


class AvtoSalon:
    """Avtosalon klassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f"{self.name} avtosaloni"

    def __getitem__(self, index):
        return self.avtolar[index]
    def __setitem__(self, index,qiymat):
        self.avtolar[index]=qiymat
    def __len__(self):
        return len(self.avtolar)
    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto,Avto):
                self.avtolar.append(avto)
            else:
                print("Avto kiriting")

salon1 = AvtoSalon("MaxAvto")
print(salon1)

print(dir(Avto))
avto1 = Avto("GM","Malibu","Qora",2020,40000)
print(avto1) # obyekt haqida ma'lumot

avto1 = Avto("GM","Malibu","Qora",2020,40000)
print(avto1)

avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
print(avto1<avto2)

avto3 = Avto("Honda","Accord","Oq",2017,40000)
print(avto1==avto3)
salon1.add_avto(avto1,avto3,avto2)

print(salon1[:])
# ['_Avto__num_avto',
#  '__class__',
#  '__delattr__',
#  '__dict__',
#  '__dir__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__gt__',
#  '__hash__',
#  '__init__',
#  '__init_subclass__',
#  '__le__',
#  '__lt__',
#  '__module__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__setattr__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  '__weakref__']