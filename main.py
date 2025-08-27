import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Get token from environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Must join channels
MUST_JOIN = [
    "https://t.me/boteratrack",
    "https://t.me/boterapro"
]

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    text = (
        f"👋 Hello {user.first_name}!\n\n"
        "Welcome to the Bot Builder 🤖\n\n"
        "Before you can use this bot, please make sure you’ve joined our channels:\n"
        "1️⃣ https://t.me/boteratrack\n"
        "2️⃣ https://t.me/boterapro\n\n"
        "✅ After joining, you can access all features!"
    )

    await update.message.reply_text(text)

# Simple ping command
async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏓 Pong! Bot is working fine.")

def main():
    # Create app
    app = Application.builder().token(BOT_TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ping", ping))

    # Run bot
    app.run_polling()

if __name__ == "__main__":
    main()