import streamlit as st


st.title('Lung Function Forecaster :lungs:')
st.subheader('by Ken\'s Chiemps :monkey:', )

'Please upload a CT scan of your lungs and input your age and smoking status!'

age = st.slider('Age', min_value=18, max_value=122, step=1)
gender = st.radio('Sex', ['Man', 'Woman'])
smoking_status = st.radio('Do you smoke? :smoking:', ['Yes', 'No'])
ct_scan = st.file_uploader('CT scan of lungs', type=['png', 'jpg'])
since_scan = st.number_input('Weeks since CT scan', step=1)
since_checkup = st.number_input('Weeks since last checkup', step=1)
lung_capacity = st.number_input('Lung capacity at last checkup (mL)')