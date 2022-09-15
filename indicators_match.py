from settings import get_config
from mysql.connector import connect, Error
from datetime import datetime
import statistics
import matplotlib.pyplot as plt


def SQL_connector(Config, database):
    sql_connection = connect(
            host=Config.HOST,
            user=Config.USER,
            password=Config.PASSWORD,
            database=database
        )

    return sql_connection


def execute_read_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
        connection.commit()


def draw_graph(pollution_fact, pollution_forecast, abs_difference):
    count = [i for i in range(len(pollution_fact))]

    plt.figure(figsize=(16, 8))

    plt.title(f"Абсолютная погрешность измерений: {abs_difference}")
    plt.xlabel("ID замера")
    plt.ylabel("Уровень загрязнения, AQI")

    plt.plot(count, pollution_forecast, color='mediumvioletred', linewidth='5.0', linestyle='dashdot')
    plt.plot(count, pollution_fact, color='green', linewidth='5.0')

    plt.legend(['FORECAST', 'FACT'])

    plt.savefig('difference.png')


def main():
    Config = get_config()

    pollution_fact = list()
    pollution_forecast = list()
    difference = list()

    sql_connection = SQL_connector(Config, Config.DATABASE)
    sql_query = """SELECT * FROM `data`"""

    rows_fact = execute_read_query(sql_connection, sql_query)

    sql_connection = SQL_connector(Config, 'forecast_daily')
    sql_query = """SELECT * FROM `pollution`"""

    rows_forecast = execute_read_query(sql_connection, sql_query)

    for i in range(len(rows_forecast)):
        timestamp_forecast = datetime.fromtimestamp(rows_forecast[i][1])
        date_forecast = timestamp_forecast.date()
        hour_forecast = datetime.strptime(str(timestamp_forecast), "%Y-%m-%d %H:%M:%S").hour
        for _ in range(len(rows_fact)):
            timestamp_fact = datetime.fromtimestamp(round(float(rows_fact[_][1])))
            date_fact = timestamp_fact.date()
            hour_fact = datetime.strptime(str(timestamp_fact), "%Y-%m-%d %H:%M:%S").hour
            if (date_forecast == date_fact) & (hour_forecast == hour_fact):
                pollution_fact.append(int(rows_fact[_][2]))
                pollution_forecast.append(int(rows_forecast[i][2]))
                break

    for i in range(len(pollution_forecast)):
        difference.append(abs(int(pollution_forecast[i])-int(pollution_fact[i])))

    abs_difference = round(statistics.mean(difference))

    draw_graph(pollution_fact, pollution_forecast, abs_difference)


if __name__ == '__main__':
    main()
