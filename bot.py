import qrcode

from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

INPUT_TEXT = 0

def start(update, context):

    update.message.reply_text('¡Hola bienvenido!, ¿qué deseas hacer?\n\nUsa /qr para generar un código qr')

def qr_command_handdler(update, context):

    update.message.reply_text('Envíe el texto para generar un código QR')

    return INPUT_TEXT

def generate_qr(text):

    filename = text + '.jpg'

    img = qrcode.make(text)
    img.save(filename)

    return filename


def input_text(update, context):

    text = update.message.text

    filename = generate_qr(text)

    print(filename)
    
    #send_qr(filename)

    return ConversationHandler.END

if __name__ == '__main__':

    updater = Updater(token='1949314508:AAGDpitaLVzXmNFMIeugNvELx9kDNzjHJeM', use_context=True)
    
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('qr', qr_command_handdler)
        ],

        states={
            INPUT_TEXT: [MessageHandler(Filters.text, input_text)]
        },

        fallbacks=[]
    ))

    updater.start_polling()
    updater.idle()
