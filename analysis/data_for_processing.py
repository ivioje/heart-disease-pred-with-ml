#import necessary modules
import pandas as pd

#load data
READ_PATH = pd.read_csv('/data/heart_2020_cleaned.csv')
SAVE_PATH = 'analysis/data_for_modelling.pkl'

READ_PATH.head()

READ_PATH.info()

"""Aim is to predict the pocssibility of a patient
having heart disease (in percentage), given that other 
medical attributes of the patient is provided."""
#rename the HeartDisease column to label
READ_PATH = READ_PATH.rename({
    'HeartDisease': 'label'
}, axis=1)

#change all boolean No and Yes values to 0 and 1 respectively
READ_PATH["label"] = READ_PATH["label"].replace({
    "Yes": 1,
    "No": 0
})
READ_PATH["Smoking"] = READ_PATH["Smoking"].replace({
    "Yes": 1,
    "No": 0
})
READ_PATH["AlcoholDrinking"] = READ_PATH["AlcoholDrinking"].replace({
    "Yes": 1,
    "No": 0
})
READ_PATH["Stroke"] = READ_PATH["Stroke"].replace({
    "Yes": 1,
    "No": 0
})
READ_PATH["DiffWalking"] = READ_PATH["DiffWalking"].replace({
    "Yes": 1,
    "No": 0
})
READ_PATH["PhysicalActivity"] = READ_PATH["PhysicalActivity"].replace({
    "Yes": 1,
    "No": 0
})
READ_PATH["Asthma"] = READ_PATH["Asthma"].replace({
    "Yes": 1,
    "No": 0
})
READ_PATH["KidneyDisease"] = READ_PATH["KidneyDisease"].replace({
    "Yes": 1,
    "No": 0
})
READ_PATH["SkinCancer"] = READ_PATH["SkinCancer"].replace({
    "Yes": 1,
    "No": 0
})

#change the options of categorical variables to values
READ_PATH["Sex"] = READ_PATH["Sex"].replace({
    "Male": 0,
    "Female": 1
})
READ_PATH["AgeCategory"] = READ_PATH["AgeCategory"].replace({
    "18-24": 0,
    "25-29": 1,
    "30-34": 2,
    "35-39": 3,
    "40-44": 4,
    "45-49": 5,
    "50-54": 6,
    "55-59": 7,
    "60-64": 8,
    "65-69": 9,
    "70-74": 10,
    "75-79": 11,
    "80 or older": 12
})
READ_PATH["Race"] = READ_PATH["Race"].replace({
    "American Indian/Alaskan Native": 0,
    "Asian": 1,
    "Black": 2,
    "Hispanic": 3, 
    "Other": 4,
    "White": 5
})
READ_PATH["Diabetic"] = READ_PATH["Diabetic"].replace({
    "No": 0,
    "Yes": 1,
    "No, borderline diabetes": 2,
    "Yes (during pregnancy)": 3, 
})
READ_PATH["GenHealth"] = READ_PATH["GenHealth"].replace({
    "Excellent": 0,
    "Fair": 1,
    "Good": 2,
    "Poor": 3, 
    "Very good": 4,
})

# Plot showing the initial distribution of data for the label
READ_PATH.label.value_counts().plot(kind="bar", color=["salmon", "lightblue"])

# Pickle is a python module used to serialize a python object into a
# binary format and deserialize it back to the python object. 
READ_PATH.to_pickle(SAVE_PATH)