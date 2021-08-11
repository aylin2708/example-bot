import os
from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

INPUT_TEXT = 0

def start(update, context):

    button1 = InlineKeyboardButton(
        text='Sobre el autor',
        url='https://lugodev.com'
    )

    button2 = InlineKeyboardButton(
        text='Twitter',
        url='https://twitter.com'
    )

    update.message.reply_text(
        text='Haz click en un botón',
        reply_markup=InlineKeyboardMarkup([
            [button1],
            [button2]
        ])
    )

if __name__ == '__main__':

    updater = Updater(token=os.environ['TOKEN'], use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()