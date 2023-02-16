import streamlit as st
import pandas as pd
import numpy as np
import joblib
import webbrowser

# not sure if needed
from PIL import Image


st.sidebar.image('images/jf.jpeg', use_column_width='always') # my pic
st.sidebar.header('Jonathan B. Fetterolf')
st.sidebar.caption('''Data Scientist based out of Alexandria, VA. Interested in complex problem solving, machine learning, statistical analysis and new technology surrounding the data world.''')

st.sidebar.header('Contact Info')
# Contact info links
st.sidebar.write('''[Malaria Repository](https://github.com/fetterollie/Malaria-Data-Exploration)''')
#gh_button = st.sidebar.button('GitHub')
#if gh_button:    
#    webbrowser.open_new_tab(https://github.com/fetterollie)
st.sidebar.write('''[GitHub](https://github.com/fetterollie)''')
#li_button = st.sidebar.button('LinkedIn')
#if li_button:    
#   webbrowser.open_new_tab(https://www.linkedin.com/in/jonathanfetterolf/)
st.sidebar.write('''[LinkedIn](https://dev.to/fetterollie)''')
#dt_button = st.sidebar.button('Blog')
#if dt_button:
#    webbrowser.open_new_tab(https://dev.to/fetterollie)
st.sidebar.write('''[Blog](https://dev.to/fetterollie)''')
#tw_button = st.sidebar.button('Twitter')
#if tw_button:    
#    webbrowser.open_new_tab(https://twitter.com/fetterollie)
st.sidebar.write('''[Twitter](https://twitter.com/fetterollie)''')

st.title('Malaria Prediction Application')
st.image('images/mal_cells.jpg', use_column_width='always')

st.header('About the Project')
st.write('''According to the latest [World Malaria Report](https://www.who.int/publications/i/item/9789240064898) published by the [World Health Organization](https://www.who.int/news-room/fact-sheets/detail/malaria), there were 247 million cases of malaria in 2021 compared to 245 million cases in 2020. The estimated number of malaria deaths stood at 619,000 in 2021 compared to 625,000 in 2020. An early diagnosis and subsequently early treatment of malaria will help doctors practicing in araea with high rates of malaria infection and malaria deaths. Four African countries accounted for over half of all malaria deaths worldwide: Nigeria (31.3%), the Democratic Republic of the Congo (12.6%), United Republic of Tanzania (4.1%) and Niger (3.9%).''')
st.write('''The [WHO | Regional Office for Africa](https://www.afro.who.int/health-topics/malaria) recognizes that malaria is going undiagnosed and subsequently untreated in areas where the parasite is prevalent and the resources to diagnose and treat it are the lowest. The WHO wants to create a model that can accurately predict whether or not a cell from stained blood smear is infected with malaria in order to more effectively diagnose and treat malaria in the population. ''')
st.write('''This application can save lives. According to the [CDC](https://www.cdc.gov/malaria/diagnosis_treatment/clinicians1.html#:~:text=The%20preferred%20antimalarial%20for%20interim,not%20adequate%20for%20interim%20treatment.): in an ideal situation malaria treatment should not be initiated until the diagnosis has been established by laboratory testing. “Presumptive treatment”, i.e., without prior laboratory confirmation, should be reserved for extreme circumstances, such as strong clinical suspicion of severe disease in a setting where prompt laboratory diagnosis is not available. Doctors will still be needed to take blood and provide treatments. Histologists will still be required to prepare slides and confirm the diagnoses. This technology will simply make their operations more effiecient and allow them to dianose and treat more patients.''')
