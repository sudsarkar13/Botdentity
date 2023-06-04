from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm a Telegram bot.")

def echo(update, context):
    user_id = update.message.from_user.id
    chat_id = update.message.chat.id
    context.bot.send_message(chat_id=chat_id, text=f"User ID: {user_id}")
    context.bot.send_message(chat_id=chat_id, text=f"Channel ID: {chat_id}")

def main():
    token = os.environ.get('BOT_TOKEN')
    if token is None:
        print("Error: Bot token not found in environment variables.")
        return
    
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
