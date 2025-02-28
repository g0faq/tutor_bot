from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [KeyboardButton("👩‍🏫 Инфо о преподавателе")],
        [KeyboardButton("📅 Записаться"), KeyboardButton("📆 График")],
        [KeyboardButton("📑 Домашние задания"), KeyboardButton("💬 Отзывы")],
        [KeyboardButton("🎓 Занятие"), KeyboardButton("📞 Поддержка")]
    ]
    reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)

    welcome_message = "👋 Привет! Я помогу вам с учебным процессом. 😊\n\nВыберите нужный раздел!"

    await update.message.reply_text(welcome_message, reply_markup=reply_markup)


def main():
    app = ApplicationBuilder().token('7629398192:AAFXoPvvx-F_al0uL9dY8jSC3lafwUnv7ws').build()

    app.add_handler(CommandHandler("start", start))

    print("✅ Бот успешно запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()