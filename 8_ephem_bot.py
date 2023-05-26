"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import settings

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}

planets = ['Venus','Mercury',  'Mars', 'Jupiter', 'Saturn', 'Uranus','Pluto']

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text('Welcome to the club, buddy!')

def planet(update, context):
    text = 'Вызван /planet'
    print(text)
    update.message.reply_text('Введите название планеты на английском')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)
    may_be_planet = user_text.title()
    for i in planets:
        if may_be_planet == i:
            planet_coord = str('ephem.' + i + '(date.today())')
            print(eval(planet_coord))
            update.message.reply_text(ephem.constellation(eval(planet_coord)))
            mars = ephem.Mars(date.today())
            print(ephem.constellation(mars))




def main():
    mybot = Updater( settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
