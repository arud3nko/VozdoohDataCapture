import matplotlib.pyplot as plt
import pytz
from mysql.connector import connect, Error
from matplotlib.colors import LinearSegmentedColormap
from datetime import datetime
from settings import get_config

Config = get_config()

Krasnoyarsk = pytz.timezone('Asia/Krasnoyarsk')
global_path = Config.GLOBAL_PATH

yandex_logo = '../static/yandex_logo.png'
nebo_logo = '../static/Logo.png'


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def watermark():
    ax = plt.gca()
    im_ya = plt.imread(yandex_logo)
    ax.figure.figimage(im_ya,
                       ax.bbox.xmax/2.29,
                       ax.bbox.ymax/1.125,
                       alpha=0.5, zorder=1)

    im_nebo = plt.imread(nebo_logo)
    ax.figure.figimage(im_nebo,
                       ax.bbox.xmax/1.87,
                       ax.bbox.ymax/1.19,
                       alpha=1, zorder=1)

    return ax


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

    watermark()

    plt.savefig(global_path+"images/pollution-time-graph.png")


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

    watermark()

    plt.savefig(global_path+"images/wind-speed-time-graph.png")


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

    watermark()

    plt.savefig(global_path+"images/graph-pollution-wind-speed.png")


def pollution_pressure_graph(pollution, pressure):

    c = ['lawngreen', 'green', 'palegreen', 'lightcoral', 'red', 'darkred']
    v = [0, 0.4, 0.5, 0.6, 0.9, 1.]
    l = list(zip(v, c))
    user_cmap = LinearSegmentedColormap.from_list('rg', l)

    fig, ax = plt.subplots(figsize=(12, 8))

    ax.scatter(x=pressure, y=pollution, c=pollution, cmap=user_cmap)

    plt.xlabel("Атмосферное давление, мм. рт. ст.")
    plt.ylabel("Уровень загрязнения, AQI")

    plt.title(f"График зависимости уровня загрязнения воздуха\nот атмосферного давления. Последнее обновление: {datetime.now(Krasnoyarsk)}")

    watermark()

    plt.savefig(global_path+"images/graph-pollution-pressure.png")


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

    watermark()

    plt.savefig(global_path+'images/graph.png')


def main():

    try:
        sql_connection = connect(
            host=Config.HOST,
            user=Config.USER,
            password=Config.PASSWORD,
            database=Config.DATABASE
        )

    except Error as E:
        sql_connection.commit()
        print(E)

    select_data = "SELECT * FROM `data`"

    rows = execute_read_query(sql_connection, select_data)
    pollution = []
    wind_speed = []
    temperature = []
    pressure = []

    for row in rows:
        pollution.append(int(row[2]))
        wind_speed.append(float(row[4]))
        temperature.append(int(row[3]))
        pressure.append(int(row[6]))

    pollution_time_graph(pollution, wind_speed)
    wind_speed_time_graph(pollution, wind_speed)
    pollution_wind_speed_graph(pollution, wind_speed)
    pollution_wind_speed_temp_graph(pollution, wind_speed, temperature)
    pollution_pressure_graph(pollution, pressure)


if __name__ == "__main__":
    main()
