from telegram.ext import Updater,CommandHandler

PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}




def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text) #ответ бота на сообщение

def main():
    mybot = Updater("705952373:AAHroSOXqrgr0dySvq2oZxpHVavWwTL956g", request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user)) #добавить в диспетчер старт
    mybot.start_polling() #начни забирать сообщения
    mybot.idle() #работай,пока не закроют




main() 
