import telebot
import os
from flask import Flask, request

EXTERNAL_FOLDER = os.path.dirname(os.path.dirname(__file__))
TOKEN = '519955729:AAGIJYECdFK4hmPAqwcg00iJs2V5cO9ePV8'
HOST     = '' # Same FQDN used when generating SSL Cert
PORT     = 8443
CERT     = os.path.join(EXTERNAL_FOLDER, 'server.crt')
CERT_KEY = os.path.join(EXTERNAL_FOLDER, 'server.key')
URL = 'playman31.pythonanywhere.com'


bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)
context = (CERT, CERT_KEY)

markup = types.ReplyKeyboardMarkup(row_width=2)
markup.row('Yes', 'No', 'I dont know')

def launch_app():
	setWebhook()
	app.run(host="127.0.0.1", port=os.environ.get('PORT', 5000), ssl_context = context, debug=True)

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
    bot.set_webhook(url=URL, certificate=open(CERT, 'rb'))