import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, PollAnswer
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.utils.keyboard import InlineKeyboardBuilder
import os
from dotenv import load_dotenv
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

load_dotenv()

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()
channel_id = "-1002212766882"


class CreatePoll(StatesGroup):
    set_poll_name = State()
    set_poll_choices = State()
    set_right_choice = State()
    set_points_and_send = State()


@dp.poll_answer()
async def update_poll_answers(poll_answer: PollAnswer):
    print("ну хоть что-нибудь")
    print(poll_answer.option_ids)
    print(poll_answer.user.id)
    print(poll_answer.poll_id)


# 0. Вход в создание опроса
@dp.message(StateFilter(None), Command('create_poll'))
async def create_poll(message: Message, state: FSMContext):
    # await bot.send_message(channel_id, "Введите название опроса")
    await message.answer(
        text="Введите название опроса:",
        # reply_markup=make_row_keyboard(available_food_names)
    )
    await state.set_state(CreatePoll.set_poll_name)


# 1. Установка имени опроса
@dp.message(CreatePoll.set_poll_name, F.text)
async def set_poll_name(message: Message, state: FSMContext):
    await state.update_data(poll_name=message.text)
    await message.answer(
        text="Введите варианты ответа одним сообщением. Каждый вопрос должен быть с новой строки:",
    )
    await state.set_state(CreatePoll.set_poll_choices)


# 1. Если имя опроса введено неверно
@dp.message(CreatePoll.set_poll_name)
async def set_poll_name(message: Message):
    await message.answer(
        text="Название опроса должно быть текстом. Попробуйте ещё раз:",
    )


# 2. Установка вопросов
choice_numbers = []
@dp.message(CreatePoll.set_poll_choices, F.text)
async def set_poll_choices(message: Message, state: FSMContext):
    choices_list = message.text.splitlines()
    await state.update_data(poll_choices=choices_list)
    numered_choices_str = ""
    for i in range(len(message.text.splitlines())):
        numered_choices_str = numered_choices_str + str(i+1) + ': ' +  choices_list[i] + '\n'
        choice_numbers.append(str(i+1))
    await message.answer(
        text=f"""Вы ввели следующие варианты ответов:
{numered_choices_str}
Укажите номер верного варианта ответа:
""")
    await state.set_state(CreatePoll.set_right_choice)


# 2. Если вопросы были введены неверно
@dp.message(CreatePoll.set_poll_choices)
async def set_poll_choices(message: Message):
    await message.answer(
        text="Варианты ответов были введены неверно. Попробуйте ещё раз:",
    )


# 3. Установка верного варианта ответа
@dp.message(CreatePoll.set_right_choice, F.text.in_(choice_numbers))
async def set_right_choice(message: Message, state: FSMContext):
    await state.update_data(right_choice=int(message.text) - 1)
    await message.answer(
        text="Введите стоимость верного варианта:",
    )
    globals()['choice_numbers'] = []
    await state.set_state(CreatePoll.set_points_and_send)


# 3. Установка верного варианта ответа
@dp.message(CreatePoll.set_right_choice)
async def set_right_choice(message: Message):
    await message.answer(
        text="Номер верного варианта введён неверно. Попробуйте ещё раз:",
    )


# 4. Установка стоимости правильного варианта и отправка опроса
@dp.message(CreatePoll.set_points_and_send, F.text.regexp(r'^\+?(0|[1-9]\d*)$'))
async def set_points(message: Message, state: FSMContext):
    await state.update_data(points=message.text)
    await message.answer(
        text="Опрос успешно создан.",
    )
    data = await state.get_data()
    await bot.send_poll(
        chat_id=channel_id,
        question=data['poll_name'],
        options=data['poll_choices'],
        type="quiz",
        correct_option_id=data['right_choice'],
        # is_anonymous=False
        )
    await state.clear()


# 4. Если стоимость была введена неверно
@dp.message(CreatePoll.set_points_and_send)
async def set_points(message: Message):
    await message.answer(
        text="Стоимость верного ответа была введена неверно. Попробуйте ещё раз:",
    )


async def main():
    await dp.start_polling(bot, allowed_updates=["message", "inline_query", "poll", "poll_answer"])


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
