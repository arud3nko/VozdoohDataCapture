import json
import requests
from settings import get_config
from dataclasses import dataclass

Config = get_config()

api_key = Config.WEATHER_API_KEY

req_header = {"X-Yandex-API-Key": api_key}
req_params = {
    'lat': '55.976276',
    'lon': '92.854022',
    'lang': 'ru_RU'
    # 'limit': '2'  # bug fix
}


@dataclass
class WeatherObj:
    temp: str
    condition: str
    wind_speed: str
    wind_dir: str
    pressure: str
    humidity: str
    season: str
    cloudness: str


def parse_json_data():
    request = requests.get('https://api.weather.yandex.ru/v2/informers', headers=req_header, params=req_params)
    request_result = request.text
    return request_result


def create_weather_obj(data):
    data = data['fact']
    weather_obj = WeatherObj(temp=data['temp'], condition=data['condition'],
                             wind_speed=data['wind_speed'], wind_dir=data['wind_dir'],
                             pressure=data['pressure_mm'], humidity=data['humidity'],
                             season=data['season'], cloudness='NULL')  # bug fix data['cloudness'])

    return weather_obj


def get_current_weather():
    data = json.loads(parse_json_data())
    weather_obj = create_weather_obj(data)

    return weather_obj


def main():
    print(get_current_weather().temp)


if __name__ == '__main__':
    main()
