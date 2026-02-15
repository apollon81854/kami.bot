import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests

bot = telebot.TeleBot("8592922954:AAGwp6AfDHXIqLglkNSJycw_w4K7UMZzoZw")

# ✅ УДАЛЯЕМ WEBHOOK
requests.get(f"https://api.telegram.org/bot{bot.token}/deleteWebhook")

# ✅ URL вашего фото (замените на своё)
PHOTO_URL = "https://photos.app.goo.gl/Rh8dsJ1N8ZWoNw2F6"  # ← ВСТАВЬТЕ ССЫЛКУ НА ФОТО

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
    
    # ✅ ОТПРАВЛЯЕМ ФОТО + ТЕКСТ + КНОПКИ
    bot.send_photo(
        chat_id=message.chat.id,
        photo=PHOTO_URL,  # Ссылка на фото
        caption="Выбери то, что интересует тебя.",  # Текст под фото
        reply_markup=markup  # Кнопки под фото
    )

bot.polling()
