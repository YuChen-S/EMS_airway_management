import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import streamlit as st
import os

def st_website_setting():
    st.set_page_config(
        page_title="Webpage title",
        page_icon="random",
        layout="centered",
        initial_sidebar_state="auto",
    )

def st_sidebar_info():
    with st.sidebar:
        st.title("About")
        st.info(
            """
            EMS(Emergent Medical Service) data analysis in Taiwan。\n
            Data : 消防緊急救護急救處置─按區域別分\n
            Data link: https://data.gov.tw/dataset/12097
            """
        )
        st.title("Contact")
        st.info(
            """
            Team: 
            [Yu Chen Shen](), 
            [](), \n
            Director: [Chao-Wen Chen]
            """
        )
        st.success("Contact zoro6mihawk@gmail.com if any problem was found, thanks")
        st.write('''---''')

def st_title_info():
    st.title('Taiwan EMS Data Visualizer')
    st.subheader(
    '''
    This application will help you to create linecharts for time versus counts of each airway management in EMS system.
    ''', anchor=None)
    st.write('Thanks for using our product!')
    st.write('---')

def year_month_delta(start_time='2016/01', end_time='2022/06'):
    return 12*(pd.to_datetime(end_time).year - pd.to_datetime(start_time).year) + \
        (pd.to_datetime(end_time).month - pd.to_datetime(start_time).month)

def generate_municipality_line(start_time='2016/01', end_time='2022/06', airway_type='Mask', additional_city=[]):
    '''
    This function would generate a multiple line plot based on "消防緊急救護急救處置─按區域別分" dataset labeled by municipality or other additional cities.

    start_time: str, format as 'yyyy/mm', the start timepoint of line plot, the earliest timestamp is '2013/01', default '2016/01'
    end_time: str, format as 'yyyy/mm', the end timepoint of line plot, the lastest timestamp is '2022/06', default '2022/06'
    airway: str, one of ['Oral_airway', 'Nasal_airway', 'Aspirate', 'Nasal_cannula', 'Mask', 'NRM', 'BVM', 'SGA', 'Endo', 'Nebulizer_mask', 'Heimlich', 'Others'], default 'Mask'
    additional_city: str, additional cities besides the six municipalities, add them into the line plot, defualt [], which means only plot the six municipalities
    '''

    ### Read file and basic index / column
    file_path = os.path.join(os.getcwd(), 'EMS_management_by_city.csv')
    df_taiwan = pd.read_csv(file_path,)
    start_time = start_time
    end_time = end_time
    year_index = 351 # if 2016 -> iloc[351*3:, :]
    target_city = '新北市|臺北市|桃園市|臺中市|臺南市|高雄市' if additional_city==[] else '新北市|臺北市|桃園市|臺中市|臺南市|高雄市'+'|'+'|'.join(additional_city)
    target_city = target_city.replace("台", "臺")
    airway_columns = ['消防緊急救護急救處置', '總次數', '呼吸道處置', '口咽呼吸道', '鼻咽呼吸道', '抽吸', '鼻管', '面罩', '非再呼吸型面罩', 'BVM', 'SGA', '氣管內管', '霧化吸入型面罩', 
                      '哈姆立克法', '其他',]
    airway_names = ['total_service_count', 'airway_manage_count', 'Oral_airway', 'Nasal_airway', 'Aspirate', 'Nasal_cannula', 'Mask', 'NRM', 'BVM', 'SGA', 'Endo', 'Nebulizer_mask', 
                    'Heimlich', 'Others']
    df_taiwan = df_taiwan.loc[351*(int(start_time[0:4])-2013):, airway_columns]
    df_taiwan = df_taiwan[df_taiwan['消防緊急救護急救處置'].str.contains(target_city)]
    df_taiwan = df_taiwan[df_taiwan['消防緊急救護急救處置'].str.contains('月')]
    df_taiwan = df_taiwan[~df_taiwan['消防緊急救護急救處置'].str.contains('br')]
    df_taiwan.rename(columns = {'消防緊急救護急救處置':'year_month_city', '總次數':'total_service_count', '呼吸道處置':'airway_manage_count', '口咽呼吸道':'Oral_airway', '鼻咽呼吸道':'Nasal_airway', 
                '抽吸':'Aspirate', '鼻管':'Nasal_cannula', '面罩':'Mask', '非再呼吸型面罩':'NRM', '氣管內管':'Endo', '霧化吸入型面罩':'Nebulizer_mask','哈姆立克法': 'Heimlich', 
                '其他': 'Others'}, inplace = True)
    df_taiwan.replace('-', 0, inplace=True)
    for column in airway_names:
        try:
            df_taiwan[column] = df_taiwan[column].str.replace(',', '').fillna(0).astype('int64')
        except:
            pass
    city_name = {'新北市':'New Taipei', '臺北市':'Taipei City', '桃園市':'Taoyuan City', '臺中市':'Taichung City', '臺南市':'Tainan City', '高雄市':'Kaohsiung City', '宜蘭縣':'Yilan County', 
                '新竹縣':'Hsinchu County', '苗栗縣':'Miaoli County', '彰化縣':'Changhua County', '南投縣':'Nantou County', '雲林縣':'Yunlin County', '嘉義縣':'Chiayi County', 
                 '屏東縣':'Pingtung County', '臺東縣': 'Taitung County', '花蓮縣':'Hualien County', '澎湖縣':'Penghu County', '基隆市':'Keelung City', '新竹市':'Hsinchu City', 
                 '嘉義市':'Chiayi City', '金門縣':'Kinmen County', '連江縣':'Lienchiang County'}
    df_taiwan['year_month_city'] = df_taiwan['year_month_city'].apply(lambda x:str(int(x.split(' ')[0][0:3])+1911) + '-' + x.split(' ')[1][:-2] + ' ' + city_name[x.split(' ')[-1]])
    df_taiwan.reset_index(inplace=True)

    ### Data correction
    # data loss at Taichung City 202203
    df_taiwan.iloc[df_taiwan[df_taiwan['year_month_city']=='2022-3 Taichung City'].index[0], 2:] = (df_taiwan[df_taiwan['year_month_city']=='2022-2 Taichung City'].iloc[0, 2:] \
                                                    + df_taiwan[df_taiwan['year_month_city']=='2022-4 Taichung City'].iloc[0, 2:]) // 2
    # data saved in wrong column (Nasal nanuula <-> Mask) at New Taipei 202009
    new_taipei_202009_index = df_taiwan[df_taiwan['year_month_city']=='2020-9 New Taipei'].index[0]
    df_taiwan.iloc[new_taipei_202009_index, 7], df_taiwan.iloc[new_taipei_202009_index, 8] = df_taiwan.iloc[new_taipei_202009_index, 8], df_taiwan.iloc[new_taipei_202009_index, 7]

    ### Plot the figure
    plt.style.use('seaborn-darkgrid')
    fig = plt.figure(figsize=(40, 15),)
    month_period = year_month_delta(start_time=start_time, end_time=end_time)+1
    x = pd.Series(pd.period_range(start_time, freq='M', periods=month_period)).astype('str')
    plt.plot(x, df_taiwan[df_taiwan.year_month_city.str.contains('Kaohsiung')][airway_type], label='Kaohsiung', linestyle='-', marker='o', color='tab:red', alpha=0.8)
    plt.plot(x, df_taiwan[df_taiwan.year_month_city.str.contains('New')][airway_type], label="New Taipei", linestyle='--', marker='o', color='tab:blue', alpha=0.8,)
    plt.plot(x, df_taiwan[df_taiwan.year_month_city.str.contains('Taipei City')][airway_type], label='Taipei', linestyle='--', marker='o', color='tab:cyan', alpha=0.8)
    plt.plot(x, df_taiwan[df_taiwan.year_month_city.str.contains('Taoyuan')][airway_type], label='Taoyuan', linestyle='--', marker='o', color='tab:orange', alpha=0.8)
    plt.plot(x, df_taiwan[df_taiwan.year_month_city.str.contains('Taichung')][airway_type], label='Taichung', linestyle='-.', marker='.', color='tab:green', alpha=0.8)
    plt.plot(x, df_taiwan[df_taiwan.year_month_city.str.contains('Tainan')][airway_type], label='Tainan', linestyle='-.', marker='.', color='limegreen', alpha=0.8)

    if additional_city:
        colors = plt.cm.Dark2(np.linspace(0, 1, len(additional_city)))
        for index, city in enumerate(additional_city):
            city = city.replace("台", "臺")
            try:
                plt.plot(x, df_taiwan[df_taiwan.year_month_city.str.contains(city_name[city])][airway_type], label=city_name[city], \
                         linestyle=':', marker='*', color=colors[index], alpha=0.8)
            except:
                pass

    plt.title('EMS data from municipalities: Oxygen from ' + airway_type, fontsize=24)
    plt.xlabel('Year-Month', fontsize=20)
    plt.ylabel('Event counts', fontsize=20)
    plt.xticks(rotation=-30)
    plt.legend(fontsize=20, loc='upper left', frameon=True, facecolor='white', markerscale=1.5, ncol=2)
    ylim = fig.gca().get_ylim()

    ### COVID-19 events
    text_y_interval = (ylim[1]/1450)*60
    text_line_interval = (ylim[1]/1450)*10
    # 2019/12: Wuhan Pandemics
    plt.vlines(year_month_delta(start_time=start_time, end_time='2019/12'), ylim[0], ylim[1]+text_y_interval, linestyle=':', color='darkgrey', alpha=0.5)
    plt.text(year_month_delta(start_time=start_time, end_time='2019/12'), ylim[1]+text_y_interval+text_line_interval, '2019/12:Wuhan Pandemics', fontsize=16)
    # 2020/01: NHCC set up
    plt.vlines(year_month_delta(start_time=start_time, end_time='2020/01'), ylim[0], ylim[1], linestyle=':', color='darkgrey', alpha=0.5)
    plt.text(year_month_delta(start_time=start_time, end_time='2020/01'), ylim[1]+text_line_interval, '2020/01:NHCC set up', fontsize=16)
    # 2020/02: Announcement to EMS
    plt.vlines(year_month_delta(start_time=start_time, end_time='2020/02'), ylim[0], ylim[1]-text_y_interval, linestyle=':', color='red', alpha=0.8)
    plt.text(year_month_delta(start_time=start_time, end_time='2020/02'), ylim[1]-text_y_interval+text_line_interval, '2020/02:Announcement to EMS', fontsize=16)
    # 2021/01: Taoyuan General Hospital\ncluster infection
    plt.vlines(year_month_delta(start_time=start_time, end_time='2021/01'), ylim[0], ylim[1]+text_y_interval, linestyle=':', color='red', alpha=0.8)
    plt.text(year_month_delta(start_time=start_time, end_time='2021/01'), ylim[1]+text_y_interval+text_line_interval, '2021/01:Taoyuan Hospital Cluster', fontsize=16)
    # 2021/05: Northern Taiwan\nPandemics & Level III alert
    plt.vlines(year_month_delta(start_time=start_time, end_time='2021/05'), ylim[0], ylim[1], linestyle=':', color='red', alpha=0.8)
    plt.text(year_month_delta(start_time=start_time, end_time='2021/05'), ylim[1]+text_line_interval, '2021/05:North Taiwan Level 3 alert', fontsize=16)
    # 2021/07: Reopen to\nLevel II alert
    plt.vlines(year_month_delta(start_time=start_time, end_time='2021/07'), ylim[0], ylim[1]-text_y_interval, linestyle=':', color='green', alpha=0.5)
    plt.text(year_month_delta(start_time=start_time, end_time='2021/07'), ylim[1]-text_y_interval+text_line_interval, '2021/07:Level 2 alert', fontsize=16)
    # 2022/03: Omicron Outbreak
    plt.vlines(year_month_delta(start_time=start_time, end_time='2022/03'), ylim[0], ylim[1]+text_y_interval, linestyle=':', color='red', alpha=0.8)
    plt.text(year_month_delta(start_time=start_time, end_time='2022/03'), ylim[1]+text_y_interval+text_line_interval, '2022/03:Omicron', fontsize=16)
    
    return fig