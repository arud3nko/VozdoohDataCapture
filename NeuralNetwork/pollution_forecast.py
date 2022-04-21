import joblib

tree_grid = joblib.load('neural_net.pkl')

weather_indicators = [[-5, 1.2, 0, 751, 58, True, False, False, False, False, False, False]]

print(tree_grid.predict(weather_indicators))
