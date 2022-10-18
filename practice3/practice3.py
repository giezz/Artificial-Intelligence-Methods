from bs4 import BeautifulSoup as bs
import requests
import codecs
from collections import Counter


def parsing():
    url = "https://www.gismeteo.ru/weather-kirov-4292/"
    # request = requests.get(url)
    # soup = bs(request.text, "html.parser")

    doc = bs(codecs.open(
        'GISMETEO_ Погода в Кирове сегодня, прогноз погоды Киров на сегодня, Киров (городской округ), Кировская область, Россия.html',
        encoding='utf-8',
        mode='r'
    ).read(), 'html.parser')

    current_temp = doc.find("span", class_="unit unit_temperature_c").text
    weather = doc.find("div", class_="widget-row-chart widget-row-chart-temperature").find("div", class_="values").find_all("span", class_="unit unit_temperature_c")
    wind = doc.find("div", class_="widget-row widget-row-wind-direction").find_all("div", class_="direction")

    print(f"Температура сейчас {current_temp}")

    average_temp = 0
    for w in weather:
        # print(w.text)
        average_temp += int(w.text)
    print(f"Средняя температура сегодня {average_temp / len(weather)}")

    winds = []
    for w in wind:
        # print(w.text)
        winds.append(w.text)
    print(f"Направление ветра в среднем{Counter(winds).most_common(1)[0][0]}")


if __name__ == '__main__':
    parsing()
