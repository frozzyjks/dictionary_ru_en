from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from dictionary import translate_text

# Вставь сюда токен от BotFather
TOKEN = "7478005440:AAFvNfUGe1ZAnZiKicHj5pgPxnxEy_WuR4Q"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я бот-словарь.\n"
        "Отправь мне слово или текст, и я переведу его на английский.\n"
        "Команды:\n/start - приветствие\n/help - помощь"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Просто напиши слово или текст, а я переведу его на английский."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    translation = translate_text(text)
    await update.message.reply_text(f"Перевод: {translation}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()
