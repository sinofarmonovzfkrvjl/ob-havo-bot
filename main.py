from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import CommandStart
import logging
import asyncio
import requests
from keyboards import cities_button, times
from dotenv import load_dotenv
import os

place = {'place': None}

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

@router.callback_query(lambda call: call.data in ["zero", "three", "six", "nine", "twelve", "fiveteen", "eighteen", "twentyone", "twentyfour"])
async def CallBackQuery(call: types.CallbackQuery):
    print(call.data)
    weather = UzbekistanWeather(place=place['place']).today()
    if call.data == "zero":
        await call.message.answer(f"""
            soat {times} da:
            harorat: {weather[0][0]['bugun'][1]['3 soatlik harorat'][times]['harorat']}C
            havo: {weather[0][0]['bugun'][1]['3 soatlik harorat'][times]['havo']}
            shamol tezligi: {weather[0][0]['bugun'][1]['3 soatlik harorat'][times]['shamol tezligi']}
            yog'ingarchilik: {weather[0][0]['bugun'][1]['3 soatlik harorat'][times]["yog'ingarchilik"]}
            namlik: {weather[0][0]['bugun'][1]['3 soatlik harorat'][times]['namlik']}
            yomg'ir yog'ish ehtimoli: {weather[0][0]['bugun'][1]['3 soatlik harorat'][times]["yomg'ir yog'ish ehtimoli"]}
        """)
    elif call.data == "three":
        times = "03:00"
    elif call.data == "six":
        times = "06:00"
    elif call.data == "nine":
        times = "09:00"
    elif call.data == "twelve":
        times = "12:00"
    elif call.data == "fiveteen":
        times = "15:00"
    elif call.data == "eighteen":
        times = "18:00"
    elif call.data == "twentyone":
        times = "21:00"
    elif call.data == "twentyfour":
        times = "24:00"
        
print("matched")
@router.message(lambda call: True)
async def answer(call: types.CallbackQuery):
    print("matched")
    city = call.data
    place['place'] = city
    await call.message.answer("vaqtni tanlang", reply_markup=times)

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