import joblib

tree_grid = joblib.load('neural_net.pkl')


def forecast(temp, wind_speed, wind_dir, pressure, humidity, condition):
    c_clear, c_cloudy, c_light_rain, c_light_snow, c_overcast, c_snow, c_wet_snow = False, False, False, False, \
                                                                                    False, False, False
    if condition == 'clear':
        c_clear = True
    elif condition == 'cloudy':
        c_cloudy = True
    elif condition == 'light-rain':
        c_light_rain = True
    elif condition == 'light-snow':
        c_light_snow = True
    elif condition == 'overcast':
        c_overcast = True
    elif condition == 'snow':
        c_snow = True
    elif condition == 'wet-snow':
        c_wet_snow = True

    wind_dir = float(wind_dir)

    if 157.5 < wind_dir <= 202.5:
        wind_dir = 0
    elif 0 <= wind_dir <= 22.5 or 337.5 < wind_dir <= 360:
        wind_dir = 1
    elif 247.5 < wind_dir <= 292.5:
        wind_dir = 2
    elif 202.5 < wind_dir <= 247.5:
        wind_dir = 3
    elif 112.5 < wind_dir <= 157.5:
        wind_dir = 4
    elif 67.5 < wind_dir <= 112.5:
        wind_dir = 5
    elif 22.5 < wind_dir <= 67.5:
        wind_dir = 6
    else:
        wind_dir = 7

    indicators = [[int(temp), float(wind_speed), int(wind_dir), int(pressure), int(humidity),
                   c_clear, c_cloudy, c_light_rain, c_light_snow, c_overcast, c_snow, c_wet_snow]]
    result = tree_grid.predict(indicators)
    return result


# print(forecast('-3', '3.7', '270', '733', '66', 'overcast'))
