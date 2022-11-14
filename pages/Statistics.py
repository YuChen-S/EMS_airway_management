import streamlit as st
import os
from PIL import Image
st.markdown('## Results of statistic analysis.')
st.write('''''')

st.sidebar.info(
    '''
    Demonstation of statistic analysis\n
    '''
)

paired_t_test = Image.open(os.path.dirname(__file__)+'/municipalities_figures/paired_t_test.png')
st.image(paired_t_test, caption='')

