import streamlit as st
import joblib
model=joblib.load(r'C:\Users\thaku\Desktop\My YouTube\Machine Learning\salary_prediction_model.joblib')
st.set_page_config(page_title = "Salary Predictor", page_icon = "💸", layout = "centered")

st.title('Salary Prediction 💰💸')
st.subheader('Years of Experience')

exp=st.slider('',0.0,15.0,0.0)

if exp:
    prediction=model.predict([[exp]])
    st.success(f'Estimate Salary {prediction[0]:.2f}')