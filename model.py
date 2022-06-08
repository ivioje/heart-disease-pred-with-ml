import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from imblearn.under_sampling import RandomUnderSampler


READ_FILE = 'data/data-for-modelling.pkl'
SAVE_PATH = 'log_reg.pkl'

heart_data = pd.read_pickle(READ_FILE)

X = heart_data.drop(columns='target', axis=1)
y = heart_data['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

model = LogisticRegression()
# training the LogisticsRegression model with training data
model.fit(X_train, y_train)

# using balanced weights
model_bal = LogisticRegression(max_iter=500, class_weight="balanced")
model_bal.fit(X_train, y_train)

# undersampling
undersample = RandomUnderSampler(sampling_strategy="majority")
X_over, y_over = undersample.fit_resample(X, y)
X_train, X_test, y_train, y_test = train_test_split(
    X_over, y_over, test_size=0.2, random_state=2022)

model_us = LogisticRegression(max_iter=500)
model_us.fit(X_train, y_train)

X_train_prediction = model_us.predict(X_train)
X_test_prediction = model_us.predict(X_test)

# accuracy on training data
training_data_accuracy = accuracy_score(X_train_prediction, y_train)
print('Accuracy on Training data : ', training_data_accuracy)
print('Confudion matrix: \n----------------------------------------')

# accuracy on test data
test_data_accuracy = accuracy_score(X_test_prediction, y_test)
print('Accuracy on Test data : ', test_data_accuracy)
print('Confusion matrix: \n----------------------------------------')
print(confusion_matrix(X_test_prediction, y_test))
print('\n----------------------------------------')
print(classification_report(X_test_prediction, y_test))

# Saving the final model
with open(SAVE_PATH, "wb") as pickle_out:
    pickle.dump(model, pickle_out)
