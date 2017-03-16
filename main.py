import os
import telebot
from flask import Flask, request
import config
import texts
import logging

bot = telebot.TeleBot(config.token)

server = Flask(__name__)


logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

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
        bot.send_message(message.from_user.id, texts.speakersText, reply_markup=config.speaker_menu())
    elif message.text.find('Сергей Король') != -1:
        bot.send_message(message.from_user.id, texts.speaker_Korol)
        bot.send_video(message.from_user.id, texts.speaker_Korol_video)
    elif message.text.find('Татьяна Иванова') != -1:
        bot.send_message(message.from_user.id, texts.speaker_Ivanova)
        bot.send_photo(message.from_user.id, texts.speaker_Ivanova_img)
    elif message.text.find('Сергей Ешанов') != -1:
        bot.send_message(message.from_user.id, texts.speaker_Eshanov)
        bot.send_video(message.from_user.id, texts.speaker_Eshanov_video)
    elif message.text.find('Александр Якунин') != -1:
        bot.send_message(message.from_user.id, texts.speaker_Yakunin)
        bot.send_video(message.from_user.id, texts.speaker_Yakunin_video)
    elif message.text.find('Василий Ящук') != -1:
        bot.send_message(message.from_user.id, texts.speaker_Yaschuk, disable_web_page_preview=True)
        bot.send_photo(message.from_user.id, texts.speaker_Yaschuk_img)
    elif message.text.find('Павел Перец') != -1:
        bot.send_message(message.from_user.id, texts.speaker_Perec, disable_web_page_preview=True)
        bot.send_document(message.from_user.id, texts.speaker_Perec_doc)
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
        bot.send_message(message.from_user.id, texts.anyInputText)

# bot.polling(none_stop=True)


@server.route("/", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://sber-camp-bot.herokuapp.com/")
    return "!", 200

server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
# server.run()
