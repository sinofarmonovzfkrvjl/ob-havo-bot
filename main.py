from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import CommandStart
import logging
import asyncio
import requests
from keyboards import cities_button
from dotenv import load_dotenv
import os

class UzbekistanWeather:
    def __init__(self, place):
        self.place = place

    def today(self):
        response = requests.get(f"https://ob-havo-api-y572.onrender.com/api/v1/obhavo/{self.place}")
        return [response.json(), self.place]

load_dotenv()
bot = Bot(os.getenv("TOKEN"))
router = Router()

@router.startup()
async def startup(bot: Bot):
    await bot.send_message(os.getenv("TELEGRAM_ID"), "Bot ishga tushdi")

@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}\nmen ob havo malumotlarini berivchi botman\no'z hududingizni tanlang", reply_markup=cities_button)

@router.callback_query()
async def CallBackQuery(call: types.CallbackQuery):
    city = call.data
    timess = ["00:00", "03:00", "06:00", "09:00", "12:00", "15:00", "18:00", "21:00"]
    await call.answer(cache_time=60)
    weather = UzbekistanWeather(city).today()
    await call.message.answer(weather[1].capitalize())
    for times in timess:
        await call.message.answer(f"""
            soat {times} da:
            harorat: {weather[0][0]['bugun'][1]['3 soatlik harorat'][times]['harorat']}C
            havo: {weather[0][0]['bugun'][1]['3 soatlik harorat'][times]['havo']}
            shamol tezligi: {weather[0][0]['bugun'][1]['3 soatlik harorat'][times]['shamol tezligi']}
            yog'ingarchilik: {weather[0][0]['bugun'][1]['3 soatlik harorat'][times]["yog'ingarchilik"]}
            namlik: {weather[0][0]['bugun'][1]['3 soatlik harorat'][times]['namlik']}
            yomg'ir yog'ish ehtimoli: {weather[0][0]['bugun'][1]['3 soatlik harorat'][times]["yomg'ir yog'ish ehtimoli"]}
        """)

@router.shutdown()
async def shutdown():
    await bot.send_message(os.getenv("TELEGRAM_ID"), "Bot to'xtadi")

async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="botni ishga tushirish")
    ])

    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


logging.basicConfig(level=logging.INFO)
asyncio.run(main())