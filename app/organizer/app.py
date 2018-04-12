import telebot
import os
from flask import Flask, request

TOKEN = '519955729:AAGIJYECdFK4hmPAqwcg00iJs2V5cO9ePV8'
HOST     = '' # Same FQDN used when generating SSL Cert
PORT     = 8443
CERT     = 'path/to/ssl/server.crt'
CERT_KEY = 'path/to/ssl/server.key'


bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

markup = types.ReplyKeyboardMarkup(row_width=2)
markup.row('Yes', 'No', 'I dont know')

def launch_app():
	setWebhook()
	app.run(host="127.0.0.1", port=os.environ.get('PORT', 5000))

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: message.text == 'Ask me')
def ask(message):
    tb.send_message(chat_id, "Choose your answer:", reply_markup=markup)


@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return 'OK'
'''
@app.route('/' + TOKEN, methods=['POST'])
def process():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return 'OK'
   '''

def setWebhook():
    bot.remove_webhook()
    bot.set_webhook(url="", certificate=open(CERT, 'rb'))