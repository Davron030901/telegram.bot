from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import os
import google.generativeai as genai

# GeminAI API bilan bog'lanish funksiyasi
def get_response_from_geminAI(message):
    # API kalitini atrof-muhit o'zgaruvchisidan oling
    api_key = os.environ.get("API_KEY")

    if api_key is None:
        print("API kaliti o'rnatilmagan! Atrof-muhit o'zgaruvchisini o'rnating.")
        return "API kaliti o'rnatilmagan!"
    else:
        # API kalitini sozlash
        genai.configure(api_key=api_key)

        # Modelni yaratish
        generation_config = {
            "temperature": 0.9,
            "top_p": 1,
            "max_output_tokens": 2048,
            "response_mime_type": "text/plain",
        }

        model = genai.GenerativeModel(
            model_name="gemini-1.0-pro",
            generation_config=generation_config,
        )

        # Foydalanuvchi bilan muloqot sessiyasini boshlash
        chat_session = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [
                        "easy to gemini\n",
                    ],
                },
                {
                    "role": "model",
                    "parts": [
                        "**Gemini Zodiac Sign**\n\n**Dates:** May 21 - June 21\n**Element:** Air\n**Symbol:** The Twins\n**Ruling Planet:** Mercury\n**Key Traits:** Communication, Intelligence, Adaptability, Curiosity\n\n...",
                    ],
                },
            ]
        )

        # Foydalanuvchi xabariga javob olish
        response = chat_session.send_message(message)
        return response.text  # Javobni qaytarish

# /start komandasi
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Assalomu alaykum! Menga savolingizni yuboring.')

# Foydalanuvchi xabariga javob berish
async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    response = get_response_from_geminAI(user_message)
    await update.message.reply_text(response)

def main():
    # Telegram bot tokenini kiriting
    token = '7208041122:AAHKOUYfR-kDmYAaYcusghikHBKPNWWisbU'

    # Yangilangan `Application` sinfi yordamida botni yaratish
    application = Application.builder().token(token).build()

    # Handlerlarni qo'shish
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Botni ishga tushirish
    application.run_polling()

if __name__ == '__main__':
    main()
