# инициализация бота
bot = telebot.TeleBot(BOT_TOKEN)


# Создание клавиатуры с кнопкой "Start"
def create_start_button(func=lambda message: message.text.lower() == '/start'):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    start_button = telebot.types.KeyboardButton("/start")
    markup.add(start_button)
    return markup


@bot.message_handler(commands=['start'])
def start_command_handler(message):
    handle_start(bot, message)


@bot.message_handler(commands=["menu"])
def menu(message):
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=main_menu())  # Вызов основного меню


@bot.message_handler(func=lambda message: True)  # Для любых других сообщений отправляем кнопку /menu
def send_menu_button(message):
    bot.send_message(message.chat.id, "Для доступа к функциям выберите /menu", reply_markup=create_menu_button())  # Кнопка /menu


bot.polling(non_stop=True)