import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# --- Load Bot Token ---
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    logger.error("❌ BOT_TOKEN is missing! Please set it in Render Environment Variables.")
    raise SystemExit("❌ BOT_TOKEN is missing! Please set it in Render Environment Variables.")

# --- Start Command ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is running successfully!")

def main():
    try:
        application = Application.builder().token(TOKEN).build()

        # Commands
        application.add_handler(CommandHandler("start", start))

        logger.info("🚀 Bot started successfully. Waiting for updates...")
        application.run_polling()

    except Exception as e:
        logger.error(f"❌ Bot crashed with error: {e}", exc_info=True)
        raise

if __name__ == "__main__":
    main()