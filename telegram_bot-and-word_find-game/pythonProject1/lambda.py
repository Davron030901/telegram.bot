import math
uzunlik = lambda pi, r : 2*pi*r
print(uzunlik(math.pi,10))

product = lambda x, y : x ** y
print(product(3, 2))

def daraja(n):
    return lambda x : x**n

kvadrat = daraja(2)
kub = daraja(3)
print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")