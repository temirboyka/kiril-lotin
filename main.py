#@lnkl_bot  shu manzilga kiriladi nomi kiril-lotin
from transliterate import to_cyrillic, to_latin
import telebot
TOKEN='6240571606:AAGpf-fvZ9SuLzbdkMbCihSvlaq5FrpHB3M'
bot=telebot.TeleBot(TOKEN,parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob="Assalomu aleykum, Xush kelibsiz!"
    javob+="\nMatn kiriting:"
    bot.reply_to(message,javob)



@bot.message_handler(func=lambda message:True)
def echo_all(message):
    msg=message.text
    if msg.isascii():
        javob=to_cyrillic(msg)
    else:
        javob=to_latin(msg)
    bot.reply_to(message,javob)
bot.polling()
