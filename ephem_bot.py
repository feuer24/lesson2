from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )    

def greet_user(bot, update):
    text = 'Вызван /start Привет'
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s",
    update.message.chat.username,
    update.message.chat.id,
    update.message.text)
    update.message.reply_text(user_text)

def get_position(bot, update):
    user_text = update.message.text.split()
    planet = user_text[1]
    if planet == 'Mars':
        pos = ephem.Mars('2019/12/01')
    elif planet == 'Venus':
        pos = ephem.Venus('2019/12/01')
    elif planet == 'Jupiter':   
        pos = ephem.Jupiter('2019/12/01')
    elif planet == 'Saturn':   
        pos = ephem.Saturn('2019/12/01')         
    constellation = ephem.constellation(pos)
    update.message.reply_text(constellation)

def main():
    mybot = Updater(settings.API_KEY)
    logging.info("Bot is running")
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet',get_position))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()
main()    