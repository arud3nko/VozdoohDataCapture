from dataclasses import dataclass
from datetime import datetime
import requests
import typing


@dataclass(frozen=False)
class WeatherObj:
    datetime: typing.Any
    temperature: float
    windSpeed: float
    humidity: float
    pressure: typing.Any = None
    pollution: int = None

    def __post_init__(self):
        if self.pressure:
            self.pressure = self.pressure * 0.75006
        else:
            self.pressure = "Null"

        self.datetime = self.datetime.replace(self.datetime[10], ' ')
        self.datetime = self.datetime.replace(self.datetime[-6:], '')

        self.datetime = datetime.strptime(self.datetime,
                                          '%Y-%m-%d %H:%M:%S')
        self.datetime = int(self.datetime.timestamp())


def api_request(Config):
    url = "https://api.tomorrow.io/v4/timelines"

    querystring = {
        "location": "56.010569, 92.852572",
        "fields": ["temperature", "windSpeed", "humidity", "pressureSurfaceLevel"],
        "units": "metric",
        "timesteps": ["1h", "1d"],
        "timezone": "Asia/Krasnoyarsk",
        "apikey": Config.TOMORROW_API_TOKEN}

    response = requests.request("GET", url, params=querystring)

    data = response.json()

    # print(json.dumps(data, indent=4))

    return data


def collect_data(Config):
    data = api_request(Config)

    weatherObjectsDaily = list()
    weatherObjectsHourly = list()

    for i in range(len(data["data"]["timelines"][0]["intervals"])):
        tempObject = WeatherObj(
            data["data"]["timelines"][0]["intervals"][i]["startTime"],
            data["data"]["timelines"][0]["intervals"][i]["values"]["temperature"],
            data["data"]["timelines"][0]["intervals"][i]["values"]["windSpeed"],
            data["data"]["timelines"][0]["intervals"][i]["values"]["humidity"],
            data["data"]["timelines"][0]["intervals"][i]["values"]["pressureSurfaceLevel"]
        )

        weatherObjectsDaily.append(tempObject)

    for i in range(len(data["data"]["timelines"][1]["intervals"])):
        try:
            tempObject = WeatherObj(
                data["data"]["timelines"][1]["intervals"][i]["startTime"],
                data["data"]["timelines"][1]["intervals"][i]["values"]["temperature"],
                data["data"]["timelines"][1]["intervals"][i]["values"]["windSpeed"],
                data["data"]["timelines"][1]["intervals"][i]["values"]["humidity"],
                data["data"]["timelines"][1]["intervals"][i]["values"]["pressureSurfaceLevel"]
            )

            weatherObjectsHourly.append(tempObject)
        except KeyError:
            continue

    return weatherObjectsDaily, weatherObjectsHourly


def main():
    pass


if __name__ == '__main__':
    main()
