from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import logging
import asyncio
from weather import UzbekistanWeather
from keyboards import cities_button, more_info
from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher()

@dp.startup()
async def startup(bot: Bot):
    await bot.send_message(os.getenv("TELEGRAM_ID"), "Bot ishga tushdi")

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}\nmen ob havo malumotlarini berivchi botman\no'z hududingizni tanlang", reply_markup=cities_button)

@dp.callback_query(lambda call: call.data != 'get_more_info')
async def CallBackQuery(call: types.CallbackQuery):
    global city
    city = call.data
    max_weather = UzbekistanWeather(call.data).today()[0]['bugun'][0]['harorat'][1]['max']
    min_weather = UzbekistanWeather(call.data).today()[0]['bugun'][0]['harorat'][0]['min']
    await call.message.answer(f"bugungi {call.data} ob havosi: \n\teng baland harorat: {max_weather}\n\teng past harorat: {min_weather}", reply_markup=more_info)
    await call.answer(cache_time=60)

@dp.callback_query(lambda call: call.data == 'get_more_info')
async def CallbackQUery2(call: types.CallbackQuery):
    await call.message.answer(
        f"""Soat 00:00da:\n\t\t
            {UzbekistanWeather(city).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['harorat']}\n
        Soat 03:00da: {UzbekistanWeather(city).today()[0]['bugun'][1]['3 soatlik harorat']['03:00']}\n
        Soat 06:00da: {UzbekistanWeather(city).today()[0]['bugun'][1]['3 soatlik harorat']['06:00']}\n
        Soat 09:00da: {UzbekistanWeather(city).today()[0]['bugun'][1]['3 soatlik harorat']['09:00']}\n
        Soat 12:00da: {UzbekistanWeather(city).today()[0]['bugun'][1]['3 soatlik harorat']['12:00']}\n
        Soat 15:00da: {UzbekistanWeather(city).today()[0]['bugun'][1]['3 soatlik harorat']['15:00']}\n
        Soat 18:00da: {UzbekistanWeather(city).today()[0]['bugun'][1]['3 soatlik harorat']['18:00']}\n
        Soat 21:00da: {UzbekistanWeather(city).today()[0]['bugun'][1]['3 soatlik harorat']['21:00']}\n"""
    )
    await call.answer(cache_time=60)

@dp.shutdown()
async def shutdown():
    await bot.send_message(os.getenv("TELEGRAM_ID"), "Bot to'xtadi")

async def main():

    await bot.set_my_commands([
        types.BotCommand(command="start", description="botni ishga tushirish")
    ])
    await dp.start_polling(bot)


logging.basicConfig(level=logging.INFO)
asyncio.run(main())