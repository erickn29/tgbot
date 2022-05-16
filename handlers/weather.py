import datetime

import emoji
import requests

API = '5730e41c-f539-45e5-8e41-9924ff4e36a5'
URL = 'https://api.weather.yandex.ru/v2/forecast'
CONDITION_DICT = {
    'clear': emoji.emojize(':sun:'),
    'partly-cloudy': emoji.emojize(':sun_behind_small_cloud:'),
    'cloudy': emoji.emojize(':sun_behind_large_cloud:'),
    'overcast': emoji.emojize(':cloud:'),
    'drizzle': emoji.emojize(':sun_behind_rain_cloud:'),
    'light-rain': emoji.emojize(':sun_behind_rain_cloud:'),
    'rain': emoji.emojize(':sun_behind_small_cloud:'),
    'moderate-rain': emoji.emojize(':sun_behind_small_cloud:'),
    'heavy-rain': emoji.emojize(':cloud_with_rain:'),
    'continuous-heavy-rain': emoji.emojize(':cloud_with_rain:'),
    'showers': emoji.emojize(':cloud_with_rain:'),
    'wet-snow': emoji.emojize(':cloud_with_snow:'),
    'light-snow': emoji.emojize(':cloud_with_snow:'),
    'snow': emoji.emojize(':cloud_with_snow:'),
    'snow-showers': emoji.emojize(':cloud_with_snow:'),
    'hail': emoji.emojize(':cloud_with_snow:'),
    'thunderstorm': emoji.emojize(':cloud_with_lightning:'),
    'thunderstorm-with-rain': emoji.emojize(':cloud_with_lightning:'),
    'thunderstorm-with-hail': emoji.emojize(':cloud_with_lightning:'),
}
WIND_DICT = {
    'nw': 'СЗ',
    'n': 'С',
    'ne': 'СВ',
    'e': 'В',
    'se': 'ЮВ',
    's': 'Ю',
    'sw': 'ЮЗ',
    'w': 'З',
    'с': 'штиль',
}
CITIES_DICT = {
    'arkh': (64.54, 40.54),
    'spb': (59.94, 30.31),
    'msk': (55.75, 37.62),
    'krd': (45.04, 38.98),
    'kng': (54.71, 20.51),
    'nn': (56.33, 44),
    'yar': (57.63, 39.87),
    'kzn': (55.79, 49.12),
    'ala': (36.5438, 31.9998)
}


def get_weather(city):
    print(f'[{datetime.datetime.now().time().strftime("%H:%M:%S")}]Ищу погоду для {city}')
    city_string = ''
    headers = {'X-Yandex-API-Key': API}
    querysetting = {'lat': CITIES_DICT[city][0], 'lon': CITIES_DICT[city][1], 'extra': 'true'}
    data = requests.request("GET", URL, headers=headers, params=querysetting).json()
    city_string += f"Погода на неделю для города {data['geo_object']['province']['name']}\n\n"
    print(data['geo_object']['province']['name'])
    for i in range(len(data['forecasts'])):
        this_date = data['forecasts'][i]['date'].split('-')
        true_date = datetime.date(int(this_date[0]), int(this_date[1]), int(this_date[2]))
        if true_date == datetime.datetime.now().date():
            city_string += '*Погода на сегодня*\n'
            city_string += f"_Днем_: {data['forecasts'][i]['parts']['day_short']['temp']}'C "
            city_string += f"{CONDITION_DICT[data['forecasts'][i]['parts']['day_short']['condition']].capitalize()} "
            city_string += WIND_DICT[data['forecasts'][i]['parts']['day_short']['wind_dir']]
            city_string += f" {data['forecasts'][i]['parts']['day_short']['wind_speed']} м/с\n"
            city_string += f"_Ночью_: {data['forecasts'][i]['parts']['night_short']['temp']}'C "
            city_string += f"{CONDITION_DICT[data['forecasts'][i]['parts']['night_short']['condition']].capitalize()} "
            city_string += WIND_DICT[data['forecasts'][i]['parts']['night_short']['wind_dir']]
            city_string += f" {data['forecasts'][i]['parts']['night_short']['wind_speed']} м/с\n\n"
        else:
            city_string += f'*Погода на {true_date.strftime("%d.%m.%Y")}*\n'
            city_string += f"_Днем_: {data['forecasts'][i]['parts']['day_short']['temp']}'C "
            city_string += f"{CONDITION_DICT[data['forecasts'][i]['parts']['day_short']['condition']].capitalize()} "
            city_string += WIND_DICT[data['forecasts'][i]['parts']['day_short']['wind_dir']]
            city_string += f" {data['forecasts'][i]['parts']['day_short']['wind_speed']} м/с\n"
            city_string += f"_Ночью_: {data['forecasts'][i]['parts']['night_short']['temp']}'C "
            city_string += f"{CONDITION_DICT[data['forecasts'][i]['parts']['night_short']['condition']].capitalize()} "
            city_string += WIND_DICT[data['forecasts'][i]['parts']['night_short']['wind_dir']]
            city_string += f" {data['forecasts'][i]['parts']['night_short']['wind_speed']} м/с\n\n"
    return city_string

# print(get_weather('kng'))
