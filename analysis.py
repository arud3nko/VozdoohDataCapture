from mysql.connector import connect, Error
import matplotlib.pyplot as plt
import numpy as np
from statistics import mean
from mpl_toolkits.mplot3d import Axes3D
from  matplotlib.colors import LinearSegmentedColormap


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
    count = [i for i in range(250)]

    average_wind_speed = round(mean(wind_speed), 3)
    average_pollution = round(mean(pollution), 3)

    print(average_wind_speed, average_pollution)

    y = wind_speed[:250]
    x = pollution[:250]
    plt.figure(figsize=(12, 8))

    plt.grid(True)

    plt.plot(count, x)

    plt.show()


def wind_speed_time_graph(pollution, wind_speed):
    count = [i for i in range(250)]

    y = wind_speed[:250]
    plt.figure(figsize=(12, 8))

    plt.grid(True)
    plt.plot(count, y)
    plt.show()


def pollution_wind_speed_graph(pollution, wind_speed):
    # y = pollution[:250]
    # plt.figure(figsize=(12, 8))

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.scatter(x=wind_speed, y=pollution)

    plt.show()


def pollution_wind_speed_temp_graph(pollution, wind_speed, temperature):

    fig = plt.figure()
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
    ax.set_ylabel("Температура, С°")
    ax.set_zlabel("Уровень загрязнения, AQI")

    plt.title(f"График зависимости уровня загрязнения воздуха \nот погодных условий. Замеров: {len(pollution)}")
    #plt.savefig('graph.png')
    plt.show()



def main():

    try:
        sql_connection = connect(
            host = '',
            user = '',
            password = '',
            database = ''
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
        print(f'AIR: {row[2]} | TEMP: {row[3]} |  W-SPEED: {float(row[4])}')
        pollution.append(int(row[2]))
        wind_speed.append(float(row[4]))
        temperature.append(int(row[3]))

    pollution_unique = []
    wind_speed_unique = []

    # print(min(pollution), max(pollution))
    # print(min(wind_speed), max(wind_speed))

    #pollution_time_graph(pollution, wind_speed)
    # wind_speed_time_graph(pollution, wind_speed)
    pollution_wind_speed_temp_graph(pollution, wind_speed, temperature)


if __name__ == "__main__":
    main()
