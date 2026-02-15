import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot("8411299364:AAF4mkwmXt-LHoxvWbIs2XWzGvTwq5pqg5w")

@bot.message_handler(commands=['start', 'menu'])
def send_menu(message):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("Instagram", url="https://www.instagram.com/kami.kaaa_"),
        InlineKeyboardButton("TikTok", url="https://www.tiktok.com/@kamiw.www")
    )
    markup.add(
        InlineKeyboardButton("Boost", url="https://t.me/boost?c=3041366792"),
        InlineKeyboardButton("Чат", url="https://t.me/kamachatnax")
    )
    bot.send_message(message.chat.id, 'Соц.Сети Kami', reply_markup=markup)

bot.polling()
