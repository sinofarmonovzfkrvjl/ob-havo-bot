from uzbekistanweather import UzbekistanWeather
import json

weather = UzbekistanWeather("toshkent").today()[0][0]['bugun'][1]['3 soatlik harorat']

print(weather)