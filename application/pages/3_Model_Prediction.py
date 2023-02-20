import streamlit as st
import pandas as pd
import numpy as np
import pickle
import tensorflow as tf
import tensorflow.keras

st.title('Model Prediction')

st.write('1. Click "Browse files" and select desired image')
st.write('2. Upload the image by clicking "Submit Image"')
st.write('3. If you are satisfied with your image click "Make Prediction"')

@st.cache_resource()
def load_model():
    with st.spinner('Loading Model...'):
        model = tf.keras.models.load_model('model5.h5')
        return model
    
malaria_model = load_model()

st.sidebar.title('Forms')
form1 = st.sidebar.form(key='Input')

image_upload = form1.file_uploader(label='Upload Image to Predict', type='png')

form_button = form1.form_submit_button('Submit Image')
if form_button:
    st.text('Uploaded Image')
    st.image(image_upload)  

predict_button = st.button('Make Prediction')
if predict_button:
    imdim = 64
    img = tf.keras.utils.load_img(image_upload)
    inp_arr = tf.keras.utils.img_to_array(img) # convert to array
    mod_arr = np.array([inp_arr]) # convert to batch structure

    resize = tf.keras.layers.Resizing(imdim, imdim) # resize
    resized = resize(mod_arr)

    pred_class = None #initiate class placeholder
    pred = malaria_model.predict(resized) #make prediction & fill pred_class
    if pred >= 0.5:
        pred_class = 'Uninfected'
    else:
        pred_class = 'Parasitized'
    st.image(image_upload)
    st.write(f'Prediction: {pred_class}')
    st.write(f'Prediction Value: {pred[0][0]}')
