import telebot

TOKEN = '1949314508:AAGDpitaLVzXmNFMIeugNvELx9kDNzjHJeM'
CHAT_ID = '1204799968'

bot = telebot.TeleBot(TOKEN)

bot.send_message(CHAT_ID, 'hello')
ti = open('/home/aylin/Documentos/example_cubano/sticker/sticker.webp', 'rb')
bot.send_sticker(CHAT_ID, ti)