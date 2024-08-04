from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import CommandStart
import logging
import asyncio
from weather import UzbekistanWeather
from keyboards import cities_button, more_info, hours_btn
from dotenv import load_dotenv
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
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
async def CallBackQuery(call: types.CallbackQuery, state: FS):
    open("city.txt", "w").write(call.data)
    max_weather = UzbekistanWeather(call.data).today()[0]['bugun'][0]['harorat'][1]['max']
    min_weather = UzbekistanWeather(call.data).today()[0]['bugun'][0]['harorat'][0]['min']
    await call.message.answer(f"bugungi {call.data} ob havosi: \n\teng baland harorat: {max_weather}\n\teng past harorat: {min_weather}", reply_markup=more_info)
    await call.answer(cache_time=60)

@router.message(lambda hours: hours.data == ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00'])
async def hours_info(call: types.CallbackQuery):
    print(open("city.txt", "r").read())
    if call.data == "00:00":
        await call.message.answer(
            f"""harorat: {UzbekistanWeather(str(str(open("city.txt", "r").read()))).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['harorat']}"""
            f"""havo: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['havo']}"""
            f"""shamol tezligi: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['shamol tezligi']}"""
            f"""yog'ingarchilik: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yog'ingarchilik"]}"""
            f"""namlik: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['namlik']}"""
            f"""yomg'ir yog'ish ehtimoli: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yomg'ir yog'ish ehtimoli"]}"""
        )
    elif call.data == "03:00":
        await call.message.answer(
            f"""harorat: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['harorat']}"""
            f"""havo: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['havo']}"""
            f"""shamol tezligi: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['shamol tezligi']}"""
            f"""yog'ingarchilik: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yog'ingarchilik"]}"""
            f"""namlik: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['namlik']}"""
            f"""yomg'ir yog'ish ehtimoli: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yomg'ir yog'ish ehtimoli"]}"""
        )
    elif call.data == "06:00":
        await call.message.answer(
            f"""harorat: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['harorat']}"""
            f"""havo: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['havo']}"""
            f"""shamol tezligi: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['shamol tezligi']}"""
            f"""yog'ingarchilik: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yog'ingarchilik"]}"""""
            f"""namlik: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['namlik']}"""
            f"""yomg'ir yog'ish ehtimoli: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yomg'ir yog'ish ehtimoli"]}"""
        )
    elif call.data == "09:00":
        await call.message.answer(
            f"""harorat: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['harorat']}"""
            f"""havo: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['havo']}"""
            f"""shamol tezligi: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['shamol tezligi']}"""
            f"""yog'ingarchilik: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yog'ingarchilik"]}"""
            f"""namlik: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['namlik']}"""
            f"""yomg'ir yog'ish ehtimoli: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yomg'ir yog'ish ehtimoli"]}"""
        )
    elif call.data == "12:00":
        await call.message.answer(
            f"""harorat: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['harorat']}"""
            f"""havo: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['havo']}"""
            f"""shamol tezligi: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['shamol tezligi']}"""
            f"""yog'ingarchilik: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yog'ingarchilik"]}"""
            f"""namlik: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['namlik']}"""
            f"""yomg'ir yog'ish ehtimoli: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yomg'ir yog'ish ehtimoli"]}"""
        )
    elif call.data == "15:00":
        await call.message.answer(
            f"""harorat: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['harorat']}"""
            f"""havo: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['havo']}"""
            f"""shamol tezligi: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['shamol tezligi']}"""
            f"""yog'ingarchilik: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yog'ingarchilik"]}"""
            f"""namlik: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['namlik']}"""
            f"""yomg'ir yog'ish ehtimoli: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yomg'ir yog'ish ehtimoli"]}"""
        )
    elif call.data == "18:00":
        await call.message.answer(
            f"""harorat: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['harorat']}"""
            f"""havo: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['havo']}"""
            f"""shamol tezligi: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['shamol tezligi']}"""
            f"""yog'ingarchilik: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yog'ingarchilik"]}"""
            f"""namlik: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['namlik']}"""
            f"""yomg'ir yog'ish ehtimoli: {UzbekistanWeather(str(open("city.txt", "r").read())).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yomg'ir yog'ish ehtimoli"]}"""
        )
    elif call.data == "21:00":
        await call.message.answer(
            f"""harorat: {UzbekistanWeather(open("city.txt", "r").read()).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['harorat']}"""
            f"""havo: {UzbekistanWeather(open("city.txt", "r").read()).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['havo']}"""
            f"""shamol tezligi: {UzbekistanWeather(open("city.txt", "r").read()).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['shamol tezligi']}"""
            f"""yog'ingarchilik: {UzbekistanWeather(open("city.txt", "r").read()).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yog'ingarchilik"]}"""
            f"""namlik: {UzbekistanWeather(open("city.txt", "r").read()).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']['namlik']}"""
            f"""yomg'ir yog'ish ehtimoli: {UzbekistanWeather(open("city.txt", "r").read()).today()[0]['bugun'][1]['3 soatlik harorat']['00:00']["yomg'ir yog'ish ehtimoli"]}"""
        )

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