import telebot

TOKEN = '1949314508:AAGDpitaLVzXmNFMIeugNvELx9kDNzjHJeM'
CHAT_ID = '1204799968'

bot = telebot.TeleBot(TOKEN)

bot.send_message(CHAT_ID, 'hello')

video = open('/home/aylin/Documentos/example_cubano/video/video_2021-08-17_19-37-28.mp4', 'rb')
bot.send_video(CHAT_ID, video)