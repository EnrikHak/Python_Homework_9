from asyncore import dispatcher
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from function_bot import start, cancel, time, abc



bot = Bot(token='')
update = Updater(token='')
dispatcher = update.dispatcher




start_handler = CommandHandler('start', start)
cancel_handler = CommandHandler('cancel', cancel)
time_handler = CommandHandler('time', time)
abc_handler = MessageHandler(Filters.text, abc)




dispatcher.add_handler(start_handler)
dispatcher.add_handler(cancel_handler)
dispatcher.add_handler(time_handler)
dispatcher.add_handler(abc_handler)




print('server start')
update.start_polling()
update.idle()