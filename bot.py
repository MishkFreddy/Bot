import random
import string
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Функция генерации пароля
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Обработчик команды /generate
def generate_handler(update: Update, context: CallbackContext) -> None:
    length = 12  # Можно изменить длину пароля по желанию
    password = generate_password(length)
    update.message.reply_text(f"Сгенерированный пароль: {password}")

# Главная функция
def main():
    # Токен вашего бота
    updater = Updater("", use_context=True)

    # Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчик команды /generate
    dp.add_handler(CommandHandler("generate", generate_handler))

    # Стартуем бота
    updater.start_polling()

    # Останавливаем бота при нажатии Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
