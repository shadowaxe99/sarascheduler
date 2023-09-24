import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv('data.csv')

# Check if the dataset has at least two samples
if len(data) < 2:
    print('Error: Insufficient data to calculate the model score.')
    exit()

# Split the dataset into features and target
X = data[['feature1', 'feature2']]
y = data['target']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
score = model.score(X_test, y_test)

# Print the score
print('Model Score:', score)
