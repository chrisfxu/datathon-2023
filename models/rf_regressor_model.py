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
        train = pd.read_csv(self.train_data_path)
        y = train["FVC"]
        X = train.copy()
        X = X.drop(columns = ["FVC", "Patient"])
        X['Sex'] = X['Sex'] == "Male"
        X['SmokingStatus'] = X['SmokingStatus'] == "Ex-smoker"
        regressor = RandomForestRegressor(n_estimators=100, random_state=0)
        regressor.fit(X, y)

        with open(self.trained_model_filename, 'wb') as f:
            pickle.dump(regressor, f)
    
    def predict(_self, age: int, is_male: bool, does_smoke: bool, weeks_since_scan: int, weeks_since_checkup: int, lung_capacity: float):
        return _self.model.predict([[weeks_since_scan, lung_capacity, age, is_male, does_smoke]])


if __name__ == '__main__':
    model = RandomForestRegressorModel()