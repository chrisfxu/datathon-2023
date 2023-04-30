import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from models.rf_regressor_model import RandomForestRegressorModel
from scipy.interpolate import make_interp_spline


st.set_page_config(layout='wide')
st.title('Lung Function Forecaster :lungs:')
st.subheader('by Ken\'s Chiemps :monkey:', )

form, results, surf = st.columns([1, 2, 1])

with form:
    '### Answer these questions...'
    age = st.number_input('Age', min_value=18, max_value=122, step=1)
    gender = st.radio('Sex', ['Man', 'Woman'])
    smoking_status = st.radio('Do you smoke? :smoking:', ['Yes', 'No'])
    ct_scan = st.file_uploader('CT scan of lungs', type=['png', 'jpg'])
    weeks_since_scan = st.number_input('Weeks since CT scan', step=1, value=2)
    lung_capacity = st.number_input('Lung capacity at last checkup (mL)', value=2720)
    percent_capacity = st.number_input('Lung capacity at last checkup (%)', 0, 100, value=60)

@st.cache_resource
def get_model():
    return RandomForestRegressorModel()

model = get_model()

with results:
    '### Will your lungs be fine?'
    ages_projected = np.arange(age + 5, 123, 1)
    weeks_since_scan_projected = (ages_projected - age) * 52 + weeks_since_scan
    Y = []
    for i in range(len(ages_projected)):
        Y.append(model.predict(ages_projected[i], gender == 'Man', smoking_status == 'Yes', weeks_since_scan_projected[i], lung_capacity, percent_capacity)[0])
    #define x as 200 equally spaced values between the min and max of original x 
    xnew = np.linspace(ages_projected.min(), ages_projected.max(), 200) 

    #define spline with degree k=7
    spl = make_interp_spline(ages_projected, Y, k=9)
    y_smooth = spl(xnew)

    #create smooth line chart 
    plt.plot(xnew, y_smooth)
    # plt.plot(ages_projected, Y)
    plt.xlabel('Age (years)')
    plt.ylabel('Projected Lung Capacity (mL)')
    st.pyplot(plt)

with surf:
    #st.markdown(r"![Doctors Hate This One Simple Trick!](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.RkJFdQILTedyGsDtxLQq6gAAAA%26pid%3DApi&f=1&ipt=443df8bcabc60c25c19a73158b7031be13a4008845ef4ee2d4973afe9197c6c6&ipo=images)")
    #st.markdown(r"![Hot Singles In Your Area](https://i1.sndcdn.com/artworks-PyA0dgP4Tz0yv7zz-Fx2Qlg-t240x240.jpg)")
    st.markdown(r"![Subway Surf](https://media.tenor.com/1wZ88hrB5SwAAAAd/subway-surfer.gif)")
