import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from core.faq_engine import get_answer

async def start_telegram(token: str):
    bot = Bot(token=token)
    dp = Dispatcher()

    @dp.message(Command("start"))
    async def cmd_start(message: Message):
        await message.answer("Olá! Envie uma pergunta sobre jogos e eu tentarei responder.")

    @dp.message()
    async def handle_msg(message: types.Message):
        q = message.text or ""
        resposta = get_answer(q)
        await message.answer(resposta)

    await dp.start_polling(bot, handle_signals=False)

if __name__ == "__main__":
    import os
    token = os.getenv("TELEGRAM_TOKEN") or "SEU_TOKEN_TELEGRAM"
    asyncio.run(start_telegram(token))
