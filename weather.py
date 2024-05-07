import requests
from bs4 import BeautifulSoup

class WeatherNotFoundError(Exception):
    """
    Weather not found, make sure you write the city name correctly, use Weather().help()
    """

class Weather:
    def __init__(self, place):
        self.place: str = place

    def help(self):
        return """Siz mana bu shaharlarni ob havo malumotlarini ko'rishingiz mumkin:
    toshkent, andijon, buxoro, guliston, jizzax, zarafshon, qarshi, navoiy, namangan, nukus, samarqand, termiz, urganch, farg'ona, xiva
        """

    def today(self):
        if self.place.lower() == "toshkent":
            response = requests.get(f"https://obhavo.uz/tashkent")
        elif self.place.lower() == "andijon":
            response = requests.get(f"https://obhavo.uz/andijan")
        elif self.place.lower() == "buxoro":
            response = requests.get(f"https://obhavo.uz/bukhara")
        elif self.place.lower() == "guliston":
            response = requests.get(f"https://obhavo.uz/gulistan")
        elif self.place.lower() == "jizzax":
            response = requests.get(f"https://obhavo.uz/jizzakh")
        elif self.place.lower() == "zarafshon":
            response = requests.get(f"https://obhavo.uz/zarafshan")
        elif self.place.lower() == "qarshi":
            response = requests.get(f"https://obhavo.uz/karshi")
        elif self.place.lower() == "navoiy":
            response = requests.get(f"https://obhavo.uz/navoi")
        elif self.place.lower() == "namangan":
            response = requests.get(f"https://obhavo.uz/namangan")
        elif self.place.lower() == "nukus":
            response = requests.get(f"https://obhavo.uz/nukus")
        elif self.place.lower() == "samarqand":
            response = requests.get(f"https://obhavo.uz/samarkand")
        elif self.place.lower() == "termiz":
            response = requests.get(f"https://obhavo.uz/termez")
        elif self.place.lower() == "urganch":
            response = requests.get(f"https://obhavo.uz/urgench")
        elif self.place.lower() == "farg'ona":
            response = requests.get(f"https://obhavo.uz/ferghana")
        elif self.place.lower() == "xiva":
            response = requests.get(f"https://obhavo.uz/khiva")
        else:
            raise WeatherNotFoundError("Ob Havo malumoti topilmadi, shahar nomini to'g'ri yozganingiznga ishonch hosil qiling, yoki Weather().help() dan foydalaning")
        soup = BeautifulSoup(response.content, 'html.parser')
        data = soup.find_all("span")
        return f"ertalab {data[2].text}, kechqurun: {data[3].text}"