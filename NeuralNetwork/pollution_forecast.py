import joblib

tree_grid = joblib.load('NeuralNetwork/neural_net.pkl')


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
    indicators = [[int(temp), float(wind_speed), int(wind_dir), int(pressure), int(humidity),
                   c_clear, c_cloudy, c_light_rain, c_light_snow, c_overcast, c_snow, c_wet_snow]]
    result = tree_grid.predict(indicators)
    return result


# print(forecast('-5', '1.2', '0', '751', '58', 'clear'))
