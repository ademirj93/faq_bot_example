from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from core.faq_engine import get_answer
import asyncio

# ATENÇÃO: este código usa aiogram v2 API

bot_instance = None

def start_telegram(token: str):
    """Starta o bot do Telegram (bloqueante)."""
    global bot_instance
    bot_instance = Bot(token=token)
    dp = Dispatcher(bot_instance)

    @dp.message_handler(commands=['start', 'help'])
    async def send_welcome(message: types.Message):
        await message.reply("Olá! Envie uma pergunta sobre jogos e eu tentarei responder.")

    @dp.message_handler()
    async def handle_msg(message: types.Message):
        q = message.text or ""
        resposta = get_answer(q)
        await message.reply(resposta)

    executor.start_polling(dp, skip_updates=True)

if __name__ == "__main__":
    import os
    token = os.getenv("TELEGRAM_TOKEN") or "SEU_TOKEN_TELEGRAM"
    start_telegram(token)
