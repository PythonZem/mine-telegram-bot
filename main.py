import logging

from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
from utilities import get_rate, form_massage
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

CHOOSING = 1

reply_keyboard = [
    ["Get the currency exchange rate",],
]
markup = ReplyKeyboardMarkup(
    reply_keyboard,
    one_time_keyboard=True,
    resize_keyboard=True
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    await update.message.reply_text(
        "Hi! I was created to display currency rates in Privatbank."
        " That's one thing I was created for. What do you want?",
        reply_markup=markup,
    )

    return CHOOSING


async def show_rates(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(form_massage(get_rate()))

    return CHOOSING


async def done(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    return ConversationHandler.END


def main() -> None:
    """Run the bot."""

    application = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CHOOSING: [
                MessageHandler(
                    filters.Regex("^(Get the currency exchange rate)$"), show_rates
                ),
            ],
        },
        fallbacks=[MessageHandler(filters.Regex("^Done$"), done)],
    )

    application.add_handler(conv_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
