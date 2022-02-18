from weather import get_current_weather
from nebo import get_current_pollution
import sqlite3
import datetime


def main():
    current_datetime = datetime.datetime.now().timestamp()
    weather = get_current_weather()
    pollution = get_current_pollution()

    sql_connection = sqlite3.connect('pollution_weather.db')
    cursor = sql_connection.cursor()

    sql_query = """INSERT INTO data (date, pollution, temp, wind_speed, wind_dir,
                    pressure, humidity, cloudness, condition, season)
                    VALUES 
                    (?,?,?,?,?,?,?,?,?,?);"""

    data_tuple = (current_datetime, pollution, weather.temp, weather.wind_speed,
                  weather.wind_dir, weather.pressure, weather.humidity,
                  weather.cloudness, weather.condition, weather.season)

    count = cursor.execute(sql_query, data_tuple)
    sql_connection.commit()
    cursor.close()



if __name__ == '__main__':
    main()