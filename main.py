import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
import os
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()



@dp.message()
async def cmd_start(message: Message):
    await message.answer("окэй")
    # await message.reply("допустим")


async def main():
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())


# from aiogram import Bot, Dispatcher, types
# from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# API_TOKEN = "7395412269:AAHuuaeAaXcjBTpDyUbt5V7YemXD2dj3vps"

# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(storage=MemoryStorage())

# @dp.message(commands=['start'])
# async def start(message: types.Message):
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(KeyboardButton("Option 1"))
#     keyboard.add(KeyboardButton("Option 2"))
    
#     await message.answer("Choose an option:", reply_markup=keyboard)

# if __name__ == '__main__':
#     import asyncio
#     loop = asyncio.get_event_loop()
#     try:
#         loop.create_task(dp.start_polling())
#         loop.run_forever()
#     except KeyboardInterrupt:
#         pass
#     finally:
#         loop.stop()
#         loop.close()