from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import CommandStart
import logging
import asyncio
from uzbekistanweather import UzbekistanWeather
from keyboards import cities_button, more_info, hours_btn
from dotenv import load_dotenv
import os

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
    for time in ["00:00", "03:00", "06:00", "09:00", "12:00", "15:00", "18:00", "21:00"]:
        await call.message.answer(
            f"""harorat: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat'][time]['harorat']}"""
            f"""havo: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat'][time]['havo']}"""
            f"""shamol tezligi: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat'][time]['shamol tezligi']}"""
            f"""yog'ingarchilik: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat'][time]["yog'ingarchilik"]}"""
            f"""namlik: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat'][time]['namlik']}"""
            f"""yomg'ir yog'ish ehtimoli: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat'][time]["yomg'ir yog'ish ehtimoli"]}"""
        )
    # "Soat "
    # f"""harorat: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['harorat']}"""
    # f"""havo: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['havo']}"""
    # f"""shamol tezligi: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['shamol tezligi']}"""
    # f"""yog'ingarchilik: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yog'ingarchilik"]}"""
    # f"""namlik: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['namlik']}"""
    # f"""yomg'ir yog'ish ehtimoli: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yomg'ir yog'ish ehtimoli"]}"""

    # f"""harorat: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['harorat']}"""
    # f"""havo: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['havo']}"""
    # f"""shamol tezligi: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['shamol tezligi']}"""
    # f"""yog'ingarchilik: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yog'ingarchilik"]}"""
    # f"""namlik: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['namlik']}"""
    # f"""yomg'ir yog'ish ehtimoli: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yomg'ir yog'ish ehtimoli"]}"""

    # f"""harorat: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['harorat']}"""
    # f"""havo: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['havo']}"""
    # f"""shamol tezligi: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['shamol tezligi']}"""
    # f"""yog'ingarchilik: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yog'ingarchilik"]}"""""
    # f"""namlik: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['namlik']}"""
    # f"""yomg'ir yog'ish ehtimoli: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yomg'ir yog'ish ehtimoli"]}"""

    # f"""harorat: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['harorat']}"""
    # f"""havo: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['havo']}"""
    # f"""shamol tezligi: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['shamol tezligi']}"""
    # f"""yog'ingarchilik: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yog'ingarchilik"]}"""
    # f"""namlik: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['namlik']}"""
    # f"""yomg'ir yog'ish ehtimoli: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yomg'ir yog'ish ehtimoli"]}"""

    # f"""harorat: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['harorat']}"""
    # f"""havo: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['havo']}"""
    # f"""shamol tezligi: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['shamol tezligi']}"""
    # f"""yog'ingarchilik: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yog'ingarchilik"]}"""
    # f"""namlik: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['namlik']}"""
    # f"""yomg'ir yog'ish ehtimoli: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yomg'ir yog'ish ehtimoli"]}"""
    
    # f"""harorat: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['harorat']}"""
    # f"""havo: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['havo']}"""
    # f"""shamol tezligi: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['shamol tezligi']}"""
    # f"""yog'ingarchilik: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yog'ingarchilik"]}"""
    # f"""namlik: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['namlik']}"""
    # f"""yomg'ir yog'ish ehtimoli: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yomg'ir yog'ish ehtimoli"]}"""

    # f"""harorat: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['harorat']}"""
    # f"""havo: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['havo']}"""
    # f"""shamol tezligi: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['shamol tezligi']}"""
    # f"""yog'ingarchilik: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yog'ingarchilik"]}"""
    # f"""namlik: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['namlik']}"""
    # f"""yomg'ir yog'ish ehtimoli: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yomg'ir yog'ish ehtimoli"]}"""

    # f"""harorat: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['harorat']}"""
    # f"""havo: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['havo']}"""
    # f"""shamol tezligi: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['shamol tezligi']}"""
    # f"""yog'ingarchilik: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yog'ingarchilik"]}"""
    # f"""namlik: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['namlik']}"""
    # f"""yomg'ir yog'ish ehtimoli: {UzbekistanWeather().today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yomg'ir yog'ish ehtimoli"]}"""
    

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