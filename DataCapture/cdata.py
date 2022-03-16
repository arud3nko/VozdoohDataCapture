from weather import get_current_weather
from nebo import get_current_pollution
from mysql.connector import connect, Error
from settings import get_config
import datetime

Config = get_config()


def main():
    current_datetime = datetime.datetime.now().timestamp()
    weather = get_current_weather()
    pollution = get_current_pollution()

    try:
        sql_connection = connect(
            host=Config.HOST,
            user=Config.USER,
            password=Config.PASSWORD,
            database=Config.DATABASE
        )
        cursor = sql_connection.cursor()
    except Error as E:
        print(E)

    try:
        sql_query = """INSERT INTO `data` (`date`, pollution, temp, wind_speed, wind_dir,
                        pressure, humidity, cloudness, `condition`, season)
                        VALUES 
                        (%s, %s, %s, %s, %s, %s, %s, NULL, %s, %s);"""  # bug fixes - NULL above the cloudness

        data_tuple = (current_datetime, pollution, weather.temp, weather.wind_speed,
                      weather.wind_dir, weather.pressure, weather.humidity,
                      # weather.cloudness, weather.condition, weather.season)
                      weather.condition, weather.season)  # bug fixes

        count = cursor.execute(sql_query, data_tuple)
        sql_connection.commit()

    except Exception as e:
        sql_connection.commit()
        print(e)


if __name__ == '__main__':
    main()