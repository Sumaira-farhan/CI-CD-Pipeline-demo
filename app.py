import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("Student Pass Prediction App")

hours = st.number_input("Enter study hours"

if st.button("Predict"):
    prediction = model.predict([[hours]])

    if prediction[0] == 1:
        st.success("Student will PASS 🎉")
    else:
        st.error("Student may FAIL ❌")
