from abc import ABC, abstractmethod


class BaseModel(ABC):
    @abstractmethod
    def predict(self, age: int, is_male: bool, does_smoke: bool, weeks_since_scan: int, weeks_since_checkup: int, lung_capacity: int) -> str:
        pass