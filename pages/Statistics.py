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



descriptive_stat = Image.open(os.path.dirname(__file__)+'/statistic_figures/descriptive_stat.jpg')
st.image(descriptive_stat, caption='')

paired_t_test = Image.open(os.path.dirname(__file__)+'/statistic_figures/paried_t_test_top5.jpg')
st.image(paired_t_test, caption='')

# chi2_ = Image.open(os.path.dirname(__file__)+'/municipalities_figures/Chi square test for Mask from all city.jpg')
# st.image(chi2_mask, caption='')