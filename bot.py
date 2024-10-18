import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Обработка команды /start
def start(update, context):
    update.message.reply_text('Привет! Я ваш Telegram бот. Чем могу помочь?')

# Обработка команды /help
def help_command(update, context):
    update.message.reply_text('Вы можете использовать следующие команды:\n/start - Начать работу с ботом\n/help - Получить помощь')

# Эхо-ответ на любое текстовое сообщение
def echo(update, context):
    update.message.reply_text(f'Вы сказали: {update.message.text}')

def main():
    # Получаем токен из переменной окружения
    token = os.getenv('TELEGRAM_TOKEN')
    
    # Создаем Updater и передаем токен
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    # Регистрируем команды и обработчики сообщений
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Запуск бота
    updater.start_polling()

    # Работаем до нажатия Ctrl-C или завершения процесса
    updater.idle()

if __name__ == '__main__':
    main()
