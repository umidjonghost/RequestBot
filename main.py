import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = "7763814340:AAHZd5_wuXq8hv00nAZAVa548t6YrcZWkWY"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer("Assalomu alaykum!")

async def main():
    print('working')
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())




