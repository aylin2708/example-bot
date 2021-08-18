import telebot

TOKEN = '1949314508:AAGDpitaLVzXmNFMIeugNvELx9kDNzjHJeM'
CHAT_ID = '1204799968'

bot = telebot.TeleBot(TOKEN)

bot.send_message(CHAT_ID, 'hello')

doc = open('/home/aylin/Documentos/example_cubano/PDF/generate.pdf', 'rb')
bot.send_document(CHAT_ID, doc)
bot.send_message(CHAT_ID, "FILEID")