import requests
from bs4 import BeautifulSoup


today = requests.get("https://www.ob-havo.com/asia/uzbekistan/tashkent?page=today")
todaysoup = BeautifulSoup(today.content, 'html.parser')

tomorrow = requests.get("https://www.ob-havo.com/asia/uzbekistan/tashkent?page=tomorrow")
tomorrowsoup = BeautifulSoup(tomorrow.content, 'html.parser')


class Weather:
    def __init__(self):
        pass

    def toshkent(self):
        max_middle_temp = todaysoup.find("span", {"class": "fourteen-max"})
        min_middle_temp = todaysoup.find("span", {"class": "fourteen-min"})

        necessary_things = todaysoup.find_all("span", {"class": "day-value"})
        weather = todaysoup.find_all("div", class_="weather_des")

        yogingarchilik = todaysoup.find_all("span", class_="length_unit mm_unit")

        m_taqsin_s = todaysoup.find_all("span", class_="wind_unit")

        recommended_clothes = todaysoup.find_all("div", class_="wear_item_name")

        return [{"bugun": [
                    {"harorat": [{"min": min_middle_temp.text},
                         {"max": max_middle_temp.text}]},
                    {"3 soatlik harorat": {"00:00": {"harorat": necessary_things[0].text,
                                             "havo": weather[0].text,
                                             "shamol tezligi": f"{necessary_things[32].text}{m_taqsin_s[0].text}",
                                             "yog'ingarchilik": f"{necessary_things[16].text}{yogingarchilik[0].text}",
                                             "namlik": f"{necessary_things[24].text}%",
                                             "yomg'ir yog'ish ehtimoli": f"{necessary_things[8].text}%"},
                                   "03:00": {"harorat": necessary_things[1].text,
                                             "havo": weather[1].text,
                                             "shamol tezligi": f"{necessary_things[32].text}{m_taqsin_s[1].text}",
                                             "yog'ingarchilik": f"{necessary_things[17].text}{yogingarchilik[1].text}",
                                             "namlik": f"{necessary_things[25].text}%",
                                             "yomg'ir yog'ish ehtimoli": f"{necessary_things[9].text}%"}, 
                                   "06:00": {"harorat": necessary_things[2].text,
                                             "havo": weather[2].text,
                                             "shamol tezligi": f"{necessary_things[32].text}{m_taqsin_s[2].text}",
                                             "yog'ingarchilik": f"{necessary_things[18].text}{yogingarchilik[2].text}",
                                             "namlik": f"{necessary_things[26].text}%",
                                             "yomg'ir yog'ish ehtimoli": f"{necessary_things[10].text}%"}, 
                                   "09:00": {"harorat": necessary_things[3].text,
                                             "havo": weather[3].text,
                                             "shamol tezligi": f"{necessary_things[32].text}{m_taqsin_s[3].text}",
                                             "yog'ingarchilik": f"{necessary_things[19].text}{yogingarchilik[3].text}",
                                             "namlik": f"{necessary_things[27].text}%",
                                             "yomg'ir yog'ish ehtimoli": f"{necessary_things[11].text}%"}, 
                                   "12:00": {"harorat": necessary_things[4].text,
                                             "havo": weather[4].text,
                                             "shamol tezligi": f"{necessary_things[32].text}{m_taqsin_s[4].text}",
                                             "yog'ingarchilik": f"{necessary_things[20].text}{yogingarchilik[4].text}",
                                             "namlik": f"{necessary_things[28].text}%",
                                             "yomg'ir yog'ish ehtimoli": f"{necessary_things[12].text}%"},
                                   "15:00": {"harorat": necessary_things[5].text,
                                             "havo": weather[5].text,
                                             "shamol tezligi": f"{necessary_things[32].text}{m_taqsin_s[5].text}",
                                             "yog'ingarchilik": f"{necessary_things[21].text}{yogingarchilik[5].text}",
                                             "namlik": f"{necessary_things[29].text}%",
                                             "yomg'ir yog'ish ehtimoli": f"{necessary_things[13].text}%"},
                                   "18:00": {"harorat": necessary_things[6].text,
                                             "havo": weather[6].text,
                                             "shamol tezligi": f"{necessary_things[32].text}{m_taqsin_s[5].text}",
                                             "yog'ingarchilik": f"{necessary_things[22].text}{yogingarchilik[6].text}",
                                             "namlik": f"{necessary_things[30].text}%",
                                             "yomg'ir yog'ish ehtimoli": f"{necessary_things[14].text}%"},
                                   "21:00": {"harorat": necessary_things[7].text,
                                             "havo": weather[7].text,
                                             "shamol tezligi": f"{necessary_things[32].text}{m_taqsin_s[6].text}",
                                             "yog'ingarchilik": f"{necessary_things[23].text}{yogingarchilik[7].text}",
                                             "namlik": f"{necessary_things[31].text}%",
                                             "yomg'ir yog'ish ehtimoli": f"{necessary_things[15].text}%"}}},
                    {"kiyimlarga oid tavfsiyalar": [clothe.text for clothe in recommended_clothes]}]},
               {"ertaga": "soon :)"}]