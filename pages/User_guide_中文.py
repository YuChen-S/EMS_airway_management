import streamlit as st
import os
from PIL import Image
st.title('使用說明書')
st.write('''本頁將快速說明如何使用本視覺化工具，謝謝。''')
st.sidebar.info(
    '''
    User requirement: \n
    For researcher who needs a handy tool for visualization of time series trend of EMS managements. 
    '''
)
st.sidebar.error(
    '''
    Caution:\n
    Please cite this webpage before sharing the figures, thanks.
    '''
    )

st.markdown("### --- Step 0: 關於本工具 ---")
st.markdown(
    '''本工具可協助您以視覺化方式呈現本國到院前處置的統計資料。  
    本工具可繪製兩張折線圖，若選擇氣道相關之處置，會再產生一張額外的柱狀圖。   
    第一張折線圖將呈現處置次數與時間的關係；而第二張則呈現處置比例與時間的關係。
    柱狀圖則是針對選擇的地區，呈現各氣道分級(初階/進階)之比重與時間的關係。
    '''
    )


st.markdown("### --- 步驟 1 : 選擇時間 ---")
st.write('選擇預分析的時間區段。可選擇之最初時間點為2013/01；而最終時間點為2022/06。')
time_period = Image.open(os.path.dirname(__file__)+'/user_guide_images/time_period.JPG')
st.image(time_period, caption='')

st.markdown("### --- 步驟 2 : 選擇到院前處置的類型以及處置名稱 ---")
st.markdown('''共四類到院前處置可供選擇: 1.呼吸道相關 2.創傷保護措施 3.心肺復甦術 4.藥物相關。''')
st.write('選擇完類型後，系統會自動切換對應到的處置清單，再勾選欲分析的處置即可。')
airway_type = Image.open(os.path.dirname(__file__)+'/user_guide_images/airway_type.JPG')
st.image(airway_type, caption='')

st.markdown("### --- 步驟 3 : 選擇欲分析的地區 ---")
st.write('''
1. 選擇欲分析的直轄市(必填)。
2. 選擇其他欲分析的縣市(選填)。
2. 若步驟2選擇呼吸道相關處置，則須再選擇一地區進行柱狀圖之分析。
''')
st.markdown('''柱狀圖中，會將處置區分成五個類別，並計算各類別的占比:
1. 進階呼吸道(Advanced airway): '*SGA*', '*Endo*'
2. 進階給氧方式(Advanced oxygenation): '*BVM*', '*Nebulizer_mask*'
3. 初階呼吸道(Basic airway): '*Oral_airway*', '*Nasal_airway*'
4. 初階給氧方式(Basic oxygenation): '*Nasal_cannula*', '*Mask*', '*NRM*'
5. 其他(Others): '*Aspirate*', '*Heimlich*', '*Others*' )
''')
target_city = Image.open(os.path.dirname(__file__)+'/user_guide_images/target_city.JPG')
st.image(target_city, caption='')

st.markdown("### --- 步驟 4 : 進行資料視覺化 ---")
st.write('''填寫完前述個條件後，請點選"Start Data Visualization"按鈕，開始分析。''')
st.write('''分析時會顯示進度條，請稍等數秒後查看結果。''')
start_viz = Image.open(os.path.dirname(__file__)+'/user_guide_images/start_viz.JPG')
st.image(start_viz, caption='')

st.markdown("### --- 步驟 5 : 檢視結果圖表 ---")
st.write('''可獲得兩張折線圖，若選擇呼吸道相關處置，可會額外再產生一張柱狀圖''')
st.write('''折線圖中會以代號方式呈現數個重大疫情事件，代號與對應的事件如下圖所示''')
covid_event = Image.open(os.path.dirname(__file__)+'/user_guide_images/covid_event.JPG')
st.image(covid_event, caption='')
result_1 = Image.open(os.path.dirname(__file__)+'/user_guide_images/result_1.JPG')
st.image(result_1, caption='折線圖: 事件次數')
result_2 = Image.open(os.path.dirname(__file__)+'/user_guide_images/result_2.JPG')
st.image(result_2, caption='折線圖: 事件比率')
result_3 = Image.open(os.path.dirname(__file__)+'/user_guide_images/result_3.JPG')
st.image(result_3, caption='柱狀圖: 呼吸道處置類別比率')
st.write('''  註: 柱狀圖中之黑色折線為 *該城市之呼吸道處置總數 / 全國之呼吸道處置總數* ''')