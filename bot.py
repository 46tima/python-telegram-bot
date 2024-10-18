import os
from telegram.ext import Updater, CommandHandler

# Define a start command
def start(update, context):
    update.message.reply_text('Hello! I am your Telegram bot.')

# Main function to start the bot
def main():
    token = os.getenv('TELEGRAM_TOKEN')
    
    # Create the Updater and pass it your bot's token
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register a handler for the /start command
    dp.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
