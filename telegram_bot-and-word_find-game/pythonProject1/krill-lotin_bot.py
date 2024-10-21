from translate import to_latin,to_cyrillic

import telebot

TOKEN="7609060500:AAEqc3B3Yjs-QEGhsHU6CwKX6cpHBQSEaVU"
bot =telebot.TeleBot(TOKEN,parse_mode=None)

@bot.message_handler(commands=["start"])
def send_welcome(massage):
    javob="Assalomu alaykum xush kelibsiz! Bu bot gapni Krildan lotinga yoki Lotindan krillga o'tgazuvchi bot."
    javob+="\nMatn kiriting"
    bot.reply_to(massage,javob)
@bot.message_handler(func=lambda massage: True)
def echo_all(massage):
    msg=massage.text
    javob=lambda msg : to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    # if msg.isascii():
    #     javob=to_cyrillic(msg)
    # else:
    #     javob=to_latin(msg)
    bot.reply_to(massage,javob(msg))


bot.polling()

# matn=input("Matn kiriting:")
# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))