from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler


class Bot:
    def __init__(self, bot_token: str):
        self.bot_token = bot_token

    @staticmethod
    async def start_command(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text('This is a test message')

    def start_bot(self):
        start_handler = CommandHandler('start', self.start_command)
        application = ApplicationBuilder().token(self.bot_token).build()
        application.add_handler(start_handler)
        application.run_polling()
