import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
from flask import Flask
import os
import threading

# ✅ ВАШ НОВЫЙ ТОКЕН
bot = telebot.TeleBot("8411299364:AAEKoMeXTumvx-TyNvIwhJspau9QIWJtNFo")

# ✅ УДАЛЯЕМ WEBHOOK
requests.get(f"https://api.telegram.org/bot8046950381:AAFswiapOFK1jhaX2T47IKxQLkE63UVMcaQ/deleteWebhook")

PHOTO_URL = "https://photos.app.goo.gl/Rh8dsJ1N8ZWoNw2F6"

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Bot is alive!"

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
    
    bot.send_photo(
        chat_id=message.chat.id,
        photo=PHOTO_URL,
        caption="Выбери то, что интересует тебя.",
        reply_markup=markup
    )

def run_bot():
    bot.polling()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    threading.Thread(target=run_bot, daemon=True).start()
    app.run(host='0.0.0.0', port=port)
