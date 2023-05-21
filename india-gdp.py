# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Step 2: Load and preprocess the data
data = pd.read_csv('gdp_data.csv')  # Replace 'gdp_data.csv' with your dataset file
# Perform data preprocessing steps like handling missing values, outliers, etc.

# Step 3: Split the data into training and testing sets
train_data = data.iloc[:-12]  # Use all but the last 12 months for training
test_data = data.iloc[-12:]   # Use the last 12 months for testing

# Step 4: Create SARIMA model
model = SARIMAX(train_data['GDP'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))

# Step 5: Train the model
model_fit = model.fit()

# Step 6: Make predictions
predictions = model_fit.forecast(steps=len(test_data))

# Step 7: Evaluate the model
mse = mean_squared_error(test_data['GDP'], predictions)
rmse = np.sqrt(mse)
print("Root Mean Squared Error (RMSE):", rmse)

# Step 8: Visualize the results
plt.plot(train_data['Year'], train_data['GDP'], label='Train Data')
plt.plot(test_data['Year'], test_data['GDP'], label='Actual GDP')
plt.plot(test_data['Year'], predictions, label='Predicted GDP')
plt.xlabel('Year')
plt.ylabel('GDP')
plt.title('India GDP Prediction')
plt.legend()
plt.show()
