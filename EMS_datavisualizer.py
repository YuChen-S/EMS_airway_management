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
        start_year = st.selectbox('The start year: ', year_list, index=5)
    with user_col_1_2:
        month_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        start_month = st.selectbox('The start month: ', month_list, index=5)
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
    st.subheader('Please select the field of management and a specific procedure')
    user_col_3_1, user_col_3_2 = st.columns(2)
    management_dic = {
        'Airway':['口咽呼吸道', '鼻咽呼吸道', '抽吸', '鼻管', '面罩', '非再呼吸型面罩', 'BVM', 'SGA', '氣管內管', '霧化吸入型面罩', 
                        '哈姆立克法', '其他',], 
        'Trauma':['頸圈', '清洗傷口', '包紮止血', '長背板固定', '鏟式擔架固定', 'KED固定', '骨折固定', '夾板固定'], 
        'CPR':['CPR', '使用AED/不建議電擊', '使用AED/電擊',], 
        'Drug':['靜脈輸液', '口服葡萄糖', '建議給藥']}
    with user_col_3_1:
        management_type = st.selectbox('The field of management', list(management_dic.keys()), index=0)
    with user_col_3_2:
        procedure_name = st.selectbox('The procedure', management_dic[management_type], index=0)
    st.warning('The selected management: ' + '**_' + procedure_name + '_**')
    st.write('---')

    # fourth row
    st.subheader('Please select the target cities for line chart')
    user_col_4_1, user_col_4_2 = st.columns(2)
    municipalities = ['新北市', '臺北市', '桃園市', '臺中市', '臺南市', '高雄市', ]
    city_name = ['宜蘭縣', '新竹縣', '苗栗縣', '彰化縣', '南投縣', '雲林縣', '嘉義縣', '屏東縣', '臺東縣', '花蓮縣', \
        '澎湖縣', '基隆市', '新竹市', '嘉義市', '金門縣', '連江縣']
    with user_col_4_1:
        municipality = st.multiselect('Municipalities for linechart', municipalities, ['新北市'])
        st.warning(f'The municipalities for line chart : **_{municipality}_**.')
    with user_col_4_2:
        additional_city = st.multiselect('Additional city for linechart: ', city_name, ['嘉義市'])
        st.warning(f'The additional cities for line chart : **_{additional_city}_**')
    st.write('---')
    # fifth row
    primary_city = '新北市'
    if management_type == 'Airway':
        st.subheader('Please select the target city for stacked bar chart')
        user_col_5_1, user_col_5_2 = st.columns(2)
        with user_col_5_1:
            primary_city = st.selectbox('The specific city for stacked bar chart: ', municipalities+city_name, index=0)
            st.warning(f'The city for bar chart : **_{primary_city}_**')
###### Model prediction ######
submit = st.button("Start Data Visualization")
show_result = False
with st.container():
    if submit:
        my_bar = st.progress(0)
        # start_time='2016/01', end_time='2022/06', category='Airway', procedure='Mask', municipality=['臺北市',], primary_city='新北市', additional_city=[]
        fig, fig_bar, fig_ratio = generate_municipality_line(start_time, end_time, management_type, procedure_name, municipality, primary_city, additional_city, )
        for percent_complete in range(100):
             time.sleep(0.02)
             my_bar.progress(percent_complete + 1)
        
        st.success('Thanks for waiting, please check your result!')
        st.write('---')
        show_result = True

###### Result block ######
if show_result:
    with st.container():
        st.markdown("##### Key COVID-19 events")
        st.write(
            '''
            A: 2019/12: **Wuhan Pandemics**\n
            B: 2020/01: **NHCC set up**\n
            C: 2021/01: **Taoyuan Hospital Cluster**\n
            D: 2021/05: **North Taiwan Level 3 Alert**\n
            E: 2021/07: **National Level 2 Alert**\n
            F: 2022/03: **Omicron Outbreak**
            ''')
        st.subheader('Linechart of event counts versus time:')
        st.pyplot(fig, clear_figure=True, figsize=(15, 3))
        st.subheader('Linechart of event ratio versus time:')
        st.pyplot(fig_ratio, clear_figure=True, figsize=(15, 3))
        if management_type == 'Airway':
            st.subheader('Barchart of categorical ratio versus time:')
            st.pyplot(fig_bar, clear_figure=True, figsize=(15, 3))
###### health education block ######
