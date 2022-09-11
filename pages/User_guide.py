import streamlit as st
import os
from PIL import Image
st.title('USER GUIDE')
st.write('''This brief user guide will help you go thorugh all the steps you need to get 
linechart for airway management from EMS data.  Please check this page carefully if you 
meet any trouble when using the application. Thanks!''')
st.sidebar.info(
    '''
    User requirement: \n
    For researcher who needs a handy tool for visualization of time series trend of EMS airway managements. 
    '''
)
st.sidebar.error(
    '''
    Caution:\n
    Please cite this webpage before sharing the figures, thanks.
    '''
    )

st.markdown("### --- Step 0: About our app ---")
st.write('This application would help you to visualize the trends of pre-hospital airway management. \
    The app will produce two linecharts and one barchart. The first linechart contains info of time \
    versus counts of selected airway management. The second one visualized the trends in a "ratio" manner. \
    Finally, we provide a barchart showing frequency as each category of airway management in specific city.')
st.markdown('''The five categories used in barchart:
1. Advanced airway: 'SGA', 'Endo'
2. Advanced oxygenation: 'BVM', 'Nebulizer_mask'
3. Basic airway: 'Oral_airway', 'Nasal_airway'
4. Basic oxygenation: 'Nasal_cannula', 'Mask', 'NRM'
5. Others: 'Aspirate', 'Heimlich', 'Others'
''')
st.markdown("### --- Step 1: Set the time period ---")
st.write('Please select the time period of data. The application would automatically extract the statistics\
 from the time span you assigned. The minimal timestamp is 2013/01 and the maximum is 2022/06.')
time_period = Image.open(os.path.dirname(__file__)+'/user_guide_images/time_period.JPG')
st.image(time_period, caption='')

st.markdown("### --- Step 2: Select the type of airway management ---")
st.write('Please choose the insterested airway management to be analyzed.')
airway_type = Image.open(os.path.dirname(__file__)+'/user_guide_images/airway_type.JPG')
st.image(airway_type, caption='')

st.markdown("### --- Step 3: Select the additional cities(Counties) and one specific city for bar chart ---")
st.write('''
1. Select the cities to be included in linecharts in addition to six municipalities.
2. Choose one specific city for the categorical ratio stacked barchart.
''')
target_city = Image.open(os.path.dirname(__file__)+'/user_guide_images/target_city.JPG')
st.image(target_city, caption='')

st.markdown("### --- Step 4: Start visualization ---")
st.write('''After finishing all the question, you could get your result by press
the "Start Data Visualization" button just below the questionnaire block.
''')
st.write('''You may wait for a few seconds before the result block shows up. 
There would be a blue progress bar indicating our application is alive.''')
start_viz = Image.open(os.path.dirname(__file__)+'/user_guide_images/start_viz.JPG')
st.image(start_viz, caption='')

st.markdown("### --- Step 5: Check your result ---")
st.write('''Now your result is avaliable. You will see two linecharts and one barcharts. 
Thanks you very much!''')
result_1 = Image.open(os.path.dirname(__file__)+'/user_guide_images/result_1.JPG')
st.image(result_1, caption='')
result_2 = Image.open(os.path.dirname(__file__)+'/user_guide_images/result_2.JPG')
st.image(result_2, caption='')
result_3 = Image.open(os.path.dirname(__file__)+'/user_guide_images/result_3.JPG')
st.image(result_3, caption='')