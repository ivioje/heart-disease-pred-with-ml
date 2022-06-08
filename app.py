import streamlit as st
import pandas as pd
import joblib

age = st.number_input('Enter age')
sex = st.selectbox("Select your gender", ('Male', 'Female'))
chestPain = st.selectbox(
    'What type of chest pain do you have', ('typical angina', 'atypical angina', 'non-anginal pain', 'asymptomatic'))
trestbps = st.number_input(
    'resting blood pressure (in mm Hg on admission to the hospital)?')
chol = st.number_input('serum cholestoral in mg/dl')
fastingBS = st.selectbox(
    'Is your fasting blood sugar > 120 mg/dl ', ('No', 'Yes'))
ecg = st.selectbox(
    'resting electrocardiographic', ('normal', 'having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)', 'showing probable or definite left ventricular hypertrophy by Estes\' criteria'))
thalach = st.number_input('maximum heart rate achieved')
exang = st.selectbox(
    'exercise induced angina', ('No', 'Yes'))
oldpeak = st.number_input('ST depression induced by exercise relative to rest')
slope = st.selectbox('The slope of the peak exercise ST segemt', ('Upsloping', 'Flat', 'Downsloping'))
ca = st.selectbox('number of major vessels (0-3) colored by flourosopy', ('0', '1', '2', '3'))
thal = st.selectbox('Level of Thalassemia', ('Normal', 'Fixed defect', 'Reversable defect'))

# load model
if st.button('Detect'):
    model = joblib.load('log_reg.pkl')

    X = pd.DataFrame([[age, sex, chestPain, trestbps, chol, fastingBS, ecg, thalach, exang, oldpeak, slope,
                    ca, thal]], columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
                                                                                    'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'])

    X = X.replace(['No', 'Yes'], [0, 1])
    X = X.replace(['typical angina', 'atypical angina', ' non-anginal pain', 'asymptomatic'], [0, 1, 2, 3])
    X = X.replace(['Male', 'Female'], [1, 0])
    X = X.replace(['normal', 'having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)', 'showing probable or definite left ventricular hypertrophy by Estes\' criteria'], [0, 1, 2])
    X = X.replace(['Upsloping', 'Flat', 'Downsloping'], [0, 1, 2])
    X = X.replace(['0', '1', '2', '3'], [0,1,2,3])
    X = X.replace(['Normal', 'Fixed defect', 'Reversable defect'], [0,1,2])


    prediction = model.predict(X)[0]

    st.markdown('***')

    if prediction == 0:
        st.markdown("**Age: {age}")
        f'Age: {age}', f'Gender: {sex}', f'cp: {chestPain}', f'trestbps: {trestbps}', f'chol: {chol}', f'fastingBS: {fastingBS}',
        f'ecg: {ecg}', f'thalach: {thalach}', f'exang: {exang}', f'oldpeak: {oldpeak}', f'slope: {slope}', f'ca: {ca}', f'thal: {thal}'
        st.markdown(
            "### You do not have heart disease.")
    elif prediction == 1:
        st.markdown(f"* Age - {age}")
        f'Age: {age}', f'Gender: {sex}', f'cp: {chestPain}', f'trestbps: {trestbps}', f'chol: {chol}', f'fastingBS: {fastingBS}',
        f'ecg: {ecg}', f'thalach: {thalach}', f'exang: {exang}', f'oldpeak: {oldpeak}', f'slope: {slope}', f'ca: {ca}', f'thal: {thal}'
        st.markdown(
            "### You have heart disease.")
