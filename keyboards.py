from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

cities_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Toshkent", callback_data='toshkent'), InlineKeyboardButton(text="Andijon", callback_data="andijon"), InlineKeyboardButton(text="Buxoro", callback_data='buxoro')],
        [InlineKeyboardButton(text="Guliston", callback_data="guliston"), InlineKeyboardButton(text="Jizzax", callback_data='jizzax'), InlineKeyboardButton(text="zarafshon", callback_data="zarafshon")],
        [InlineKeyboardButton(text="Qarshi", callback_data='qarshi'), InlineKeyboardButton(text="Navoiy", callback_data="navoiy"), InlineKeyboardButton(text="Namangan", callback_data='namangan')],
        [InlineKeyboardButton(text="Nukus", callback_data="nukus"), InlineKeyboardButton(text="Samarqand", callback_data='samarqand'), InlineKeyboardButton(text="Termiz", callback_data="termiz")],
        [InlineKeyboardButton(text="Farg'ona", callback_data="farg'ona"), InlineKeyboardButton(text="xiva", callback_data="xiva"), InlineKeyboardButton(text="Angren", callback_data="angren")],
        [InlineKeyboardButton(text="Baliqchi", callback_data="baliqchi"), InlineKeyboardButton(text="Sirdaryo", callback_data="sirdaryo"), InlineKeyboardButton(text="Qashqadaryo", callback_data="qashqadaryo")],
        [InlineKeyboardButton(text="Bekobod", callback_data="bekobod"), InlineKeyboardButton(text="Bog'ot", callback_data="bog'ot"), InlineKeyboardButton(text="bulung'ur", callback_data="bulung'ur")],
        [InlineKeyboardButton(text="Denov", callback_data="denov"), InlineKeyboardButton(text="Chiroqchi", callback_data="chiroqchi"), InlineKeyboardButton(text="Dehqonobod", callback_data="dehqonobod")],
        [InlineKeyboardButton(text="Ishtixon", callback_data="ishtixon"), InlineKeyboardButton(text="Jondor", callback_data="jondor"), InlineKeyboardButton(text="Kitob", callback_data="kitob")],
        [InlineKeyboardButton(text="Kokand", callback_data="kokand"), InlineKeyboardButton(text="Koson", callback_data="koson"), InlineKeyboardButton(text="Marg'ilon", callback_data="marg'ilon")],
        [InlineKeyboardButton(text="Nurobod", callback_data="nurobod"), InlineKeyboardButton(text="Olmaliq", callback_data="olmaliq"), InlineKeyboardButton(text="Oltiariq", callback_data="oltiariq")],
        [InlineKeyboardButton(text="Oltinsoy", callback_data="ontinsoy"), InlineKeyboardButton(text="oqtosh", callback_data="oqtosh"), InlineKeyboardButton(text="parkent", callback_data="parkent")],
        [InlineKeyboardButton(text="payariq", callback_data="payariq"), InlineKeyboardButton(text="Qamashi", callback_data="qamashi"), InlineKeyboardButton(text="Qumqo'rg'on", callback_data="qumqo'rg'on")],
        [InlineKeyboardButton(text="Qo'qon", callback_data="qo'qon"), InlineKeyboardButton(text="Quva", callback_data="quva"), InlineKeyboardButton(text="Rishton", callback_data="rishton")],
        [InlineKeyboardButton(text="Romitan", callback_data="romitan"), InlineKeyboardButton(text="Shahrisabz", callback_data="shahrisabz"), InlineKeyboardButton(text="sherobod", callback_data="sherobod")],
        [InlineKeyboardButton(text="Shofirkon", callback_data="shofirkon"), InlineKeyboardButton(text="Shovot", callback_data="shovot"), InlineKeyboardButton(text="Kitob", callback_data="kitob")],
        [InlineKeyboardButton(text="Uchquduq", callback_data="uchquduq"), InlineKeyboardButton(text="Urgut", callback_data="urgut"), InlineKeyboardButton(text="Urganch", callback_data="urganch")],
    ]
)