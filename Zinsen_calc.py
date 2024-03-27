#Test file

import streamlit as st
from PIL import Image

st.write('This script helps to predict loan costs for fixed and variable interest rates')

ezb_image = st.file_uploader('./chart.jpeg', type='jpeg', key=6)
if ezb_image is not None:
    image = Image.open(ezb_image)
    new_image = image.resize((600, 400))
    st.image(new_image)


