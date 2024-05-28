import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
import os
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()

channel_id = "-1002212766882"

# @dp.message()
# async def send_poll(message: Message):
#     print(message.chat.id)
#     # await bot.send_message(channel_id, "sosat")
#     poll_options = ['a', 'b', 'c']
#     await bot.send_poll(
#         chat_id=channel_id,
#         question="Hoho",
#         options=poll_options,
#         type="quiz",
#         correct_option_id=0
#         )
    
@dp.message(Command('send_poll'))
async def send_poll(message: Message):
    print(message.chat.id)
    # await bot.send_message(channel_id, "sosat")
    poll_options = ['a', 'b', 'c']
    await bot.send_poll(
        chat_id=channel_id,
        question="Hoho",
        options=poll_options,
        type="quiz",
        correct_option_id=0
        )
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