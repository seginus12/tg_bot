from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv
from app.hendlers import router
import app.keyboards as kb

load_dotenv()


bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()
dp.include_router(router)