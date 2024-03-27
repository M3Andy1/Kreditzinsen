#Test file

import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

st.write('This script helps to predict loan costs for fixed and variable interest rates')

col1, col2 = st.columns(2)
with col1:
    st.write('Past Leitzins')
    ezb_image = st.image('./chart.jpeg')
    
    
with col2:
    st.write('Predicted Leitzins every 2 years')
    Start_zins=st.number_input('Start Leitzins 0')
    zins_2=st.slider('2', min_value=0, max_value=6)
    zins_4=st.slider('4', min_value=0, max_value=6)
    zins_6=st.slider('6', min_value=0, max_value=6)
    zins_8=st.slider('8', min_value=0, max_value=6)
    zins_10=st.slider('10', min_value=0, max_value=6)
    zins_12=st.slider('12', min_value=0, max_value=6)
    zins_14=st.slider('14', min_value=0, max_value=6)
    zins_16=st.slider('16', min_value=0, max_value=6)
    zins_18=st.slider('18', min_value=0, max_value=6)
    zins_20=st.slider('20', min_value=0, max_value=6)
    zins_22=st.slider('22', min_value=0, max_value=6)
    zins_24=st.slider('24', min_value=0, max_value=6)
    zins_26=st.slider('26', min_value=0, max_value=6)
    zins_28=st.slider('28', min_value=0, max_value=6)
    zins_30=st.slider('30', min_value=0, max_value=6)

predicted_EZB=[Start_zins,zins_2,zins_4,zins_6,zins_8,zins_10,zins_12,zins_14,zins_16,zins_18,zins_20,zins_22,zins_24,zins_26,zins_28,zins_30]
x_values = np.linspace(0, 30, 16)

df = pd.DataFrame({'X': x_values, 'Predicted EZB': predicted_EZB})

fig = px.line(df, x='X', y='Predicted EZB', title='Predicted EZB over Time')

# Display plot
st.plotly_chart(fig)