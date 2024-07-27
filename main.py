from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import logging
import asyncio
from weather import Weather
from keyboards import cities_button

bot = Bot("5904607271:AAEDJWUULTrD3zV8HOY7JbU94aiXk5Qexno")
dp = Dispatcher()

@dp.startup()
async def startup(bot: Bot):
    await bot.send_message(5230484991, "Bot ishga tushdi")

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}\nmen ob havo malumotlarini berivchi botman\no'z hududingizni tanlang", reply_markup=cities_button)

@dp.callback_query()
async def CallBack(call: types.CallbackQuery):
    if call.data == "toshkent":
        await call.message.answer(f"bugun toshkentda ob havo harorati {Weather('toshkent').today()} bo'lishi kutilmoqda")
    elif call.data == "andijon":
        await call.message.answer(f"bugun Andijon ob havo harorati {Weather('andijon').today()} bo'lishi kutilmoqda")
    elif call.data == "buxoro":
        await call.message.answer(f"bugun Buxoro ob havo harorati {Weather('buxoro').today()} bo'lishi kutilmoqda")
    elif call.data == "guliston":
        await call.message.answer(f"bugun Guliston ob havo harorati {Weather('guliston').today()} bo'lishi kutilmoqda")
    elif call.data == "jizzax":
        await call.message.answer(f"bugun Jizzax ob havo harorati {Weather('jizzax').today()} bo'lishi kutilmoqda")
    elif call.data == "zarafshon":
        await call.message.answer(f"bugun Zarafshon ob havo harorati {Weather('zarafshon').today()} bo'lishi kutilmoqda")
    elif call.data == "qarshi":
        await call.message.answer(f"bugun Qarshi ob havo harorati {Weather('qarshi').today()} bo'lishi kutilmoqda")
    elif call.data == "navoiy":
        await call.message.answer(f"bugun Navoiy ob havo harorati {Weather('navoiy').today()} bo'lishi kutilmoqda")
    elif call.data == "namangan":
        await call.message.answer(f"bugun Namangan ob havo harorati {Weather('namangan').today()} bo'lishi kutilmoqda")
    elif call.data == "nukus":
        await call.message.answer(f"bugun Nukus ob havo harorati {Weather('nukus').today()} bo'lishi kutilmoqda")
    elif call.data == "samarqand":
        await call.message.answer(f"bugun Samarqand ob havo harorati {Weather('samarqand').today()} bo'lishi kutilmoqda")
    elif call.data == "termiz":
        await call.message.answer(f"bugun Termiz ob havo harorati {Weather('termiz').today()} bo'lishi kutilmoqda")
    elif call.data == "urganch":
        await call.message.answer(f"bugun Urganch ob havo harorati {Weather('urganch').today()} bo'lishi kutilmoqda")
    elif call.data == "farg'ona":
        fargona = Weather('farg\'ona').today()
        await call.message.answer(f"bugun Farg'ona ob havo harorati {fargona} bo'lishi kutilmoqda")
    elif call.data == "xiva":
        await call.message.answer(f"bugun Xiva ob havo harorati {Weather('xiva').today()} bo'lishi kutilmoqda")
    await call.answer("")

async def main():
    await dp.start_polling(bot)


logging.basicConfig(level=logging.INFO)
asyncio.run(main())