import json
import requests

api_key = '2917db88-d0cf-4c58-a782-8714cdab0094'

req_header = {"X-Yandex-API-Key": api_key}
req_params = {
    'lat': '55.976276',
    'lon': '92.854022',
    'lang': 'ru_RU',
    'limit': '2'
}

#dataclass
class WeatherObj:
    def __init__(self, *args):
        self.temp = args[0]
        self.condition = args[1]
        self.wind_speed = args[2]
        self.wind_dir = args[3]
        self.pressure = args[4]
        self.humidity = args[5]
        self.season = args[6]
        self.cloudness = args[7]


def parse_json_data():
    request = requests.get('https://api.weather.yandex.ru/v2/forecast', headers=req_header, params=req_params)
    request_result = request.text
    return request_result


def create_weather_obj(data):
    data = data['fact']
    weather_obj = WeatherObj(data['temp'], data['condition'],
                             data['wind_speed'], data['wind_dir'],
                             data['pressure_mm'], data['humidity'],
                             data['season'], data['cloudness'])
    return weather_obj


def get_current_weather():
    data = json.loads(parse_json_data())

    weather_obj = create_weather_obj(data)

    return weather_obj


def main():
    print(get_current_weather().temp)


if __name__ == '__main__':
    main()