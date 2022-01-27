from telebot import *
bot = TeleBot("5041489350:AAEoMuYuOsWsAbEYLA0sJOA1W7I7x7JGi5o")

Tugmalar =types.InlineKeyboardMarkup(row_width=(2))
tugma1=types.InlineKeyboardButton('Uzbek',callback_data='S')
tugma2=types.InlineKeyboardButton('Rus',callback_data='H')
Tugmalar.add(tugma1,tugma2)
# Tugmalar = types.ReplyKeyboardMarkup(resize_keyboard=True)
# tugma1=types.KeyboardButton('Salom')
# tugma2=types.KeyboardButton('xayir')
# Tugmalar.add(tugma1)
# Tugmalar.add(tugma2)
@bot.message_handler(commands='start')
def start(message):
    bot.send_message(message.chat.id,f"Assalomu Alaykum {message.from_user.first_name} Botga xush kelibsiz")
    bot.send_message(message.chat.id,f'Iltimos {message.from_user.first_name} tilni tanlang xush',reply_markup=Tugmalar)
@bot.callback_query_handler(func=lambda call:True)
def call(message):
    bot.send_message(message.message.chat.id,"salom")
# @bot.message_handler(content_types=['text'])
# def botts(msa)    :
#     if msa.text=='Salom':
#         bot.send_message(msa.chat.id,"hello")
#     elif msa.text=='xayir':
#         bot.send_message(msa.chat.id,'goodbay')
bot.polling()