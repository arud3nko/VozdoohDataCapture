from NeuralNetwork import pollution_forecast
import requests
import json
import datetime

city = 'Krasnoyarsk'

text = requests.get('https://api.openweathermap.org/data/2.5/forecast?lat=55.976276&lon=92.854022&exclude=daily&units=metric&appid=a64cd13d5be981048c07c7cd1be03173')

data = text.json()

# print(json.dumps(data, indent=4, sort_keys=True))

weather = []

for element in data['list']:
    weather.append([element['dt'], element['main']['temp'], element['wind']['speed'], element['wind']['deg'],
                    int(element['main']['pressure'])*0.75008, element['main']['humidity'], element['weather'][0]['description']])
                    # element['main']['pressure'], element['main']['humidity'], element['weather']['description']])

# for el in weather:
#     print(pollution_forecast.forecast(el[1], el[2], 0, el[4], el[5], 'cloudy'))


for el in weather:
    print(datetime.datetime.fromtimestamp(el[0]), el[1], el[2], 0, el[4], el[5], '|', pollution_forecast.forecast(el[1], el[2], 0, el[4], el[5], 'cloudy'))
