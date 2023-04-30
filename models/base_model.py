from abc import ABC, abstractmethod


class BaseModel(ABC):
    train_data_path: str = 'data/train.csv'

    @abstractmethod
    def predict(self, age: int, is_male: bool, does_smoke: bool, weeks_since_scan: int, lung_capacity: float):
        pass