# Import libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.feature_selection import SelectFromModel

# Load data
titanic_df = pd.read_csv('tested.csv')

# Preprocess data
titanic_df.drop(columns='Cabin', axis=1, inplace=True)
titanic_df['Age'].fillna(titanic_df['Age'].mean(), inplace=True)
titanic_df['Fare'].fillna(titanic_df['Fare'].mean(), inplace=True)
titanic_df['Embarked'].fillna(titanic_df['Embarked'].mode()[0], inplace=True)
titanic_df.replace({'Sex': {'male': 0, 'female': 1}, 'Embarked': {'S': 0, 'C': 1, 'Q': 2}}, inplace=True)

# Separate features and target
X = titanic_df.drop(columns=['PassengerId', 'Name', 'Ticket', 'Survived'], axis=1)
Y = titanic_df['Survived']

# Handle missing values
X = X.dropna()
Y = Y.dropna()

# Split data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

# Feature selection with Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=2)
selector = SelectFromModel(rf, threshold=0.05)
X_train_selected = selector.fit_transform(X_train, Y_train)
X_test_selected = selector.transform(X_test, Y_train)

# Train Random Forest model
rf.fit(X_train_selected, Y_train)

# Evaluate model
Y_train_pred = rf.predict(X_train_selected)
Y_test_pred = rf.predict(X_test_selected)

train_accuracy = accuracy_score(Y_train, Y_train_pred)
test_accuracy = accuracy_score(Y_test, Y_test_pred)
train_precision = precision_score(Y_train, Y_train_pred)
train_recall = recall_score(Y_train, Y_train_pred)
train_f1 = f1_score(Y_train, Y_train_pred)
test_precision = precision_score(Y_test, Y_test_pred)
test_recall = recall_score(Y_test, Y_test_pred)
test_f1 = f1_score(Y_test, Y_test_pred)

# Print results
print("Train accuracy:", train_accuracy)
print("Test accuracy:", test_accuracy)
print("Train precision:", train_precision)
print("Train recall:", train_recall)
print("Train F1 score:", train_f1)
print("Test precision:", test_precision)
print("Test recall:", test_recall)
print("Test F1 score:", test_f1)

# Feature importances
feature_importances = rf.feature_importances_
print(f"Feature importances: {feature_importances}")