#Test file

import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

st.write('This script helps to predict loan costs for fixed and variable interest rates')

col1, col2 = st.columns(2)

st.write('Past Leitzins')
ezb_image = st.image('./chart.jpeg')
st.write('Predicted Leitzins every 2 years') 
with col1:
    Start_zins=st.number_input('Start Leitzins 0')
    zins_2=st.number_input('2')
    zins_4=st.number_input('4')
    zins_6=st.number_input('6')
    zins_8=st.number_input('8')
    zins_10=st.number_input('10')
    zins_12=st.number_input('12')
    zins_14=st.number_input('14')
    
with col2:

    zins_16=st.number_input('16')
    zins_18=st.number_input('18')
    zins_20=st.number_input('20')
    zins_22=st.number_input('22')
    zins_24=st.number_input('24')
    zins_26=st.number_input('26')
    zins_28=st.number_input('28')
    zins_30=st.number_input('30')

predicted_EZB=[Start_zins,zins_2,zins_4,zins_6,zins_8,zins_10,zins_12,zins_14,zins_16,zins_18,zins_20,zins_22,zins_24,zins_26,zins_28,zins_30]
x_values = np.linspace(0, 30, 16)



df = pd.DataFrame({'X': x_values, 'Predicted EZB': predicted_EZB})

st.line_chart(df, x="X", y="Predicted EZB")