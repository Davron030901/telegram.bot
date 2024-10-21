sonlar = list(range(11))

kvadratlar = list(map(lambda x:x*x,sonlar))
print(kvadratlar)

kvadratlar = []
for son in sonlar:
    kvadratlar.append(son*son)

a = [4, 5, 6]
b = [7, 8, 9]
a_plus_b = list(map(lambda x,y:x+y,a,b))
print(a_plus_b)

ismlar = ['hasan','husan','olim','umid']
print(list(map(lambda matn:matn.upper(),ismlar)))