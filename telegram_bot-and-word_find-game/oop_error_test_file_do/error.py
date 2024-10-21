# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
#     print(f"Siz {2021 - yosh} yilda tug'ilgansiz")
# except:
#     print("Siz butun son kiritmadingiz!")

# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
# except:
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2021-yosh} yilda tug'ilgansiz")

# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
# except ValueError:
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2021-yosh} yilda tug'ilgansiz")

"""Yoshingizni kiriting: 50.5
Traceback (most recent call last):
  File "/home/davron/PycharmProjects/oop/error.py", line 2, in <module>
    yosh = int(yosh)
           ^^^^^^^^^
ValueError: invalid literal for int() with base 10: '50.5'"""

# """ZeroDivisionError"""
# x,y=5,10
# try:
#    y/(x-5)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")

# """IndexError"""
#
# mevalar = ['olma','anor','anjir','uzum']
# try:
#     print(mevalar[7])
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")

# """KeyError"""
#
# user = {"username":"sariqdev",
#         "status":"admin",
#         "email":"admin@sariq.dev",
#         "phone":"99897123456"}
#
# key="tel"
# try:
#     print(f'Foydalanuvchi: {user[key]}')
# except KeyError:
#     print("Bunday kalit mavjud emas")

# """FileNotFoundError"""
#
# # filename = "data.txt" # bunday fayl mavjud emas
# # with open(filename) as f:
# #     text = f.read()
#
# filename = "data.txt" # bunday fayl mavjud emas
# try:
#     with open(filename) as f:
#         text = f.read()
# except FileNotFoundError:
#     print(f"Kechirasiz, {filename} fayli mavjud emas. Boshqa fayl tanlang.")

"""BIR NECHTA XATOLARNI USHLASH"""

# n = input("Butun son kiriting: ")
# try:
#     n = int(n)
#     x=20/n
# except ValueError: # agar foydalanuvchi butun son kiritmasa
#     print("Butun son kiritmadingiz")
# except ZeroDivisionError: # agar foydalanuvchi 0 kiritsa
#     print("0 ga bo'lib bo'lmaydi")
# else:
#     print(f"x={x}")

# import json
# files = ['talaba1.json','talaba2.json','talaba3.json','talaba4.json']
# for filename in files:
#     try:
#         with open(filename) as f:
#             talaba = json.load(f)
#     except FileNotFoundError:
#         print(f"{filename} mavjud emas")
#     else:
#         print(talaba['ism'])
#         # fayl ustida turli amallar

# import json
# files = ['talaba1.json','talaba2.json','talaba3.json','talaba4.json']
# for filename in files:
#     try:
#         with open(filename) as f:
#             talaba = json.load(f)
#     except FileNotFoundError:
#         pass #file yo'q deb davom etish
#     else:
#         print(talaba['ism'])

"""XATOLARNING OLDINI OLISH"""

while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():
        yosh = int(yosh)
        break

print(f"Siz {2024-yosh} yilda tug'ilgansiz")