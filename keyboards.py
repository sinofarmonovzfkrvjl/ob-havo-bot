from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

cities_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Toshkent", callback_data='toshkent'), InlineKeyboardButton(text="Andijon", callback_data="andijon")],
        [InlineKeyboardButton(text="Buxoro", callback_data='buxoro'), InlineKeyboardButton(text="Guliston", callback_data="guliston")],
        [InlineKeyboardButton(text="Jizzax", callback_data='jizzax'), InlineKeyboardButton(text="Zarafshon", callback_data="zarafshon")],
        [InlineKeyboardButton(text="Qarshi", callback_data='qarshi'), InlineKeyboardButton(text="Navoiy", callback_data="navoiy")],
        [InlineKeyboardButton(text="Namangan", callback_data='namangan'), InlineKeyboardButton(text="Nukus", callback_data="nukus")],
        [InlineKeyboardButton(text="Samarqand", callback_data='samarqand'), InlineKeyboardButton(text="Termiz", callback_data="termiz")],
        [InlineKeyboardButton(text="Farg'ona", callback_data="farg'ona"), InlineKeyboardButton(text="xiva", callback_data="xiva")]
    ]
)

more_info = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="ko'proq ma'lumot olish", callback_data="get_more_info")]
])