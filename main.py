from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import CommandStart
import logging
import asyncio
from uzbekistanweather import UzbekistanWeather
from keyboards import cities_button, more_info, hours_btn
from dotenv import load_dotenv
import os
import time

load_dotenv()
bot = Bot(os.getenv("TOKEN"))
router = Router()

@router.startup()
async def startup(bot: Bot):
    await bot.send_message(os.getenv("TELEGRAM_ID"), "Bot ishga tushdi")

@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}\nmen ob havo malumotlarini berivchi botman\no'z hududingizni tanlang", reply_markup=cities_button)

@router.callback_query(lambda call: call.data != 'get_more_info')
async def CallBackQuery(call: types.CallbackQuery):
    timess = ["00:00", "03:00", "06:00", "09:00", "12:00", "15:00", "18:00", "21:00"]
    for times in timess:
        await call.message.answer(f"""
            soat {times} da:
                harorat: {UzbekistanWeather(call.data).today()[0]['bugun'][1]['3 soatlik harorat'][times]['harorat']}C
                havo: {UzbekistanWeather(call.data).today()[0]['bugun'][1]['3 soatlik harorat'][times]['havo']}
                shamol tezligi: {UzbekistanWeather(call.data).today()[0]['bugun'][1]['3 soatlik harorat'][times]['shamol tezligi']}
                yog'ingarchilik: {UzbekistanWeather(call.data).today()[0]['bugun'][1]['3 soatlik harorat'][times]["yog'ingarchilik"]}
                namlik: {UzbekistanWeather(call.data).today()[0]['bugun'][1]['3 soatlik harorat'][times]['namlik']}
                yomg'ir yog'ish ehtimoli: {UzbekistanWeather(call.data).today()[0]['bugun'][1]['3 soatlik harorat'][times]["yomg'ir yog'ish ehtimoli"]}
        """)
        await call.answer(cache_time=60)
        time.sleep(1)

@router.callback_query(lambda call: call.data == 'get_more_info')
async def CallbackQUery2(call: types.CallbackQuery):
    await call.message.answer("vaqtni tanlang", reply_markup=hours_btn)
    await call.answer(cache_time=60)

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