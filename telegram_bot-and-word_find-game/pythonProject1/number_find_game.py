from random import randint
q=int(input(") dan to nechchigacha son top o'yini bo'lsin"))
m=randint(0,q)
f=int(input("Men bir son o'yladim toping:"))
count=0
while f!=m:

    if m<f:
        print("O'ylangan son kichik")
    elif m>f:
        print("O'ylangan son katta")
    else:
        print("Siz Javobni topdingiz")
    count+=1
    f = int(input("Men bir son o'yladim toping:"))
print(count)
print("Siz son o'ylang men topaman")

c=0
j="yo'q"
n=randint(0,q)
while j!="ha":
    print(n)
    j=input("To'g'ri bo'lsa 'ha', kichik bo'lsa '+', katta bo'lsa '-' ")
    if j=="+":
        n=randint(n+1,q)
    elif j=="-":
        n=randint(0,n-1)
    c+=1
print(c)

if c==count:
    print(f"Durrang! {c}ta urinishda topildi")
elif c<count:
    print(f"Yutqazdingiz! {c}ta urinishda topdim siz esa {count}ta urinishda topdingiz")
else:
    print(f"Yutdingiz! {c}ta urinishda topdim siz esa {count}ta urinishda topdingiz")