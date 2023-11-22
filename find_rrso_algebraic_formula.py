import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

# Load the data from the CSV file
df = pd.read_csv('input.csv')

# Prepare the data
X = df.iloc[:, 0:2]  # First two columns as input features
y = df.iloc[:, 2]    # Third column as the target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Get the coefficients and intercept
coefficients = model.coef_
intercept = model.intercept_

# Predict the values for the entire dataset
y_pred = model.predict(X)

# Calculate the differences
differences = y_pred - y

# Find the index of the max and min difference
max_diff_index = differences.idxmax()
min_diff_index = differences.idxmin()

# Display the instances
print("Instance with Maximum Over-Prediction:")
print("Actual Data:", df.iloc[max_diff_index])
print("Predicted RSSO:", y_pred[max_diff_index])
print("Actual RSSO:", y[max_diff_index])
print("Difference:", differences[max_diff_index])

print("\nInstance with Maximum Under-Prediction:")
print("Actual Data:", df.iloc[min_diff_index])
print("Predicted RSSO:", y_pred[min_diff_index])
print("Actual RSSO:", y[min_diff_index])
print("Difference:", differences[min_diff_index])

# Print the algebraic formula for calculating RSSO
print("\nAlgebraic Formula for Predicting RSSO:")
print(f"RSSO = {intercept} + ({coefficients[0]}*Feature1) + ({coefficients[1]}*Feature2)")
