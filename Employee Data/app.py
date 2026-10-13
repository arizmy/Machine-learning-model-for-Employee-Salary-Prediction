#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 06:00:31 2026

@author: wealth
"""

import pandas as pd
import streamlit as st
import pickle

filename = 'employee data.sav'
model = pickle.load(open(filename,'rb'))
                    
st.title('Employee salary Prediction App')
st.subheader('This app take Certain Variable to Predict Employee Salary')
st.subheader('This App is developed by Wealth')

def user_input():
    Age = st.slider('How old are you?', 0, 100)
    Work_Experience = st.slider('How many years have you work in this field?', 0, 40)
    Qualifications = st.selectbox('what is your qualification?, Hint 1 for NCE, 2 for ND, 3 for HND, 4 for B.Sc, 5 for MSc', options = [5,4,3,2,1], index=4)
    Grade_Level = st.slider('What is your grade level?', 5, 16)
    Emloyment_Type = st.selectbox('what is your Employement Classification?, Hint 1 for Permananent, 2 for Contract', options = [2,1], index=1)
    Marital_Status = st.selectbox('what is your Marital status?, Hint 1 for Single, 2 for Married', options = [2,1], index=1)
    
    
    data = {
        'Age': Age,
        'W_Experience': Work_Experience,
        'Qualifications': Qualifications,
        'Grade': Grade_Level,
        'Employment_Type': Emloyment_Type,
        'Marital_Status': Marital_Status,
        }
    
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input()
def Prediction():
    Predict = model.predict(df)
    return Predict


submit = st.button('Get prediction')
result = Prediction()
if submit:
    st.success('Thank you for filling the form. your salary is {}'.format(result*1000000))