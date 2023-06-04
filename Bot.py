from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm a Telegram bot.")

# Function to handle regular text messages
def echo(update, context):
    user_id = update.message.from_user.id
    chat_id = update.message.chat.id
    context.bot.send_message(chat_id=chat_id, text=f"User ID: {user_id}")
    context.bot.send_message(chat_id=chat_id, text=f"Channel ID: {chat_id}")

# Main function
def main():
    # Create an instance of the Updater class and pass in your bot token
    updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the handlers
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

# Call the main function to start the bot
if __name__ == '__main__':
    main()
