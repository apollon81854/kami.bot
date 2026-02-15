import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.webhook import aiohttp_server
from aiohttp import web

API_TOKEN = '8411299364:AAF4mkwmXt-LHoxvWbIs2XWzGvTwq5pqg5w'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command('start', 'menu'))
async def send_menu(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/kami.kaaa_'),
        types.InlineKeyboardButton(text='TikTok', url='https://www.tiktok.com/@kamiw.www')
    )
    builder.row(
        types.InlineKeyboardButton(text='Boost', url='https://t.me/boost?c=3041366792'),
        types.InlineKeyboardButton(text='Чат', url='https://t.me/kamachatnax')
    )
    await message.answer('Соц.Сети Kami', reply_markup=builder.as_markup())

async def on_startup(_):
    await bot.set_webhook("https://YOUR-SERVICE.onrender.com/webhook")

if __name__ == '__main__':
    app = web.Application()
    aiohttp_server.register_handlers(dp, app, path="/webhook")
    web.run_app(app, host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
