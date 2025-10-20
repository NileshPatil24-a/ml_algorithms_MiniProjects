import streamlit as st
import pickle
import numpy as np 

st.title('House Price Prediction ')
model = pickle.load(open('file.pkl', 'rb'))
data = pickle.load(open('data.pkl', 'rb'))

bedrooms = st.number_input("Enter the number of bedrooms")
bathrooms = st.number_input("Enter the number of bathrooms")
floors = st.number_input("Enter the number of floors")
waterfront = st.number_input("Enter the number of waterfront")
view = st.number_input("Enter the number of view")
condition = st.number_input("Enter the number of condition")
Year_of_built = st.number_input("Enter the number of Year_of_built")
Total_Area = st.number_input("Enter the number of Total_Area")



if st.button('predict'):
    arr = np.array([[bedrooms,bathrooms,floors,waterfront,view,condition,Year_of_built,Total_Area]])
    y_pred = model.predict(arr)
    st.write(f"Price of the House is {y_pred[0][0].astype(int)}")



# 3	3	2	0	0	4	1988	10502