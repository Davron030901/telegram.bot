from math import sqrt

sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
ildizlar = list(map(sqrt,sonlar))
print(ildizlar)
sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati

def daraja2(x):
    """Berilgan sonning kvadratini qaytaruvchi funksiya"""
    return x*x

print(list(map(daraja2,sonlar))) # sonlar ning kvadratini hisoblaymiz