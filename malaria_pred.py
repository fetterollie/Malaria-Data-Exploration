import streamlit as st
import pandas as pd
import numpy as np


# not sure if needed
from PIL import Image

st.sidebar.title('Menu')
st.sidebar.image('images/header.jpeg', use_column_width='always')


st.title('Predicting Malaria')

button1 = st.button('Click')
if button1:
    st.write('You clicked me')

"LOL OKAY"

test_input = st.number_input('Enter Age')
st.write(f'You are {test_input} years old.')
st.write(type(test_input))

num_pets = st.slider('How many pets do you have?', step=5)

'asdf'