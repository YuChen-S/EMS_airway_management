import time
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import joblib
import tqdm
import sklearn
from utils import *

###### webpage settings ######
st_website_setting()

###### sidebar info ######
st_sidebar_info()

###### Main page title and user guide
st_title_info()

###### user info block ######
with st.container():
    st.subheader('Please select the time period')
    # first row
    user_col_1_1, user_col_1_2 = st.columns(2)
    with user_col_1_1:
        year_list = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
        start_year = st.selectbox('The start year: ', year_list, index=3)
    with user_col_1_2:
        month_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        start_month = st.selectbox('The start month: ', month_list, index=0)
    start_time = str(start_year) + '/' + str(start_month)
    # second row
    user_col_2_1, user_col_2_2 = st.columns(2)
    with user_col_2_1:
        end_year = st.selectbox('The end year: ', year_list, index=len(year_list)-1)
    with user_col_2_2:
        end_month = st.selectbox('The end month: ', month_list, index=5)
    end_time = str(end_year) + '/' + str(end_month)
    if end_year == '2022' and int(end_month) > 6:
        end_time = '2022/06'
    st.warning(f'Time period: **_{start_time} ~ {end_time}_**')
    st.write('---')
    # third row
    st.subheader('Please select the type of airway management to be analyzed')
    user_col_3_1, user_col_3_2 = st.columns(2)
    airway_names = ['Oral_airway', 'Nasal_airway', 'Aspirate', 'Nasal_cannula', 'Mask', 'NRM', 'BVM', \
        'SGA', 'Endo', 'Nebulizer_mask', 'Heimlich', 'Others']
    with user_col_3_1:
        airway_type = st.selectbox('The airway managements', airway_names, index=4)
    with user_col_3_2:
        st.write(' ')
    st.warning('The selected airway management: ' + '**_' + airway_type + '_**')
    st.write('---')
    # fourth row
    st.subheader('Please select the city for bar chart and additional cities for line chart')
    user_col_4_1, user_col_4_2 = st.columns(2)
    municipality = ['新北市', '臺北市', '桃園市', '臺中市', '臺南市', '高雄市', ]
    city_name = ['宜蘭縣', '新竹縣', '苗栗縣', '彰化縣', '南投縣', '雲林縣', '嘉義縣', '屏東縣', '臺東縣', '花蓮縣', \
        '澎湖縣', '基隆市', '新竹市', '嘉義市', '金門縣', '連江縣']
    with user_col_4_1:
        additional_city = st.multiselect('Additional cities to be included in linechart', city_name, [])
        st.warning(f'The additional cities for line chart : **_{additional_city}_**.')
    with user_col_4_2:
        primary_city = st.selectbox('The specific city for stacked bar chart: ', municipality+city_name, index=0)
        st.warning(f'The specific city for bar chart : **_{primary_city}_**')
st.write('---')

###### Model prediction ######
submit = st.button("Start Data Visualization")
show_result = False
with st.container():
    if submit:
        my_bar = st.progress(0)
        fig, fig_bar, fig_ratio = generate_municipality_line(start_time, end_time, airway_type, primary_city, additional_city, )
        for percent_complete in range(100):
             time.sleep(0.02)
             my_bar.progress(percent_complete + 1)
        
        st.success('Thanks for waiting, please check your result!')
        st.write('---')
        show_result = True

###### Result block ######
if show_result:
    with st.container():
        st.subheader('Linechart of event counts versus time:')
        st.pyplot(fig, clear_figure=True, figsize=(15, 3))
        st.subheader('Linechart of event ratio versus time:')
        st.pyplot(fig_ratio, clear_figure=True, figsize=(15, 3))
        st.subheader('Barchart of categorical ratio versus time:')
        st.pyplot(fig_bar, clear_figure=True, figsize=(15, 3))
###### health education block ######
