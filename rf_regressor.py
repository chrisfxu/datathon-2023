import numpy as np
import pandas as pd
import os
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import BayesianRidge
import matplotlib.pyplot as plt

train = pd.read_csv('data/train.csv')

y = train["FVC"]
X = train.copy()
X=X.drop(columns = ["FVC", "Patient"])
X['Sex'] = X['Sex'].map(lambda x: 1 if(x == "Male") else 0 )
X['SmokingStatus'] = X['SmokingStatus'].map(lambda x: 1 if(x == "Ex-smoker") else 0 )
X.head()

regressor = RandomForestRegressor(n_estimators=100, random_state=0)
regressor.fit(X,y)

