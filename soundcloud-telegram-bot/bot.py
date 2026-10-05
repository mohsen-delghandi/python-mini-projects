from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.request import HTTPXRequest

TOKEN = "8617109010:AAGzBrJjV5sB5QdpwpSTpaiwxYmGhhiGego"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is alive 🎵")

request = HTTPXRequest(proxy="socks5://127.0.0.1:9050")
get_updates_request = HTTPXRequest(proxy="socks5://127.0.0.1:9050")

app = (
    ApplicationBuilder()
    .token(TOKEN)
    .request(request)
    .get_updates_request(get_updates_request)
    .build()
)

app.add_handler(CommandHandler("start", start))

print("BOT STARTED")

app.run_polling()