# fayl = open('/home/davron/PycharmProjects/oop/pi.txt')
# PI = fayl.read()
# print(PI)
# fayl.close()

# with open('pi.txt') as fayl:
#     pi = fayl.read()
#     print(pi)
# print(type(pi))
# pi = pi.rstrip() # qator ohiridagi bo'shliqlarni olib tashlaymiz
# pi = pi.replace('\n','') # qator tashlash belgisini almashtiramiz
# pi = float(pi) # matnni float (o'nlik) songa o'tkazamiz
# print(pi)
# print(type(pi))
# with open('/home/davron/PycharmProjects/oop/pi.txt') as fayl:
#     pi = fayl.read()

filename = 'talabalar.txt'
ism='Olimjon Hasanov J'
tyil=20044
with open(filename,'a') as file:
    file.write(ism+"\n")
    file.write(str(tyil)+"\n")
    # for line in file:
    #     print(line)