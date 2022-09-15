from mysql.connector import connect


def sql_executor(weatherObjects, Config, table_name):
    try:
        sql_connection = connect(
            host=Config.HOST,
            user=Config.USER,
            password=Config.PASSWORD,
            database=Config.DATABASE
        )

        cursor = sql_connection.cursor()

        sql_query = f"""INSERT INTO {table_name} (pollution, datetime, temperature, windSpeed, humidity, pressure)
                        VALUES 
                        (%s, %s, %s, %s, %s, %s) 
                        ON DUPLICATE KEY UPDATE
                        pollution = %s, temperature = %s, windSpeed = %s, humidity = %s, pressure = %s;"""

        for weatherObj in weatherObjects:
            data_tuple = (weatherObj.pollution, weatherObj.datetime,
                          weatherObj.temperature, weatherObj.windSpeed,
                          weatherObj.humidity, weatherObj.pressure,
                          weatherObj.pollution,
                          weatherObj.temperature, weatherObj.windSpeed,
                          weatherObj.humidity, weatherObj.pressure
                          )

            cursor.execute(sql_query, data_tuple)

        sql_connection.commit()

    except Exception as e:
        print(e)


def main():
    pass


if __name__ == '__main__':
    main()
