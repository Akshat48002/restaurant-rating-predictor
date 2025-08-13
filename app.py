import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib

st.set_page_config(page_title="Restaurant Rating Predictor", page_icon=":fork_and_knife:", layout="wide")

scaler = joblib.load("scaler.pkl")

st.title("Restaurant Rating Predictor")



st.caption("Predict the rating of a restaurant based on various features.")

st.divider()

averagecost = st.number_input("Please enter the average cost for two people:", min_value=50,max_value=999999,value=1000, step=200)

tablebooking = st.selectbox("Is table booking available?", options=["Yes", "No"])

onlinedelivery = st.selectbox("Is online delivery available?", options=["Yes", "No"])

pricerange = st.selectbox("Please select the price range:", options=[1,2,3,4])

predictbutton = st.button("Predict Rating")

st.divider()

model = joblib.load("mlmodel.pkl")

bookingstatus = 1 if tablebooking == "Yes" else 0
deliverystatus = 1 if onlinedelivery == "Yes" else 0

values = np.array([[averagecost, bookingstatus, deliverystatus, pricerange]])

X = scaler.transform(values)

if predictbutton:
    st.snow()

    prediction = model.predict(X)
    st.write(f"The predicted rating for the restaurant is: {prediction[0]:.2f}")

    if prediction[0] < 2.5:
        st.write("Poor")
    elif prediction[0] < 3.5:
        st.write("Average")
    elif prediction[0] < 4.0:
        st.write("Good")
    elif prediction[0] < 4.5:
        st.write("Very Good")
    else:
        st.write("Excellent")