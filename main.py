from env import Env
from queuing.queuing_service import QueuingService

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Halo!')


def handle_response(text: str) -> str:
    lowerized: str = text.lower()

    return lowerized


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    is_private_chat: bool = (update.message.chat.type != 'group')
    chat_id: int = update.message.chat.id
    user_name: str = update.message.chat.first_name
    user_message: str = update.message.text

    if is_private_chat:
        await QueuingService.send_messages(update.message, chat_id, user_name, user_message)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(Env.BOT_TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=5)
