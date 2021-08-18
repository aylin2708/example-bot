import telebot

TOKEN = '1949314508:AAGDpitaLVzXmNFMIeugNvELx9kDNzjHJeM'
CHAT_ID = '1204799968'

bot = telebot.TeleBot(TOKEN)

bot.send_message(CHAT_ID, 'hello')

photo = open('/home/aylin/Documentos/example_cubano/imagen/Bots-de-Telegram-2.jpg', 'rb')
bot.send_photo(CHAT_ID, photo)
bot.send_photo(CHAT_ID, "FILEID")