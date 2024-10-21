from random import randint
def sontop(x=10):
    tas_son=randint(1,x)
    print(f"Men 1 dan {x}gacha son o'yladim, toping")
    taxmin=0
    while True:
        taxmin+=1
        tax=int(input(">>>"))
        if tax<tas_son:
            print("Xato,Yana harakat qiling, bu sondan kattaroq")
        elif tax>tas_son:
            print("Xato,Yana harakat qiling, bu sondan kichikroq")
        else:
            break
    print(f"Tabriklayman ,{taxmin}ta urunishda Topdingiz!")
    return taxmin

def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan sonni toping.")
    quyi=1
    yuqori=x
    taxminlar=0
    while True:
        taxminlar+=1
        if quyi !=yuqori:
            t=randint(quyi,yuqori)
        else:
            t=quyi
        javob =input(f"Siz {t} sonni o'yladim :to'g'ri (t), o'ylagan sonimdan kichik bo'lsa (+), yoki kattaroq (-)".lower())

        if javob=="-":
            yuqori=t-1
        elif javob=="+":
            quyi=t+1
        else :
            break

    print("Topdim!")
    return taxminlar
def play(x=10):
    yana=True
    while yana!=0:
        tax_user=sontop(x)
        tax_pc=sontop_pc(x)
        if tax_pc<tax_user:
            print("Men yutdim")
        elif tax_user<tax_pc:
            print("Siz yuttingiz")
        else:
            print("Durrang")

        yana=int(input("Yana davom etasizmi, Ha(1), Yo'q (0)"))
play(20)