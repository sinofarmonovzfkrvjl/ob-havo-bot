from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

cities_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Toshkent", callback_data='toshkent'), InlineKeyboardButton(text="Andijon", callback_data="andijon")],
        [InlineKeyboardButton(text="Buxoro", callback_data='buxoro'), InlineKeyboardButton(text="Guliston", callback_data="guliston")],
        [InlineKeyboardButton(text="Jizzax", callback_data='jizzax'), InlineKeyboardButton(text="zarafshon", callback_data="zarafshon")],
        [InlineKeyboardButton(text="Qarshi", callback_data='qarshi'), InlineKeyboardButton(text="Navoiy", callback_data="navoiy")],
        [InlineKeyboardButton(text="Namangan", callback_data='namangan'), InlineKeyboardButton(text="Nukus", callback_data="nukus")],
        [InlineKeyboardButton(text="Samarqand", callback_data='samarqand'), InlineKeyboardButton(text="Termiz", callback_data="termiz")],
        [InlineKeyboardButton(text="Farg'ona", callback_data="farg'ona"), InlineKeyboardButton(text="xiva", callback_data="xiva")]
    ]
)

more_info = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="ko'proq ma'lumot olish", callback_data="get_more_info")]
])

hours_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="00:00", callback_data="00:00"), InlineKeyboardButton(text="03:00", callback_data="03:00")],
    [InlineKeyboardButton(text="06:00", callback_data="06:00"), InlineKeyboardButton(text="09:00", callback_data="09:00")],
    [InlineKeyboardButton(text="12:00", callback_data="12:00"), InlineKeyboardButton(text="15:00", callback_data="15:00")],
    [InlineKeyboardButton(text="18:00", callback_data="18:00"), InlineKeyboardButton(text="21:00", callback_data="21:00")]
])

for time in ["00:00", "03:00", "06:00", "09:00", "12:00", "15:00", "18:00", "21:00"]:
    print(time)