from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# /start komandasini ishlovchi funksiya
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Salom! Kod generatsiya qilish uchun /generate buyrug\'ini yuboring.')

# /generate komandasini ishlovchi funksiya
def generate(update: Update, context: CallbackContext) -> None:
    # Tasodifiy kod generatsiya qilish
    import random
    import string
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    update.message.reply_text(f'Sizning generatsiya qilingan kodingiz: {code}')

def main():
    # Telegram bot tokeningizni kiriting
    updater = Updater("7208041122:AAHKOUYfR-kDmYAaYcusghikHBKPNWWisbU")

    dispatcher = updater.dispatcher

    # /start va /generate komandalarini ishlovchi handlerlar
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("generate", generate))

    # Botni ishga tushirish
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()