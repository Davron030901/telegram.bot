from uzword import words
from random import choice
def get_word():
    word=choice(words)
    while "-" in word or " " in word:
        word=choice(words)
    return word.upper()

def display(user_letters,word):
    display_letter=""
    for letter in word:
        if letter in user_letters.upper():
            display_letter +=letter
        else:
            display_letter+="-"
    return display_letter

def play():
    word=get_word()
    # so'zdagi harflar
    word_letter=set(word)
    # foydalanuvchi kiritgan harflat
    user_letters=''
    print(f"Men {len(word)} xonali son o'yladim")
    # print(word)
    while len(word_letter)>0:
        print(display(user_letters,word))
        if len(user_letters)>0:
            print(f"Shu harfni avval kiritgansiz!")
        letter =input("harflarni kiriting:").upper()

        if letter in user_letters:
            print("Bu harf kiritilgan:")
            continue
        elif letter in word:
            word_letter.remove(letter)
            print(f"{letter} harifi to'g'ri")
        else:
            print("Bu harf yo'q")
        user_letters+=letter
    print(f"Tabriklayman ! {word} so'zini {len(user_letters)} ta urinishda topdingiz.")
