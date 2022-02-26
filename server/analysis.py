from mysql.connector import connect, Error
import matplotlib.pyplot as plt
import numpy as np
import pytz
from statistics import mean
from mpl_toolkits.mplot3d import Axes3D
from  matplotlib.colors import LinearSegmentedColormap
from datetime import datetime

Krasnoyarsk = pytz.timezone('Asia/Krasnoyarsk')
global_path = '/var/www/'


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def pollution_time_graph(pollution, wind_speed):
    count = [i for i in range(len(pollution))]

    y = wind_speed[:250]
    x = pollution[:250]
    plt.figure(figsize=(12, 8))

    plt.grid(True)

    plt.xlabel("ID замера")
    plt.ylabel("Уровень загрязнения, AQI")

    plt.title(
        f"График изменения уровня загрязнения воздуха"
        f"\nПоследнее обновление: {datetime.now(Krasnoyarsk)}")
    plt.plot(count, pollution, color='darkred', linewidth=3)
    plt.savefig(global_path+"images/pollution-time-graph.png")
    # plt.show()


def wind_speed_time_graph(pollution, wind_speed):
    count = [i for i in range(len(pollution))]

    y = wind_speed
    plt.figure(figsize=(12, 8))

    plt.xlabel("ID замера")
    plt.ylabel("Скорость ветра, м/с")

    plt.title(
        f"График изменения уровня скорости ветра"
        f"\nПоследнее обновление: {datetime.now(Krasnoyarsk)}")

    plt.grid(True)
    plt.plot(count, y, color='mediumvioletred')
    plt.savefig(global_path+"images/wind-speed-time-graph.png")
    # plt.show()


def pollution_wind_speed_graph(pollution, wind_speed):

    c = ['lawngreen', 'green', 'palegreen', 'lightcoral', 'red', 'darkred']
    v = [0, 0.4, 0.5, 0.6, 0.9, 1.]
    l = list(zip(v, c))
    user_cmap = LinearSegmentedColormap.from_list('rg', l)

    fig, ax = plt.subplots(figsize=(12, 8))

    ax.scatter(x=wind_speed, y=pollution, c=pollution, cmap=user_cmap)

    plt.xlabel("Скорость ветра, м/c")
    plt.ylabel("Уровень загрязнения, AQI")

    plt.title(f"График зависимости уровня загрязнения воздуха\nот скорости ветра. Последнее обновление: {datetime.now(Krasnoyarsk)}")
    plt.savefig(global_path+"images/graph-pollution-wind-speed.png")

    # plt.show()


def pollution_wind_speed_temp_graph(pollution, wind_speed, temperature):

    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(111, projection='3d')

    x = wind_speed
    y = temperature
    z = pollution

    c = ['lawngreen', 'green', 'palegreen', 'lightcoral', 'red', 'darkred']
    v = [0, 0.4, 0.5, 0.6, 0.9, 1.]
    l = list(zip(v, c))
    user_cmap = LinearSegmentedColormap.from_list('rg', l)

    ax.scatter(x, y, z, s=20, c=pollution, cmap=user_cmap)
    ax.set_xlabel("Скорость ветра, м/с")
    ax.set_ylabel("Температура, °С")
    ax.set_zlabel("Уровень загрязнения, AQI")

    plt.title(f"График зависимости уровня загрязнения воздуха от погодных условий. Замеров: {len(pollution)}\n"
              f"Последнее обновление: {datetime.now(Krasnoyarsk)}")
    plt.savefig(global_path+'images/graph.png')
    # plt.show()


def main():

    try:
        sql_connection = connect(
            host = '195.133.145.83',
            user = 'remote',
            password = '1lxyz8',
            database = 'pollution'
        )

    except Error as E:
        sql_connection.commit()
        print(E)

    select_data = "SELECT * FROM `data`"

    rows = execute_read_query(sql_connection, select_data)
    pollution = []
    wind_speed = []
    temperature = []

    for row in rows:
        # print(f'AIR: {row[2]} | TEMP: {row[3]} |  W-SPEED: {float(row[4])}')
        pollution.append(int(row[2]))
        wind_speed.append(float(row[4]))
        temperature.append(int(row[3]))

    pollution_unique = []
    wind_speed_unique = []

    # print(min(pollution), max(pollution))
    # print(min(wind_speed), max(wind_speed))

    pollution_time_graph(pollution, wind_speed)
    wind_speed_time_graph(pollution, wind_speed)
    pollution_wind_speed_graph(pollution, wind_speed)
    pollution_wind_speed_temp_graph(pollution, wind_speed, temperature)


if __name__ == "__main__":
    main()
