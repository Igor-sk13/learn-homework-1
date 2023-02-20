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
import settings
import ephem
import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

"""
PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}
"""

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

"""
def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)
"""
def planet(update, context):
    text_planet = ' '.join(context.args)
    print(text_planet)

    if hasattr(ephem, text_planet):
        target_planet = getattr(ephem, text_planet)
        today = datetime.date.today()
        planet_now = target_planet(today)

        zodiac_name = ephem.constellation(planet_now)
        update.message.reply_text(f'{text_planet} сегодня находится в {zodiac_name}')

    else:
        update.message.reply_text(f'{text_planet} еще неизвестна науке, попробуем поискать что-то другое?')


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    #dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", planet))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
