import streamlit as st
import pandas as pd
import joblib
from streamlit_option_menu import option_menu
import streamlit.components.v1 as component

# Menu items
selected = option_menu(
    menu_title=None,
    options=['Home', 'Find a doctor', 'Preventive measures'],
    icons=['house', 'activity', 'heart'],
    default_index=0,
    orientation="horizontal",
    styles={
        "nav-link": {
            'background-color': '#bbb'
        },
        "nav-link-selected": {"background-color": '#EA4B48'}
    }
)

# Side bar showing about page info info

st.sidebar.markdown(
    """
    # About this app

    ### Want to keep a healthy heart?
    """)
st.sidebar.image('images/heart.png', caption='Healthy heart', width=150)
st.sidebar.markdown("""
            In seconds, you can determine your risk of heart disease (yes/no) with this app!
            ***

            Using survey data from over 300,000 US citizens from the year 2020, a logistic regression
            model was created.

            The performance ofthe model is above avarage. It achieves an accuracy of about 80%.
    """)

# Assigning the routes to their contents
# Home
if selected == 'Home':
    st.header('Heart disease prediction system')
    st.subheader('Quickly and easily predict the condition of your heart!')

    st.markdown('***')

    if st.checkbox('Show app guide'):
        st.markdown(
            'To predict your heart disease status, simply follow the steps below:')
        st.markdown('1. Enter the parameters that best describe you')
        st.markdown(' 2. Press the "Predict" button and wait for the result')
        st.markdown(
            '>The Body Mass Index (BMI) is a measure of body fat based on height and weight.')
        st.markdown(
            '>BMI= m/h ² , m = mass (in Kilogram) and h = height (in meters).')
        st.markdown('Determine your weight with this [BMI calculator](https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/english_bmi_calculator/bmi_calculator.html)')
        st.markdown('Or determine your BMI by finding your height and weight in this [BMI Index Chart](https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmi_tbl.htm)')

    st.markdown('***')
    st.markdown('**Parameters**')

    gender = st.selectbox("Select your gender", ('Male', 'Female'))
    bmi = st.number_input('Enter BMI')
    physicalHealth = st.number_input(
        'For how many days during the past 30 days was your physical health not good?')
    mentalHealth = st.number_input(
        'For how many days during the past 30 days was your mental health not good?')
    sleepTime = st.number_input('How many hours on avarage do you sleep?')
    smoking = st.selectbox(
        'Have you smoked at least 100 cigarettes in your entire life (approx. 5 packs)?', ('No', 'Yes'))
    drinking = st.selectbox(
        'Do you have more than 14 drinks of alcohol (men) or more than 7 (women) in a week?', ('No', 'Yes'))
    stroke = st.selectbox('Do you have a stroke?', ('No', 'Yes'))
    walking = st.selectbox('Do you have difficulty walking?', ('No', 'Yes'))
    age = st.selectbox('Select your age category', ('18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64',
                                                    '65-69', '70-74', '75-79', '80 or older'))
    race = st.selectbox('Select your race', ('American Indian/Alaskan Native',
                                             'Asian', 'Black', 'Hispanic', 'Other', 'White'))
    diabetic = st.selectbox(
        'Are you diabetic?', ('No', 'No, borderline', 'Yes', 'Yes (during pregnancy)'))
    
    physicalActivity = st.selectbox(
        'Have you played any sports (running, biking, etc.) in the past month?', ('No', 'Yes'))
    
    genHealth = st.selectbox('How can you define your general health?',
                             ('Excellent', 'Fair', 'Poor', 'Good', 'Very good'))
    
    asthma = st.selectbox('Do you have asthma?', ('No', 'Yes'))
    kidneyDisease = st.selectbox('Do you have kidney disease?', ('No', 'Yes'))
    cancer = st.selectbox('Do you have skin cancer?', ('No', 'Yes'))

# predict
    if st.button('Predict'):
        model = joblib.load('model/logistic_regression.pkl')

        X = pd.DataFrame([[bmi, smoking, drinking, stroke, physicalHealth, mentalHealth, walking, gender, age, race, diabetic, physicalActivity,
                           genHealth, sleepTime, asthma, kidneyDisease, cancer]], columns=['BMI', 'Smoking', 'AlcoholDrinking', 'Stroke', 'PhysicalHealth', 'MentalHealth',
                                                                                           'DiffWalking', 'Sex', 'AgeCategory', 'Race', 'Diabetic', 'PhysicalActivity',
                                                                                           'GenHealth', 'SleepTime', 'Asthma',  'KidneyDisease', 'SkinCancer'])
        X = X.replace(['No', 'Yes'], [0, 1])
        X = X.replace(['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64',
                       '65-69', '70-74', '75-79', '80 or older'], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        X = X.replace(['Male', 'Female'], [0, 1])
        X = X.replace(['American Indian/Alaskan Native',
                       'Asian', 'Black', 'Hispanic', 'Other', 'White'], [0, 1, 2, 3, 4, 5])
        X = X.replace(['Excellent', 'Fair', 'Poor', 'Good',
                       'Very good'], [0, 1, 2, 3, 4])
        X = X.replace(['No, borderline', 'Yes (during pregnancy)'], [2, 3])

        prediction = model.predict_proba(X)[0][1] * 100

        st.markdown('***')

        if prediction <= 50:
            st.markdown(
                f"## The probability that you'll have a heart disease is {prediction: .2f}%. You are healthy.")
        elif prediction > 50:
            st.markdown(
                f"## The probability that you'll have a heart disease is {prediction: .2f}%. You need to see a doctor.")
# Find a doctor
if selected == 'Find a doctor':
    component.iframe('https://www.google.com/maps/')

# prevention
if selected == 'Preventive measures':
    st.markdown('''
    # Prevent heart disease
    
    ### According to the CDC, the follwoing are preventive measures for heart disease
    > By living a healthy lifestyle, you can help keep your blood pressure, cholesterol, 
    > and blood sugar levels normal and lower your risk for heart disease and heart attack.
    
    #### Choose Healthy Habits
    You can choose healthy habits to help prevent heart disease.
    
    ##### 1. Choose Healthy Food and Drinks
    * Choose healthy meals and snacks to help prevent heart disease and its complications. 
      Be sure to eat plenty of fresh fruits and vegetables and fewer processed foods.
    * Eating lots of foods high in saturated fat and trans fat may contribute to heart disease.
    * Eating foods high in fiber and low in saturated fats, trans fat, and cholesterol can help prevent high cholesterol.
    * Limiting salt (sodium) in your diet can also lower your blood pressure.
    * Limiting sugar in your diet can lower your blood sugar level to prevent or help control diabetes. 
    * Do not drink too much alcohol, which can raise your blood pressure. Men should have no more than 2 drinks 
      per day, and women no more than 1 drink per day. 
      For more information, visit [CDC's Alcohol and Public Health website.](https://www.cdc.gov/alcohol/)
   
    ##### 2. Keep a Healthy Weight
    People with overweight or obesity have a higher risk for heart disease. Carrying extra weight can put extra stress 
    on the heart and blood vessels.
    To find out if your weight is in a healthy range, you can [calculate your Body Mass Index 
    (BMI)](https://www.cdc.gov/healthyweight/assessing/bmi/index.html) 
    at [CDC's Assessing Your Weight website](https://www.cdc.gov/healthyweight/assessing/index.html).
   
    ##### 3. Get Regular Physical Activity
    Physical activity can help you maintain a healthy weight and lower your blood pressure, blood cholesterol, 
    and blood sugar levels. For adults, the Surgeon General recommends 2 hours and 30 minutes of moderate-intensity 
    exercise, like brisk walking or bicycling, every week. Children and adolescents should get 1 hour of physical activity every day.
    For more information, see [CDC's Nutrition, Physical Activity, and Obesity website](https://www.cdc.gov/nccdphp/dnpao/index.html).

    ##### 4. Don't Smoke
    Cigarette smoking greatly increases your risk for heart disease. If you don’t smoke, don’t start. If you do smoke, 
    quitting will lower your risk for heart disease. Your doctor can suggest ways to help you quit.
    For more information about tobacco use and quitting, see [CDC's Smoking & Tobacco Use website](https://www.cdc.gov/tobacco/).

    #### Take Charge of Your Medical Conditions
    ##### 1. Check your cholestrol
    Your health care team should test your blood levels of cholesterol at least once every 4 to 6 years. 
    If you have already been diagnosed with high cholesterol or have a family history of the condition, 
    you may need to have your cholesterol checked more often. 
    Talk with your health care team about this simple blood test. If you have high cholesterol, medicines 
    and lifestyle changes can help reduce your risk for heart disease.

    ##### 2. Control Your Blood Pressure
    High blood pressure usually has no symptoms, so have it checked on a regular basis. Your health care team should measure your 
    blood pressure at least once every 2 years if you have never had high blood pressure or other risk factors for heart disease.

    If you have been diagnosed with high blood pressure, also called hypertension, your health care team will measure your blood pressure 
    more often to make sure you have the condition under control. Talk with your health care team about how often you should check your blood pressure.
    You can check it at a doctor's office, at a pharmacy, or at home.

    If you have high blood pressure, your health care team might recommend some changes in your lifestyle, such as lowering the sodium in your diet;
    your doctor may also prescribe medicine to help lower your blood pressure.

    ##### 3. Manage Your Diabetes
    If you have diabetes, monitor your blood sugar levels carefully. Talk with your health care team about treatment options. Your doctor may recommend 
    certain lifestyle changes to help keep your blood sugar under control. These actions will help reduce your risk for heart disease.

    ##### 4. Take Your Medicines as Directed
    If you take medicine to treat high blood cholesterol, high blood pressure, or diabetes, follow your doctor's instructions carefully. Always ask
    questions if you don't understand something. Never stop taking your medicine without first talking to your doctor, nurse, or pharmacist.

    ##### 5. Work With Your Health Care Team
    You and your health care team can work together to prevent or treat the medical conditions that lead to heart disease. Discuss your treatment plan 
    regularly, and bring a list of questions to your appointments. Talk with your health care team about how heart disease and mental health disorders are related.

    If you've already had a heart attack, your health care team will work with you to prevent another one. Your treatment plan may include medicines or surgery and 
    lifestyle changes to reduce your risk. Be sure to take your medicines as directed and follow your doctor's instructions.

     ''')
