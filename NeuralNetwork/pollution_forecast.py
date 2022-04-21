import joblib

tree_grid = joblib.load('neural_net.pkl')


def forecast(temp, wind_speed, wind_dir, pressure, humidity, c_clear, c_cloudy,
             c_light_rain, c_light_snow, c_overcast, c_snow, c_wet_snow):
    indicators = [[int(temp), float(wind_speed), int(wind_dir), int(pressure), int(humidity),
                   c_clear, c_cloudy, c_light_rain, c_light_snow, c_overcast, c_snow, c_wet_snow]]
    result = tree_grid.predict(indicators)
    return result
