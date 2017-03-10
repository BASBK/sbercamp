import os
import telebot
from flask import Flask
import config
import texts


bot = telebot.TeleBot(config.token)

server = Flask(__name__)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.from_user.id, texts.anyInputText, reply_markup=config.start_menu())


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.find('Программа') != -1:
        bot.send_message(message.from_user.id, texts.programText, reply_markup=config.program_menu())
    elif message.text.find('Назад') != -1:
        bot.send_message(message.from_user.id, texts.anyInputText, reply_markup=config.start_menu())
    elif message.text.find('Спикеры') != -1:
        bot.send_message(message.from_user.id, texts.speakersText)
    elif message.text.find('Чат') != -1:
        bot.send_message(message.from_user.id, texts.chatText)
    elif message.text.find('Стикеры') != -1:
        bot.send_message(message.from_user.id, texts.stickersText)
    elif message.text.find('Контакты') != -1:
        bot.send_message(message.from_user.id, texts.contactsText)
    elif message.text.find('2️⃣2️⃣ марта') != -1:
        bot.send_message(message.from_user.id, texts.march22)
    elif message.text.find('2️⃣3️⃣ марта') != -1:
        bot.send_message(message.from_user.id, texts.march23)
    elif message.text.find('2️⃣4️⃣ марта') != -1:
        bot.send_message(message.from_user.id, texts.march24)
    elif message.text.find('2️⃣5️⃣ марта') != -1:
        bot.send_message(message.from_user.id, texts.march25)
    else:
        bot.send_message(message.from_user.id, texts.anyInputText, reply_markup=config.start_menu())

#bot.polling(none_stop=True)


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://sber-camp-bot.herokuapp.com/")
    return "!", 200

server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
