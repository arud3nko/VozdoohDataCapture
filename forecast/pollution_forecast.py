import joblib

tree_grid = joblib.load('forecast/model.pkl')


def forecast(weatherObj):
    indicators = [[int(weatherObj.temperature),
                   float(weatherObj.windSpeed),
                   int(weatherObj.pressure),
                   int(weatherObj.humidity)]]
    result = tree_grid.predict(indicators)
    weatherObj.pollution = int(result)

    return weatherObj


def main():
    pass


if __name__ == '__main__':
    main()
