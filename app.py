import streamlit as st
import numpy as np
import pandas as pd
import joblib

model = joblib.load('churn.joblib')

column = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
                'PhoneService', 'MultipleLines', 'OnlineSecurity', 'OnlineBackup',
                'InternetService_Bank transfer (automatic)']

gender = st.selectbox("Gender", ['male', 'female'])
senior_citizen = st.selectbox("Senior Citizen", ['Yes', 'No'])
partner = st.selectbox("Partner", ['Yes', 'No'])
dependents = st.selectbox("Dependents", ['Yes', 'No'])
tenure = st.slider("tenure", 0, 1000, 0)
phone_service = st.selectbox("Phone Service", ['Yes', 'No'])
multiple_lines = st.selectbox("Multiple Lines", ['Yes', 'No'])
online_security = st.selectbox("Online Security", ['Yes', 'No'])
online_backup = st.selectbox("Online Backup", ['Yes', 'No'])
internet_service_bank = st.selectbox("Internet Service Bank transfer (automatic)", ['Yes', 'No'])

gender1 = 1 if gender == 'female' else 0
senior_citizen1 = 1 if senior_citizen == 'Yes' else 0
partner1 = 1 if partner == 'Yes' else 0
dependents1 = 1 if dependents == 'Yes' else 0
phone_service1 = 1 if phone_service == 'Yes' else 0
multiple_lines1 = 1 if multiple_lines == 'Yes' else 0
online_security1 = 1 if online_security == 'Yes' else 0
online_backup1 = 1 if online_backup == 'Yes' else 0
internet_service_bank1 = 1 if internet_service_bank == 'Yes' else 0


def predict(): 
    row = np.array([gender1, senior_citizen1, partner1, dependents1, tenure, phone_service1, multiple_lines1, online_security1, online_backup1, internet_service_bank1]) 
    X = pd.DataFrame([row], columns = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
                'PhoneService', 'MultipleLines', 'OnlineSecurity', 'OnlineBackup',
                'InternetService_Bank transfer (automatic)'])
    prediction = model.predict(X)
    if prediction[0] == 1: 
        st.success('The customer remains :thumbsup:')
    else: 
        st.error('The customer leaves :thumbsdown:') 

trigger = st.button('Predict', on_click=predict)