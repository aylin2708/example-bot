from telegram.ext import Updater, CommandHandler, updater

def start(update, context):

    update.message.reply_text('Hello, human!')

if __name__ == '__main__':

    updater = Updater(token='1949314508:AAGDpitaLVzXmNFMIeugNvELx9kDNzjHJeM', use_context=True)
    
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()
