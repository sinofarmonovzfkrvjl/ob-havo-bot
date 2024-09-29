from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import CommandStart
import logging
import asyncio
from keyboards import cities_button, times
from dotenv import load_dotenv
import os
from uzbekistanweather import UzbekistanWeather
from keep_alive import keep_alive

place = {'place': None}

keep_alive()

load_dotenv()

bot = Bot(os.getenv("TOKEN"))
router = Router()

@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}\nmen ob havo malumotlarini berivchi botman\no'z hududingizni tanlang", reply_markup=cities_button)

@router.callback_query(lambda call: call.data in ['toshkent', 'andijon', 'buxoro', 'guliston', 'jizzax', 'zarafshon', 'qarshi', 'navoiy', 'namangan', 'nukus', 'samarqand', 'termiz', 'farg\'ona', 'xiva', 'angren', 'baliqchi', 'sirdaryo', 'qashqadaryo', 'bekobod', 'bog\'ot', 'bulung\'ur', 'denov', 'chiroqchi', 'dehqonobod', 'ishtixon', 'jondor', 'kitob', 'kokand', 'koson', 'marg\'ilon', 'nurobod', 'olmaliq', 'oltiariq', 'ontinsoy', 'oqtosh', 'parkent', 'payariq', 'qamashi', 'qumqo\'rg\'on', 'qo\'qon', 'quva', 'rishton', 'romitan', 'shahrisabz', 'sherobod', 'shofirkon', 'shovot', 'kitob', 'uchquduq', 'urgut', 'urganch'])
async def send_times_button(call: types.CallbackQuery):
    city = call.data
    place['place'] = city
    await call.message.answer("vaqtni tanlang", reply_markup=times)
    await call.answer(cache_time=10)

@router.callback_query(lambda call: call.data in ["zero", "three", "six", "nine", "twelve", "fiveteen", "eighteen", "twentyone", "twentyfour"])
async def send_city_button(call: types.CallbackQuery):
    weather = UzbekistanWeather(place=place['place']).today()
    if call.data == "zero":
        await call.message.answer(f"""
Toshkent
harorat: {weather[0][0]['bugun'][1]['3 soatlik harorat']["00:00"]['harorat']}C
havo: {weather[0][0]['bugun'][1]['3 soatlik harorat']["00:00"]['havo']}
shamol tezligi: {weather[0][0]['bugun'][1]['3 soatlik harorat']["00:00"]['shamol tezligi']}
yog'ingarchilik: {weather[0][0]['bugun'][1]['3 soatlik harorat']["00:00"]["yog'ingarchilik"]}
namlik: {weather[0][0]['bugun'][1]['3 soatlik harorat']["00:00"]['namlik']}
yomg'ir yog'ish ehtimoli: {weather[0][0]['bugun'][1]['3 soatlik harorat']["00:00"]["yomg'ir yog'ish ehtimoli"]}
kiyimlarga oid tavfsiyalar: {weather[0][0]['bugun'][2]['kiyimlarga oid tavfsiyalar'][0]}, {weather[0][0]['bugun'][2]['kiyimlarga oid tavfsiyalar'][1]}
""")
    elif call.data == "three":
        await call.message.answer(f"""
Toshkent:
harorat: {weather[0][0]['bugun'][1]['3 soatlik harorat']["03:00"]['harorat']}C
havo: {weather[0][0]['bugun'][1]['3 soatlik harorat']["03:00"]['havo']}
shamol tezligi: {weather[0][0]['bugun'][1]['3 soatlik harorat']["03:00"]['shamol tezligi']}
yog'ingarchilik: {weather[0][0]['bugun'][1]['3 soatlik harorat']["03:00"]["yog'ingarchilik"]}
namlik: {weather[0][0]['bugun'][1]['3 soatlik harorat']["03:00"]['namlik']}
yomg'ir yog'ish ehtimoli: {weather[0][0]['bugun'][1]['3 soatlik harorat']["03:00"]["yomg'ir yog'ish ehtimoli"]}
kiyimlarga oid tavfsiyalar: {weather[0][0]['bugun'][2]['kiyimlarga oid tavfsiyalar'][0]}, {weather[0][0]['bugun'][2]['kiyimlarga oid tavfsiyalar'][1]}
""")
    elif call.data == "six":
        await call.message.answer(f"""
Toshkent:
harorat: {weather[0][0]['bugun'][1]['3 soatlik harorat']["06:00"]['harorat']}C
havo: {weather[0][0]['bugun'][1]['3 soatlik harorat']["06:00"]['havo']}
shamol tezligi: {weather[0][0]['bugun'][1]['3 soatlik harorat']["06:00"]['shamol tezligi']}
yog'ingarchilik: {weather[0][0]['bugun'][1]['3 soatlik harorat']["06:00"]["yog'ingarchilik"]}
namlik: {weather[0][0]['bugun'][1]['3 soatlik harorat']["06:00"]['namlik']}
yomg'ir yog'ish ehtimoli: {weather[0][0]['bugun'][1]['3 soatlik harorat']["06:00"]["yomg'ir yog'ish ehtimoli"]}
kiyimlarga oid tavfsiyalar: {weather[0][0]['bugun'][2]['kiyimlarga oid tavfsiyalar'][0]}, {weather[0][0]['bugun'][2]['kiyimlarga oid tavfsiyalar'][1]}
""")
    elif call.data == "nine":
        await call.message.answer(f"""
Toshkent:
harorat: {weather[0][0]['bugun'][1]['3 soatlik harorat']["09:00"]['harorat']}C
havo: {weather[0][0]['bugun'][1]['3 soatlik harorat']["09:00"]['havo']}
shamol tezligi: {weather[0][0]['bugun'][1]['3 soatlik harorat']["09:00"]['shamol tezligi']}
yog'ingarchilik: {weather[0][0]['bugun'][1]['3 soatlik harorat']["09:00"]["yog'ingarchilik"]}
namlik: {weather[0][0]['bugun'][1]['3 soatlik harorat']["09:00"]['namlik']}
yomg'ir yog'ish ehtimoli: {weather[0][0]['bugun'][1]['3 soatlik harorat']["09:00"]["yomg'ir yog'ish ehtimoli"]}
kiyimlarga oid tavfsiyalar: {weather[0][0]['bugun'][2]['kiyimlarga oid tavfsiyalar'][0]}, {weather[0][0]['bugun'][2]['kiyimlarga oid tavfsiyalar'][1]}
""")
    elif call.data == "twelve":
        await call.message.answer(f"""
Toshkent:
harorat: {weather[0][0]['bugun'][1]['3 soatlik harorat']["12:00"]['harorat']}C
havo: {weather[0][0]['bugun'][1]['3 soatlik harorat']["12:00"]['havo']}
shamol tezligi: {weather[0][0]['bugun'][1]['3 soatlik harorat']["12:00"]['shamol tezligi']}
yog'ingarchilik: {weather[0][0]['bugun'][1]['3 soatlik harorat']["12:00"]["yog'ingarchilik"]}
namlik: {weather[0][0]['bugun'][1]['3 soatlik harorat']["12:00"]['namlik']}
yomg'ir yog'ish ehtimoli: {weather[0][0]['bugun'][1]['3 soatlik harorat']["12:00"]["yomg'ir yog'ish ehtimoli"]}
kiyimlarga oid tavfsiyalar: {weather[0][0]['bugun'][2]['kiyimlarga oid tavfsiyalar'][0]}, {weather[0][0]['bugun'][2]['kiyimlarga oid tavfsiyalar'][1]}""")
    elif call.data == "fiveteen":
        await call.message.answer(f"""
Toshkent:
harorat: {weather[0][0]['bugun'][1]['3 soatlik harorat']["15:00"]['harorat']}C
havo: {weather[0][0]['bugun'][1]['3 soatlik harorat']["15:00"]['havo']}
shamol tezligi: {weather[0][0]['bugun'][1]['3 soatlik harorat']["15:00"]['shamol tezligi']}
yog'ingarchilik: {weather[0][0]['bugun'][1]['3 soatlik harorat']["15:00"]["yog'ingarchilik"]}
namlik: {weather[0][0]['bugun'][1]['3 soatlik harorat']["15:00"]['namlik']}
yomg'ir yog'ish ehtimoli: {weather[0][0]['bugun'][1]['3 soatlik harorat']["15:00"]["yomg'ir yog'ish ehtimoli"]}
kiyimlarga oid tavfsiyalar: {weather[0][0]['bugun'][2]['kiyimlarga oid tavfsiyalar'][0]}, {weather[0][0]['bugun'][2]['kiyimlarga oid tavfsiyalar'][1]}""")
    elif call.data == "eighteen":
        await call.message.answer(f"""
Toshkent:
harorat: {weather[0][0]['bugun'][1]['3 soatlik harorat']["18:00"]['harorat']}C
havo: {weather[0][0]['bugun'][1]['3 soatlik harorat']["18:00"]['havo']}
shamol tezligi: {weather[0][0]['bugun'][1]['3 soatlik harorat']["18:00"]['shamol tezligi']}
yog'ingarchilik: {weather[0][0]['bugun'][1]['3 soatlik harorat']["18:00"]["yog'ingarchilik"]}
namlik: {weather[0][0]['bugun'][1]['3 soatlik harorat']["18:00"]['namlik']}
yomg'ir yog'ish ehtimoli: {weather[0][0]['bugun'][1]['3 soatlik harorat']["18:00"]["yomg'ir yog'ish ehtimoli"]}
kiyimlarga oid tavfsiyalar: {weather[0][0]['bugun'][2]['kiyimlarga oid tavfsiyalar'][0]}, {weather[0][0]['bugun'][2]['kiyimlarga oid tavfsiyalar'][1]}
""")
    elif call.data == "twentyone":
        await call.message.answer(f"""
Toshkent:
harorat: {weather[0][0]['bugun'][1]['3 soatlik harorat']["21:00"]['harorat']}C
havo: {weather[0][0]['bugun'][1]['3 soatlik harorat']["21:00"]['havo']}
shamol tezligi: {weather[0][0]['bugun'][1]['3 soatlik harorat']["21:00"]['shamol tezligi']}
yog'ingarchilik: {weather[0][0]['bugun'][1]['3 soatlik harorat']["21:00"]["yog'ingarchilik"]}
namlik: {weather[0][0]['bugun'][1]['3 soatlik harorat']["21:00"]['namlik']}
yomg'ir yog'ish ehtimoli: {weather[0][0]['bugun'][1]['3 soatlik harorat']["21:00"]["yomg'ir yog'ish ehtimoli"]}
kiyimlarga oid tavfsiyalar: {weather[0][0]['bugun'][2]['kiyimlarga oid tavfsiyalar'][0]}, {weather[0][0]['bugun'][2]['kiyimlarga oid tavfsiyalar'][1]}
""")
    elif call.data == "twentyfour":
        await call.message.answer(f"""
Toshkent:
harorat: {weather[0][0]['bugun'][1]['3 soatlik harorat']["24:00"]['harorat']}C
havo: {weather[0][0]['bugun'][1]['3 soatlik harorat']["24:00"]['havo']}
shamol tezligi: {weather[0][0]['bugun'][1]['3 soatlik harorat']["24:00"]['shamol tezligi']}
yog'ingarchilik: {weather[0][0]['bugun'][1]['3 soatlik harorat']["24:00"]["yog'ingarchilik"]}
namlik: {weather[0][0]['bugun'][1]['3 soatlik harorat']["24:00"]['namlik']}
yomg'ir yog'ish ehtimoli: {weather[0][0]['bugun'][1]['3 soatlik harorat']["24:00"]["yomg'ir yog'ish ehtimoli"]}
kiyimlarga oid tavfsiyalar: {weather[0][0]['bugun'][2]['kiyimlarga oid tavfsiyalar'][0]}, {weather[0][0]['bugun'][2]['kiyimlarga oid tavfsiyalar'][1]}
""")
    await call.answer(cache_time=10)

async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="botni ishga tushirish")
    ])

    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


logging.basicConfig(level=logging.INFO)
asyncio.run(main())