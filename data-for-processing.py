import pandas as pd
import pickle 

heart_data = pd.read_csv('data/heart.csv')

save_path = 'data/data-for-modelling.pkl'

# print first 5 rows of the dataset
heart_data.head()

# print last 5 rows of the dataset
heart_data.tail()

# number of rows and column in the dataset
heart_data.shape

# getting some info about the data
heart_data.info()

# checking for missing values
heart_data.isnull() .sum()

# statistical measures about the data
heart_data.describe()

# checking the distribution of target variables
heart_data['target'].value_counts()

# Save 
with open(save_path, "wb") as pickle_out:
    pickle.dump(heart_data  , pickle_out)