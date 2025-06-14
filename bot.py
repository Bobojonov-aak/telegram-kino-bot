from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7564598151:AAGpEfKlm4f7HMdk5UmYsjFjEBY1up3TPXY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Tarjima kinolar botiga xush kelibsiz!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Yordam: /kino buyrug‘ini yozing.")

async def kino(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎬 Bugungi kino: https://t.me/examplekino")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("kino", kino))
    app.run_polling()

if __name__ == "__main__":
    main()
