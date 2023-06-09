import streamlit as st
from models.base_model import BaseModel


class StubModel(BaseModel):
    @st.cache_data
    def predict(_self, age: int, is_male: bool, does_smoke: bool, weeks_since_scan: int, lung_capacity: float):
        return "You're fucked!" if does_smoke else "You're probably fine."