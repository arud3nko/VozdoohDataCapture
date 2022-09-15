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

df = pd.read_csv("data.csv")

df.drop(['id', 'date', 'wind_dir', 'cloudness',
         'condition', 'season'], axis=1, inplace=True)

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
