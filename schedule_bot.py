#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

from time import gmtime, strftime

import cherrypy
import datetime

import telebot
from telebot import types

import telegram

import config
from config import *

bot = telebot.TeleBot(config.token)


time_of_class1 = '8.30-10.05'
time_of_class2 = '10.15-11.50'
time_of_class3 = '12.00-13.35'
time_of_class4 = '15.40-17.15'
time_of_class5 = '17.25-19.00'
time_of_class6 = '19.10-20.45'


# Webhook-server

class WebhookServer(object):

    @cherrypy.expose
    def index(self):
        if 'content-length' in cherrypy.request.headers and \
                'content-type' in cherrypy.request.headers and \
                cherrypy.request.headers['content-type'] == 'application/json':

            length = int(cherrypy.request.headers['content-length'])

            json_string = cherrypy.request.body.read(length).decode("utf-8")

            update = telebot.types.Update.de_json(json_string)

            # Эта функция обеспечивает проверку входящего сообщения

            bot.process_new_updates([update])

            return ''

        else:

            raise cherrypy.HTTPError(403)

# Handler for start command

@bot.message_handler(commands=["start"])
def keyboard (message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('пн', 'вт', 'ср')
    markup.row('чт', 'пт', 'сб')
    markup.row('чс/зн')
    bot.send_message(message.chat.id, "Привет!", reply_markup=markup)

# Handler for help command

@bot.message_handler(commands=["help"])
def sendHelp(message):
    bot.send_message(
                    message.chat.id, 
                    'Все очень *просто*: нажимай кнопки и получай расписание.\n \
                    Если вдруг кнопок *нет*, воспользуйся коммандой /start', 
                    parse_mode=telegram.ParseMode.MARKDOWN
                    )

# Handler for send shedule if button pressed
# Next time i must take schedule from the text file, not like here)

@bot.message_handler(func=lambda message: True, content_types=["text"])
def main(message):

    date_now = datetime.datetime.now()
    week_num = date_now.isocalendar()[1]

    # If in new semester, parity of weeks is different
    # you can setup it here

    if not week_num % 2:
            week_chet = 'чс'
    else:
            week_chet = 'зн'

    if message.text == "чс/зн":

        if week_chet == 'чс':
            bot.send_message(message.chat.id, 'Числитель')
        else:
            bot.send_message(message.chat.id, 'Знаменатель')

    elif message.text == "пн":

        reply_txt = '*Понедельник ({})*'.format(week_chet)
                + '*{}*\nФизра\n'.format(time_of_class2)
                + '*{}*\n_(чс)_ ---\n_(зн) 392_ Дискретная математика\n'.format(time_of_class3)
                + '*{}*\n_(чс) 319_ Дискретная математика\n\
                    _(зн) 524_ Теория информационных процессов и систем'.format(time_of_class4)
                + '*{}*\n_424ю_ Основы теории управления и цифровой обработки сигналов'.format(time_of_class5)

        bot.send_message(message.chat.id, reply_txt, parse_mode=telegram.ParseMode.MARKDOWN)

    elif message.text == "вт":
        bot.send_message(message.chat.id, 'Вторник', parse_mode=telegram.ParseMode.MARKDOWN)

    elif message.text == "ср":
        bot.send_message(message.chat.id, 'Среда', parse_mode=telegram.ParseMode.MARKDOWN)

    elif message.text == "чт":
        bot.send_message(message.chat.id, 'Четверг', parse_mode=telegram.ParseMode.MARKDOWN)

    elif message.text == "пт":
        bot.send_message(message.chat.id, 'Пятница', parse_mode=telegram.ParseMode.MARKDOWN)

    elif message.text == "сб":
        bot.send_message(message.chat.id, 'Суббота', parse_mode=telegram.ParseMode.MARKDOWN)

    else:

        with open('unrecognizedMessages.txt', 'a', encoding='utf-8') as f:
            user_info = message.from_user

            temp = [
                    strftime("%d-%m-%Y %H:%M:%S", gmtime()),
                    str(message.from_user),
                    message.text
                    ]

            f.write(str(temp) + '\n')


        if (message.chat.id == somebody_telegram_id):
            bot.send_message(message.chat.id, "message to somebody")

        if (message.chat.id == somebody_telegram_id):
            bot.send_message(message.chat.id, "message to somebody")

        else:
            bot.send_message(message.chat.id, "Не понимаю тебя")

bot.remove_webhook()

bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH, certificate=open(WEBHOOK_SSL_CERT, 'r'))

# Settings for cherrypy web-server

cherrypy.config.update({
    'server.socket_host': WEBHOOK_LISTEN,
    'server.socket_port': WEBHOOK_PORT,
    'server.ssl_module': 'builtin',
    'server.ssl_certificate': WEBHOOK_SSL_CERT,
    'server.ssl_private_key': WEBHOOK_SSL_PRIV
})

cherrypy.quickstart(WebhookServer(), WEBHOOK_URL_PATH, {'/': {}})
