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
import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': 'socks5h://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 
def planet_go(bot,update):
    user_text_planet= update.message.text
    planet_split=user_text_planet.split()
    planet=planet_split[1].capitalize()
    #print(planet)

    today = datetime.datetime.today()
    today_st=today.strftime("%Y/%m/%d")
    
    if planet == 'Mercury':
        result = ephem.constellation(ephem.Mercury(today_st))
    elif planet == 'Venus':
        result = ephem.constellation(ephem.Venus(today_st))
    elif planet == 'Mars':
        result = ephem.constellation(ephem.Mars(today_st))
    elif planet == 'Jupiter':
        result = ephem.constellation(ephem.Jupiter(today_st))
    elif planet == 'Saturn':
        result = ephem.constellation(ephem.Saturn(today_st))
    elif planet == 'Uranus':
        result = ephem.constellation(ephem.Uranus(today_st))
    elif planet == 'Neptune':
        result = ephem.constellation(ephem.Neptune(today_st))
    elif planet == 'Pluto':
        result = ephem.constellation(ephem.Neptune(today_st))
    print (result)        
    update.message.reply_text(result)


def main():
    mybot = Updater("705952373:AAHroSOXqrgr0dySvq2oZxpHVavWwTL956g", request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_go))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()