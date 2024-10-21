def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi

print(summa(1,2,3))

print(summa(1,2,3,4,6))
print(summa(23,45,76,345,65,3))
def summa(x,y,*sonlar):
    return x+y+sum(sonlar)
# summa ichida typle 2 tadan kam qiymat bo'lmasligi kerak **kwargs keywords

print(summa(1,2,3,4,6))
print(summa(23,45,76,345,65,3))


def avto_info(kompaniya,model,**malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar
avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000)
print(avto1)
print(avto2)