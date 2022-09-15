from forecast import tomorrowIOapi
from forecast import pollution_forecast
from forecast import executor
from settings import get_config


def main():
    Config = get_config()

    weatherObjectsDaily, weatherObjectsHourly = tomorrowIOapi.collect_data(Config)

    for i in range(len(weatherObjectsDaily)):
        weatherObjectsDaily[i] = pollution_forecast.forecast(weatherObjectsDaily[i])

    for i in range(len(weatherObjectsHourly)):
        weatherObjectsHourly[i] = pollution_forecast.forecast(weatherObjectsHourly[i])

    executor.sql_executor(weatherObjectsDaily, Config, 'forecast_daily')
    executor.sql_executor(weatherObjectsHourly, Config, 'forecast_hourly')


if __name__ == '__main__':
    main()