import pandas as pd 
import numpy as np 
import streamlit as st
import pickle 

st.title('hello')
filename = 'file.pkl'
model = pickle.load(open(filename,'rb'))

sepal_length = st.number_input('sepal_length  ')
sepal_width = st.number_input('sepal_width ')
petal_length = st.number_input('petal_length ')
petal_width = st.number_input('petal_width  ')

arr = np.array([[sepal_length,sepal_width,petal_length,petal_width]])


if st.button('predict '):
    y_pred = model.predict(arr)
    if y_pred==1:
        st.write('setosa')
        st.image('setosa.jpg')
    elif y_pred==0:
        st.write('versicolor')
        st.image('versicolor.jpg')
    else:
        st.write('virginica')    
        st.image('virginica.jpg')
else:
    st.write('press predict ')