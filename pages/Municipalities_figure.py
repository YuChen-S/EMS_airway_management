import streamlit as st
import os
from PIL import Image
st.markdown('## This page provides several line charts of pre-hospital airway management in municipalities.')
st.write('''Use the datavisualizer to create figures including more cities. Thanks!''')

st.sidebar.info(
    '''
    Demo page\n
    '''
)

cannula_line = Image.open(os.path.dirname(__file__)+'/municipalities_figures/cannula_line_2016_2022.png')
st.image(cannula_line, caption='')

mask_line = Image.open(os.path.dirname(__file__)+'/municipalities_figures/mask_line_2016_2022.png')
st.image(mask_line, caption='')

bvm_line = Image.open(os.path.dirname(__file__)+'/municipalities_figures/bvm_line_2016_2022.png')
st.image(bvm_line, caption='')

sga_line = Image.open(os.path.dirname(__file__)+'/municipalities_figures/sga_line_2016_2022.png')
st.image(sga_line, caption='')