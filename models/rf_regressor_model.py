import pandas as pd
import os
import pickle
from sklearn.ensemble import RandomForestRegressor
from models.base_model import BaseModel


class RandomForestRegressorModel(BaseModel):
    model: RandomForestRegressor

    def __init__(self):
        self.trained_model_filename = f'trained_models/{self.__class__.__name__}'
        if not os.path.exists(self.trained_model_filename):
            self.train_and_store_model()
        with open(self.trained_model_filename, 'rb') as f:
            self.model = pickle.load(f)

    def train_and_store_model(self) -> RandomForestRegressor:
        train = pd.read_csv('data/train.csv')
        train['FVCLag'] = train.FVC.shift(1)
        train['PercentLag'] = train.Percent.shift(1)

        uq = set()
        for index, row in train.iterrows():
            if row['Patient'] not in uq:
                uq.add(row['Patient'])
                train.drop(index, axis=0, inplace=True)

        y = train["FVC"]
        X = train.copy()
        X=X.drop(columns = ["FVC", "Patient", "Percent"])
        X['Sex'] = X['Sex'].map(lambda x: 1 if(x == "Male") else 0 )
        X['SmokingStatus'] = X['SmokingStatus'].map(lambda x: 1 if(x == "Ex-smoker") else 0 )
        regressor = RandomForestRegressor(n_estimators=250, random_state=0)
        regressor.fit(X.values, y.values)

        with open(self.trained_model_filename, 'wb') as f:
            pickle.dump(regressor, f)
    
    def predict(_self, age: int, is_male: bool, does_smoke: bool, weeks_since_scan: int, capacity_lag: float, percent_lag: float):
        # Weeks  Age  Sex  SmokingStatus  FVCLag  PercentLag
        return _self.model.predict([[weeks_since_scan, age, is_male, does_smoke, capacity_lag, percent_lag]])


if __name__ == '__main__':
    model = RandomForestRegressorModel()