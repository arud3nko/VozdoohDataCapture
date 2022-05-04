from NeuralNetwork import pollution_forecast
import requests
import json
import datetime
from settings import get_config
from mysql.connector import connect, Error

city = 'Krasnoyarsk'
Config = get_config()

five_days = requests.get('https://api.openweathermap.org/data/2.5/forecast?lat=55.976276&lon=92.854022&exclude=daily&units=metric&appid=a64cd13d5be981048c07c7cd1be03173')
hourly = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=55.976276&lon=92.854022&exclude=`hourly`&units=metric&appid=a64cd13d5be981048c07c7cd1be03173')

data_hourly = hourly.json()
data_five_days = five_days.json()

weather_five_days = []
weather_hourly = []

# print(json.dumps(data_hourly, indent=4))

for element in data_hourly["hourly"]:
    weather_hourly.append([element['dt'], element['temp'], element['wind_speed'], element['wind_deg'],
                              round(int(element['pressure']) * 0.72777, 3), element['humidity'],
                              element['weather'][0]['description']])

for element in data_five_days['list']:
    weather_five_days.append([element['dt'], element['main']['temp'], element['wind']['speed'], element['wind']['deg'],
                    round(int(element['main']['pressure'])*0.72777, 3), element['main']['humidity'], element['weather'][0]['description']])


def SQL_connector(database):
    sql_connection = connect(
            host=Config.HOST,
            user=Config.USER,
            password=Config.PASSWORD,
            database=database
        )

    cursor = sql_connection.cursor()

    return cursor, sql_connection


def database_handler():
    cursor, sql_connection = SQL_connector('forecast_daily')

    sql_query = """INSERT INTO `pollution` (`timestamp`, `pollution`)
                    VALUES (%s, %s) ON DUPLICATE KEY UPDATE `pollution` = %s;"""

    for el in weather_five_days:
        data = [el[0], int(pollution_forecast.forecast(el[1], el[2], el[3], el[4], el[5], 'cloudy')),
                int(pollution_forecast.forecast(el[1], el[2], el[3], el[4], el[5], 'cloudy'))]
        try:
            cursor.execute(sql_query, data)
        except Exception as e:
            sql_connection.commit()
            print(e)

    sql_connection.commit()

    cursor, sql_connection = SQL_connector('forecast_hourly')

    for el in weather_hourly:
        data = [el[0], int(pollution_forecast.forecast(el[1], el[2], el[3], el[4], el[5], 'cloudy')),
                int(pollution_forecast.forecast(el[1], el[2], el[3], el[4], el[5], 'cloudy'))]
        try:
            cursor.execute(sql_query, data)
        except Exception as e:
            sql_connection.commit()
            print(e)

    sql_connection.commit()


database_handler()
