# import necessary libraries
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from imblearn.under_sampling import RandomUnderSampler

# Load file
READ_FILE = 'data_for_modelling.pkl'
SAVE_FILE = 'logistic_regression.pkl'

# save the pickled file to a variable called heartData
heartData = pd.read_pickle(READ_FILE)

# Separate the target column (label) from the other columns
y = heartData["label"]
X = heartData.drop("label", axis=1)

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# train model

log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

# using balanced weights
log_reg_bal = LogisticRegression(max_iter=500, class_weight="balanced")
log_reg_bal.fit(X_train, y_train)

# undersampling
undersample = RandomUnderSampler(sampling_strategy="majority")
X_over, y_over = undersample.fit_resample(X, y)
X_train, X_test, y_train, y_test = train_test_split(
    X_over, y_over, test_size=0.2, random_state=2022)

log_reg_us = LogisticRegression(max_iter=500)
log_reg_us.fit(X_train, y_train)

y_pred = log_reg_us.predict(X_test)

# Model evaluation
print('Accuracy score: ', round(accuracy_score(y_test, y_pred) * 100), '%')
print('--------------------------------------- \n')
print(classification_report(y_test, y_pred))
print('--------------------------------------- \n')
print('Confusion matrix: \n', confusion_matrix(y_test, y_pred))

# Saving the final model
with open(SAVE_FILE, "wb") as pickle_out:
    pickle.dump(log_reg, pickle_out)
