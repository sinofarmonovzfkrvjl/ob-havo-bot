from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import logging
import asyncio
from weather import UzbekistanWeather
from keyboards import cities_button
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

@dp.callback_query()
async def CallBack(call: types.CallbackQuery):
    max_weather = UzbekistanWeather(call.data).today()['bugun'][0]['harorat'][0]['max']
    min_weather = UzbekistanWeather(call.data).today()['bugun'][0]['harorat'][0]['min']

    await call.message.answer(
        f"bugungi {call.data} ob haodi: \n\teng baland harorat: {max_weather}\n\teng past harorat: {min_weather}",
    )
    # if call.data == "toshkent":
    #     await call.message.answer(f"bugun toshkentda ob havo harorati {UzbekistanWeather('toshkent').toshkent()} bo'lishi kutilmoqda")
    # elif call.data == "andijon":
    #     await call.message.answer(f"bugun Andijon ob havo harorati {UzbekistanWeather('andijon').today()} bo'lishi kutilmoqda")
    # elif call.data == "buxoro":
    #     await call.message.answer(f"bugun Buxoro ob havo harorati {UzbekistanWeather('buxoro').today()} bo'lishi kutilmoqda")
    # elif call.data == "guliston":
    #     await call.message.answer(f"bugun Guliston ob havo harorati {UzbekistanWeather('guliston').today()} bo'lishi kutilmoqda")
    # elif call.data == "jizzax":
    #     await call.message.answer(f"bugun Jizzax ob havo harorati {UzbekistanWeather('jizzax').today()} bo'lishi kutilmoqda")
    # elif call.data == "zarafshon":
    #     await call.message.answer(f"bugun Zarafshon ob havo harorati {UzbekistanWeather('zarafshon').today()} bo'lishi kutilmoqda")
    # elif call.data == "qarshi":
    #     await call.message.answer(f"bugun Qarshi ob havo harorati {UzbekistanWeather('qarshi').today()} bo'lishi kutilmoqda")
    # elif call.data == "navoiy":
    #     await call.message.answer(f"bugun Navoiy ob havo harorati {UzbekistanWeather('navoiy').today()} bo'lishi kutilmoqda")
    # elif call.data == "namangan":
    #     await call.message.answer(f"bugun Namangan ob havo harorati {UzbekistanWeather('namangan').today()} bo'lishi kutilmoqda")
    # elif call.data == "nukus":
    #     await call.message.answer(f"bugun Nukus ob havo harorati {UzbekistanWeather('nukus').today()} bo'lishi kutilmoqda")
    # elif call.data == "samarqand":
    #     await call.message.answer(f"bugun Samarqand ob havo harorati {UzbekistanWeather('samarqand').today()} bo'lishi kutilmoqda")
    # elif call.data == "termiz":
    #     await call.message.answer(f"bugun Termiz ob havo harorati {UzbekistanWeather('termiz').today()} bo'lishi kutilmoqda")
    # elif call.data == "urganch":
    #     await call.message.answer(f"bugun Urganch ob havo harorati {UzbekistanWeather('urganch').today()} bo'lishi kutilmoqda")
    # elif call.data == "farg'ona":
    #     fargona = UzbekistanWeather('farg\'ona').today()
    #     await call.message.answer(f"bugun Farg'ona ob havo harorati {fargona} bo'lishi kutilmoqda")
    # elif call.data == "xiva":
    #     await call.message.answer(f"bugun Xiva ob havo harorati {UzbekistanWeather('xiva').today()} bo'lishi kutilmoqda")
    await call.answer("")

@dp.shutdown()
async def shutdown():
    await bot.send_message(os.getenv("TELEGRAM_ID"), "Bot to'xtadi")

async def main():
    await dp.start_polling(bot)


logging.basicConfig(level=logging.INFO)
asyncio.run(main())