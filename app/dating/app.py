import telebot
import os
from flask import Flask, request

'''bot = telebot.TeleBot("519955729:AAGIJYECdFK4hmPAqwcg00iJs2V5cO9ePV8")
app = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


@app.route("/519955729:AAGIJYECdFK4hmPAqwcg00iJs2V5cO9ePV8", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://ссылка на приложение/токен вашего бота")
    return "!", 200

app.run(host="127.0.0.1", port=os.environ.get('PORT', 5000))'''