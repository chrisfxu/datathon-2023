import streamlit as st
from models.stub_model import StubModel


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
    weeks_since_scan = st.number_input('Weeks since CT scan', step=1)
    weeks_since_checkup = st.number_input('Weeks since last checkup', step=1)
    lung_capacity = st.number_input('Lung capacity at last checkup (mL)')

@st.cache_resource
def get_model():
    return StubModel()

model = get_model()

with results:
    '### Will your lungs be fine?'
    st.write(model.predict(age, gender == 'Man', smoking_status == 'Yes', weeks_since_scan, weeks_since_checkup, lung_capacity))

with surf:
    st.markdown("![Alt Text](https://media.tenor.com/1wZ88hrB5SwAAAAd/subway-surfer.gif)")
