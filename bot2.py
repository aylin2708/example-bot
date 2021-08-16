import os
from typing import Pattern
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import ChatAction, InlineKeyboardMarkup, InlineKeyboardButton
import qrcode
import pyshorteners


INPUT_TEXT = 0
INPUT_URL = 0

def start(update, context):
    
    update.message.reply_text(
        text='¡HOLA!, ¿qué deseas hacer?\n\nUsa /qr para generar un código qr, o utiliza el botón "Generar qr"',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Generar qr ✅', callback_data='qr')],
            [InlineKeyboardButton(text='Página del autor 👩‍⚕', url='https://www.instagram.com/aylinmari_')],
            [InlineKeyboardButton(text='Twitter 📱', url='https://twitter.com')],
            [InlineKeyboardButton(text='Facebook 📱', url='https://facebook.com')],
            [InlineKeyboardButton(text='Acortar URL', callback_data='url')]
        ])
    )
def qr_command_handler(update, context):
    
    update.message.reply_text('Envíe el texto para generar un código QR')

    return INPUT_TEXT

def qr_callback_handler(update, context):

    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text='Envíe el texto para generar un código QR'
    )

    return INPUT_TEXT

def generate_qr(text):

    filename = text + '.jpg'

    img = qrcode.make(text)
    img.save(filename)

    return filename

def send_qr(filename, chat):

    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )

    chat.send_photo(
        photo=open(filename, 'rb')
    )

    os.unlink(filename)



def input_text(update, context):

    text = update.message.text

    filename = generate_qr(text)

    print(filename)

    chat = update.message.chat

    print(chat)
    
    send_qr(filename, chat)

    return ConversationHandler.END


#url
def qr_command_handler(update, context):
    
    update.message.reply_text('Envíe el texto para generar un código QR')

    return INPUT_URL

def url_callback_handler(update, context):

    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text='Envíe un enlace para acortarlo'
    )

    return INPUT_URL

def input_url(update, context):

    url = update.message.text
    chat = update.message.chat

    #acortar url

    s = pyshorteners.Shortener()

    short = s.chilpit.short(url)
    'http://chilp.it/TEST'


    chat.send_action(
        action=ChatAction.TYPING,
        timeout=None
    )

    chat.send_message(
        text=short
    )

    
    return ConversationHandler.END


    
if __name__ == '__main__':
    updater = Updater(token='1949314508:AAGDpitaLVzXmNFMIeugNvELx9kDNzjHJeM', use_context=True)
    
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('qr', qr_command_handler),
            CallbackQueryHandler(pattern='qr', callback=qr_callback_handler)
        ],

        states={
            INPUT_TEXT: [MessageHandler(Filters.text, input_text)]
        },

        fallbacks=[]
    ))

    
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    dp.add_handler(ConversationHandler(
        entry_points=[
            CallbackQueryHandler(pattern='url', callback=url_callback_handler)   
        ],

        states={
            INPUT_URL: [MessageHandler(Filters.text, input_url)]
        },

        fallbacks=[]
    ))

    updater.start_polling()
    updater.idle()

    