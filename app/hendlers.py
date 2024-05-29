from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from loader import bot


router = Router()

channel_id = "-1002212766882"

@router.message(Command('send_poll'))
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
