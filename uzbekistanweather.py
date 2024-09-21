import requests

class UzbekistanWeather:
    def __init__(self, place):
        self.place = place

    def today(self):
        response = requests.get(f"https://ob-havo-api-y572.onrender.com/api/v1/obhavo/{self.place}")
        return [response.json(), self.place]