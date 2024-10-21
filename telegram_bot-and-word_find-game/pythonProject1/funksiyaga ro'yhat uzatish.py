def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
# talabalar tenglab qo'ysa xotiradan bir joyni egallaydi ro'yxatidan nusxa olish talabalar[:]
baholar = bahola(talabalar[:])
print(baholar)
print(talabalar)