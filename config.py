import telebot

token = '354272842:AAGWgmksR4CJzwU9bq3inMZNsvSpX5Q1cCU'


def start_menu():
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('📋 Программа мероприятия')
    user_markup.row('🗣 Спикеры')
    user_markup.row('💬 Чат')
    user_markup.row('💥 Стикеры')
    user_markup.row('☎ Контакты')
    return user_markup


def program_menu():
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    # 22
    user_markup.row('2️⃣2️⃣ марта')
    # 23
    user_markup.row('2️⃣3️⃣ марта')
    # 24
    user_markup.row('2️⃣4️⃣ марта')
    # 25
    user_markup.row('2️⃣5️⃣ марта')
    user_markup.row('⬅️Назад')
    return user_markup
