from weather import get_current_weather
from nebo import get_current_pollution
from mysql.connector import connect, Error
import datetime


def main():
    current_datetime = datetime.datetime.now().timestamp()
    weather = get_current_weather()
    pollution = get_current_pollution()

    # sql_connection = sqlite3.connect('pollution_weather.db')
    # cursor = sql_connection.cursor()

    try:
        sql_connection = connect(
            host = '',
            user = '',
            password = '',
            database = ''
        )
        cursor = sql_connection.cursor()
    except Error as E:
        print(E)

    try:
        sql_query = """INSERT INTO `data` (`date`, pollution, temp, wind_speed, wind_dir,
                        pressure, humidity, cloudness, `condition`, season)
                        VALUES 
                        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

        data_tuple = (current_datetime, pollution, weather.temp, weather.wind_speed,
                      weather.wind_dir, weather.pressure, weather.humidity,
                      weather.cloudness, weather.condition, weather.season)

        count = cursor.execute(sql_query, data_tuple)
        sql_connection.commit()

    except Exception as e:
        sql_connection.commit()
        print(e)


if __name__ == '__main__':
    main()