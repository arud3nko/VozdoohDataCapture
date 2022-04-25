import numpy as np
import pandas as pd
import warnings
import seaborn as sns
import matplotlib.pyplot as plt
from pylab import rcParams
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, cross_val_score
import joblib
warnings.simplefilter('ignore')
rcParams['figure.figsize'] = 8, 5


df = pd.read_csv("D:\data_2.csv")

df['c - clear'] = True
df['c - cloudy'] = True
df['c - light-rain'] = True
df['c - light-snow'] = True
df['c - overcast'] = True
df['c - snow'] = True
df['c - wet-snow'] = True

for i in range(0, 5882):
    if df['condition'][i] == 'clear':
        df['c - clear'][i] = True
        df['c - cloudy'][i] = False
        df['c - light-rain'][i] = False
        df['c - light-snow'][i] = False
        df['c - overcast'][i] = False
        df['c - snow'][i] = False
        df['c - wet-snow'][i] = False
    elif df['condition'][i] == 'cloudy':
        df['c - clear'][i] = False
        df['c - cloudy'][i] = True
        df['c - light-rain'][i] = False
        df['c - light-snow'][i] = False
        df['c - overcast'][i] = False
        df['c - snow'][i] = False
        df['c - wet-snow'][i] = False
    elif df['condition'][i] == 'light-rain':
        df['c - clear'][i] = False
        df['c - cloudy'][i] = False
        df['c - light-rain'][i] = True
        df['c - light-snow'][i] = False
        df['c - overcast'][i] = False
        df['c - snow'][i] = False
        df['c - wet-snow'][i] = False
    elif df['condition'][i] == 'light-snow':
        df['c - clear'][i] = False
        df['c - cloudy'][i] = False
        df['c - light-rain'][i] = False
        df['c - light-snow'][i] = True
        df['c - overcast'][i] = False
        df['c - snow'][i] = False
        df['c - wet-snow'][i] = False
    elif df['condition'][i] == 'overcast':
        df['c - clear'][i] = False
        df['c - cloudy'][i] = False
        df['c - light-rain'][i] = False
        df['c - light-snow'][i] = False
        df['c - overcast'][i] = True
        df['c - snow'][i] = False
        df['c - wet-snow'][i] = False
    elif df['condition'][i] == 'snow':
        df['c - clear'][i] = False
        df['c - cloudy'][i] = False
        df['c - light-rain'][i] = False
        df['c - light-snow'][i] = False
        df['c - overcast'][i] = False
        df['c - snow'][i] = True
        df['c - wet-snow'][i] = False
    elif df['condition'][i] == 'wet-snow':
        df['c - clear'][i] = False
        df['c - cloudy'][i] = False
        df['c - light-rain'][i] = False
        df['c - light-snow'][i] = False
        df['c - overcast'][i] = False
        df['c - snow'][i] = False
        df['c - wet-snow'][i] = True

df.drop(['condition'], axis=1, inplace=True)
df.drop(['id', 'date', 'cloudness', 'season'], axis=1, inplace=True)

df['wind_dir'] = pd.factorize(df['wind_dir'])[0]
temp = df['temp']
y = df['pollution']
df.drop(['pollution'], axis=1, inplace=True)

X_train, X_holdout, y_train, y_holdout = train_test_split(df.values, y, test_size=0.3,
                                                          random_state=17)
reg = RandomForestRegressor()
reg.fit(X_train, y_train)

reg_params = {'max_depth': range(1, 15), 'max_features': range(4, 15)}

tree_grid = GridSearchCV(reg, reg_params, cv=5, n_jobs=-1, verbose=True)

tree_grid.fit(X_train, y_train)

joblib.dump(tree_grid, 'neural_net.pkl', compress=1)
