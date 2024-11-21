# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Create or Load a Dataset
# For demonstration, let's use a simple example dataset
data = {
    'X': np.random.rand(100) * 100,  # Independent variable
    'y': np.random.rand(100) * 50   # Dependent variable
}
df = pd.DataFrame(data)

# Step 2: Splitting the dataset into Training and Testing sets
X = df[['X']]  # Independent variable (reshape into 2D)
y = df['y']    # Dependent variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Fit a Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model (intercept and slope)
intercept = model.intercept_
slope = model.coef_[0]
print(f"Intercept: {intercept}, Slope: {slope}")

# Step 4: Predict the Test Set Results
y_pred = model.predict(X_test)

# Step 5: Compare Actual Output Values with Predicted Values
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R-squared Value: {r2}")

# Visualization
plt.figure(figsize=(12, 6))

# Visualize Training Set
plt.subplot(1, 2, 1)
plt.scatter(X_train, y_train, color='blue', label='Training Data')
plt.plot(X_train, model.predict(X_train), color='red', label='Regression Line')
plt.title('Training Set')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()

# Visualize Testing Set
plt.subplot(1, 2, 2)
plt.scatter(X_test, y_test, color='green', label='Testing Data')
plt.plot(X_train, model.predict(X_train), color='red', label='Regression Line')  # Using training regression line
plt.title('Testing Set')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()

plt.tight_layout()
plt.show()
