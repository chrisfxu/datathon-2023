import streamlit as st


@st.cache_data
def predict(age: int, is_male: bool, does_smoke: bool, weeks_since_scan: int, weeks_since_checkup: int, lung_capacity: int) -> str:
    return "You're fucked!" if does_smoke else "You're probably fine."